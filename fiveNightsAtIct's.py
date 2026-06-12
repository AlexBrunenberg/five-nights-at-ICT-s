import pygame, random, time

pygame.init() #Initieert pygame

BREEDTE = 1920 #Geeft de breedte en hoogte aan
HOOGTE = 1080

frame = pygame.display.set_mode((BREEDTE, HOOGTE)) #maakt de frame het gegeven breedte en hoogte

pygame.mixer.init()
fnaf_laugh = pygame.mixer.Sound("fnaf-freddys-laugh.mp3")
fnaf_ambience = pygame.mixer.Sound("fnaf-ambience-extended_trim.mp3")
Camera_sound = pygame.mixer.Sound("fnaf-open-camera-sound.mp3")
lullaby = pygame.mixer.Sound("bonnies-lullaby.mp3")
door_sound = pygame.mixer.Sound("door-slamming-fnaf-1-sound-effects.mp3")
jumpscare_sound = pygame.mixer.Sound("animatronic-in-door.mp3")
Power_out = pygame.mixer.Sound("powerdown.mp3")

clock = pygame.time.Clock() #Klok start, tijd begint te lopen
fps = 15
tijd = 0
tijd_klok = 0
uur = 0
Schermstatus = False
font = pygame.font.SysFont("Arial", 60) #Font en lettergrootte
font_einde = pygame.font.SysFont("Times New Romanq", 250) #Font en lettergrootte
batterij_verbruik = 1
camera_button_status_1 = False
camera_button_status_2 = False
camera_button_status_3 = False
camera_button_status_4 = False

background_office = pygame.image.load("2DeurenOpen.png")
background_office = pygame.transform.scale(background_office, (BREEDTE, HOOGTE))
office_left_close = pygame.image.load("RDeurOpen.png")
office_left_close = pygame.transform.scale(office_left_close, (BREEDTE, HOOGTE))
office_right_close = pygame.image.load("LDeurOpen.png")
office_right_close = pygame.transform.scale(office_right_close, (BREEDTE, HOOGTE))
office_both_close = pygame.image.load("fnafBackground.png")
office_both_close = pygame.transform.scale(office_both_close, (BREEDTE, HOOGTE))
east_hall = pygame.image.load("East Hall _ Five Nights at Freddy's Wiki _ Fandom.jpg")
east_hall = pygame.transform.scale(east_hall, (BREEDTE, HOOGTE))
west_hall = pygame.image.load("West Hall _ Five Nights at Freddy's Wiki _ Fandom.jpg")
west_hall = pygame.transform.scale(west_hall, (BREEDTE, HOOGTE))
dining_area = pygame.image.load("Dining Area _ Five Nights at Freddy's Wiki _ Fandom.jpg")
dining_area = pygame.transform.scale(dining_area, (BREEDTE, HOOGTE))
show_stage = pygame.image.load("Show Stage _ Fnafapedia Wikia _ Fandom.png")
show_stage = pygame.transform.scale(show_stage, (BREEDTE, HOOGTE))
colson_normaal = pygame.image.load("ColsonGeenAchtergrond.png")

class Button:
    def __init__(self, x:int,y:int,width:int,height:int,color:any) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    def draw_button(self,text:str, c1:int, c2:int, c3:int) -> None:
        pygame.draw.rect(frame,(c1, c2, c3), (self.x, self.y, self.width, self.height))
        frame.blit((font.render(text, True, (255, 255, 255))), ((self.x), self.y+((self.height/2)-60)))
    def check_click(self,pos:tuple) -> int:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
        else:
            return 0
    
l_button_door = Button(240, 500, 120,120,(0,255,0))
button_camera = Button(900, 960, 120, 120,(255,255,255))
r_button_door = Button(1570, 500, 120,120,(0,255,0))

button_camera_1 = Button(1600, 300, 120, 120,(255,255,255))
button_camera_2 = Button(1600, 600, 120, 120,(255,255,255))
button_camera_3 = Button(1450, 900, 120, 120,(255,255,255))
button_camera_4 = Button(1750, 900, 120, 120,(255,255,255))

class Monster:
    def __init__(self, afbeelding:str, difficulty:int) -> None:
        self.difficulty = difficulty
        self.afbeelding = pygame.image.load(afbeelding)
        self.afbeelding = pygame.transform.scale(self.afbeelding, (BREEDTE, HOOGTE))
        self.progress = 0
        self.monster_actief = False
        self.cooldown_teller = 0
        self.attack_risk = 0
        self.monster_chance = 0
    def monster_tonen(self,x:int,y:int) -> None:
        frame.blit(self.afbeelding,(x,y))
    def monster_jumpscare(self, afbeelding:str) -> None:
        for zoom in range(1, 10, 1):
            zoom = zoom/10
            frame.fill((0,0,0))
            self.afbeelding = pygame.image.load(afbeelding)
            self.afbeelding = pygame.transform.scale(self.afbeelding, ((BREEDTE*zoom), (HOOGTE*zoom)))
            frame.blit(self.afbeelding,(960-(0.5*(BREEDTE*zoom)), 540-(0.5*(HOOGTE*zoom))))
            pygame.display.flip()        
        self.afbeelding = pygame.image.load(afbeelding)
        self.afbeelding = pygame.transform.scale(self.afbeelding, (BREEDTE, HOOGTE))
    def difficulty_spike(self, int_spike:int) -> None:
        self.difficulty += int_spike
    def monster_move(self) -> None:
        self.monster_chance = random.randint(0,((30-self.difficulty)*fps))
        if self.monster_chance == 1 and self.cooldown_teller <= 0 and self.progress != 6:
            self.cooldown_teller = 3*fps
            self.progress += 1
        elif self.cooldown_teller > 0:
            self.cooldown_teller -= 1
    def spawn(self) -> bool:
        self.monster_actief = True
        return self.monster_actief
    def attack(self) -> bool:
        if self.attack_risk > self.monster_chance:
            return True
        else:
            self.attack_risk += 0.1 + (0.1 * self.difficulty)


colson = Monster("colsonJumpscare.png", 0)



class Camera:
    def __init__(self, camera_nummer:int) -> None:
        self.camera_clicked = 0
        self.camera_button_status = 0
        self.camera_nummer = camera_nummer
    def camera_gebruiken(self, button:Button,) -> None:
        global camera_button_status_1, camera_button_status_2, camera_button_status_3, camera_button_status_4
        if button.check_click(pos) == 1 and self.camera_clicked == 0 :
            self.camera_clicked = 1
            self.camera_button_status = 1
            if self.camera_nummer == 1:
                camera_button_status_1 = self.camera_button_status
                camera_button_status_2 = False
                camera_button_status_3 = False
                camera_button_status_4 = False
            if self.camera_nummer == 2:
                camera_button_status_1 = False
                camera_button_status_2 = self.camera_button_status
                camera_button_status_3 = False
                camera_button_status_4 = False
            if self.camera_nummer == 3:
                camera_button_status_1 = False
                camera_button_status_2 = False
                camera_button_status_3 = self.camera_button_status
                camera_button_status_4 = False
            if self.camera_nummer == 4:
                camera_button_status_1 = False
                camera_button_status_2 = False
                camera_button_status_3 = False
                camera_button_status_4 = self.camera_button_status
            Camera_sound.play()
        elif button.check_click(pos) == 0 and self.camera_clicked == 1:
            self.camera_clicked = 0


camera_1 = Camera(1)
camera_2 = Camera(2)
camera_3 = Camera(3)
camera_4 = Camera(4)
    

batterij_totaal = 600
batterij_status = True
Lc1, Rc1 = 100, 100
Lc2, Rc2 = 100, 100
Lc3, Rc3 = 100, 100
pos = (0,0,0,0)
l_button_status, r_button_status, camera_button_status = 0, 0, 0
l_clicked, r_clicked, camera_clicked = 0, 0, 0
stage_area_monster = False
dining_area_monster = False
left_hallway_monster = False
right_hallway_monster = False
left_door_monster = False
right_door_monster = False
hallway_keuze = 0
random_factor_keuze = 0
powerplay_status = 0
area_lijst = [stage_area_monster,dining_area_monster,hallway_keuze,left_hallway_monster,left_door_monster,right_hallway_monster,right_door_monster]
fnaf_ambience.play()
colson_actief = colson.spawn()
jumpscare = False
while True:
    pygame.event.pump() # start pygame
    clock.tick(fps) # zet de fps op 60
    toetsen = pygame.key.get_pressed()  # maak een variabele om te kijken of een toets word ingedrukt

    if toetsen[pygame.K_q]: # stop de pygame door q in te drukken of door het kruisje rechts boven aan te klikken in pygame
         break
        #Deuren functies
    if jumpscare == True:
        frame.fill((0,0,0))
        pygame.display.flip()
        lullaby.play()
        time.sleep(1)
        fnaf_laugh.play()
        time.sleep(6)
        colson.monster_jumpscare("colsonJumpscare.png")
        colson.monster_tonen(0,0)
        jumpscare_sound.play()
        frame.blit((font_einde.render("0/10", True, (255, 0, 0))), ((1400), (140))) 
        pygame.display.flip()
        time.sleep(0.7)
        break
    elif jumpscare == False:
        for event in pygame.event.get():
            if l_button_door.check_click(pos) == 1 and l_clicked == False and batterij_status == 1 and camera_button_status == False:
                l_button_status = not l_button_status  # wisselt tussen True en False
                door_sound.play()
                if l_button_status == True:
                    Lc1 = 255
                    Lc2 = 0
                    Lc3 = 0
                    batterij_verbruik += 1
                else:
                    Lc1 = 100
                    Lc2 = 100
                    Lc3 = 100
                    batterij_verbruik -= 1
                l_clicked = True
            elif l_button_door.check_click(pos) == 0 and l_clicked == True:
                l_clicked = False
                
            if r_button_door.check_click(pos) == 1 and r_clicked == False and batterij_status == 1 and camera_button_status == False:
                r_button_status = not r_button_status  # wisselt tussen True en False
                door_sound.play()
                if r_button_status == True:
                    Rc1 = 255
                    Rc2 = 0
                    Rc3 = 0
                    batterij_verbruik += 1
                else:
                    Rc1 = 100
                    Rc2 = 100
                    Rc3 = 100
                    batterij_verbruik -= 1
                r_clicked = True
            elif r_button_door.check_click(pos) == 0 and r_clicked == True:
                r_clicked = False

            if button_camera.check_click(pos) == 1 and camera_clicked == False:
                camera_button_status = not camera_button_status  # wisselt tussen True en False
                if camera_button_status == True:
                    batterij_verbruik += 1
                else:
                    batterij_verbruik -= 1
                camera_clicked = True
            elif button_camera.check_click(pos) == 0 and camera_clicked == True:
                camera_clicked = False
    if colson_actief:
        area_lijst[colson.progress] = True
        colson.monster_move()
        if colson.progress == 2 and random_factor_keuze == 0:
            colson.progress = 3
        elif colson.progress == 2 and random_factor_keuze == 1:
            colson.progress = 5
        if colson.progress == 4:
            attack_check = colson.attack()
            if attack_check == True and l_button_status == False:
                jumpscare = True
            elif attack_check == True and l_button_status == True:
                colson.progress = 0
                attack_check = False
        if colson.progress == 6:
            attack_check = colson.attack()
            if attack_check == True and r_button_status == False:
                jumpscare = True
            elif attack_check == True and r_button_status == True:
                colson.progress = 0
                attack_check = False
        if batterij_totaal <= 0:
            batterij_status = False
            r_button_status = False
            l_button_status = False
            powerplay_status += 1
        if powerplay_status == 1:
            Power_out.play()
        if (tijd % 15) == 0:
            tijd_klok += 1
            batterij_totaal -= batterij_verbruik
            random_factor = random.randint(0,120)
            random_factor_keuze = random.randint(0,1)
            if random_factor == 60:
                fnaf_ambience.play()
            elif random_factor == 59:
                fnaf_laugh.play()
        
        if tijd_klok == 60:
            colson.difficulty_spike(1)
            uur += 1
            tijd_klok = 0

        klok = font.render(str(uur), True, (255,255,255))
        batterij = font.render(str(batterij_totaal), True, (255,255,255))
        if uur == 6:
            frame.fill((0,0,0))
            frame.blit((font_einde.render("You Win", True, (0, 255, 0))), ((650), (140))) 
            pygame.display.flip()
            time.sleep(10)
            break 


        frame.fill((0,0,0))
        if camera_button_status == False:
            if r_button_status == False and l_button_status == False:
                frame.blit(background_office, (0, 0))
                if colson.progress == 4:
                    frame.blit(colson_normaal, (250,250))
                elif colson.progress == 6:
                    frame.blit(colson_normaal, (1150,250))
            elif r_button_status == True and l_button_status == True:
                frame.blit(office_both_close,(0,0))
            elif r_button_status:
                frame.blit(office_right_close,(0,0))
                if colson.progress == 4:
                    frame.blit(colson_normaal, (250,250))
            elif l_button_status:
                frame.blit(office_left_close,(0,0))
                if colson.progress == 6:
                    frame.blit(colson_normaal, (1150,250))
            r_button_door.draw_button("door", Rc1,Rc2,Rc3)
            l_button_door.draw_button("door", Lc1,Lc2,Lc3)
        else:
            camera_1.camera_gebruiken(button_camera_1)
            if camera_button_status_1 == True:
                frame.blit(show_stage, (0, 0))
                if colson.progress == 0:
                    frame.blit(colson_normaal, (800,250))
            camera_2.camera_gebruiken(button_camera_2)
            if camera_button_status_2 == True:
                frame.blit(dining_area, (0, 0)) 
                if colson.progress == 1:
                    frame.blit(colson_normaal, (800,250))
            camera_3.camera_gebruiken(button_camera_3)  
            if camera_button_status_3 == True:
                frame.blit(east_hall, (0, 0))
                if colson.progress == 3:
                    frame.blit(colson_normaal, (800,250))
            camera_4.camera_gebruiken(button_camera_4)
            if camera_button_status_4 == True:
                frame.blit(west_hall, (0, 0))
                if colson.progress == 5:
                    frame.blit(colson_normaal, (1150,250))
            button_camera_1.draw_button("show", 100,100,100)
            button_camera_2.draw_button("dining", 100,100,100)
            button_camera_3.draw_button("east", 100,100,100)
            button_camera_4.draw_button("west", 100,100,100)
        button_camera.draw_button("camera", 100,100,100)
        frame.blit(klok, (0, 1020))
        frame.blit(batterij, (0, 920)) 

        pygame.display.flip()
        tijd += 1 # doe 1 bij variabele tijd


pygame.quit() # stop pygame als de while loop is gedaan 