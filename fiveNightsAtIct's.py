import pygame, random, time

pygame.init() #Initieert pygame

BREEDTE = 1920 #Geeft de breedte en hoogte aan
HOOGTE = 1080

frame = pygame.display.set_mode((BREEDTE, HOOGTE)) #maakt de frame het gegeven breedte en hoogte

pygame.mixer.init()
Fnaf_laugh = pygame.mixer.Sound("fnaf-freddys-laugh.mp3")
Fnaf_ambience = pygame.mixer.Sound("fnaf-ambience-extended_trim.mp3")
Camera_sound = pygame.mixer.Sound("fnaf-open-camera-sound.mp3")
Lullaby = pygame.mixer.Sound("bonnies-lullaby.mp3")
Door_sound = pygame.mixer.Sound("door-slamming-fnaf-1-sound-effects.mp3")
Jumpscare_sound = pygame.mixer.Sound("animatronic-in-door.mp3")
Power_out = pygame.mixer.Sound("powerdown.mp3")

clock = pygame.time.Clock() #Klok start, tijd begint te lopen
fps = 30
tijd = 0
tijdKlok = 0
uur = 0
Schermstatus = False
font = pygame.font.SysFont("Arial", 60) #Font en lettergrootte
fontEinde = pygame.font.SysFont("Times New Romanq", 250) #Font en lettergrootte
BatterijVerbruik = 1
cameraButtonStatus1 = False
cameraButtonStatus2 = False
cameraButtonStatus3 = False
cameraButtonStatus4 = False

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
colsonNormaal = pygame.image.load("ColsonGeenAchtergrond.png")
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
    def check_click(self,pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
        else:
            return 0
    
LbuttonDoor = Button(240, 500, 120,120,(0,255,0))
buttonCamera = Button(900, 960, 120, 120,(255,255,255))
RbuttonDoor = Button(1570, 500, 120,120,(0,255,0))

buttonCamera1 = Button(1600, 300, 120, 120,(255,255,255))
buttonCamera2 = Button(1600, 600, 120, 120,(255,255,255))
buttonCamera3 = Button(1450, 900, 120, 120,(255,255,255))
buttonCamera4 = Button(1750, 900, 120, 120,(255,255,255))

class Monster:
    def __init__(self, afbeelding, difficulty) -> None:
        self.difficulty = difficulty
        self.afbeelding = pygame.image.load(afbeelding)
        self.afbeelding = pygame.transform.scale(self.afbeelding, (BREEDTE, HOOGTE))
        self.progress = 0
        self.Monster_actief = False
        self.cooldown_teller = 0
        self.attack_risk = 0
        self.Monster_chance = 0
    def monsterTonen(self,x,y) -> None:
        frame.blit(self.afbeelding,(x,y))
    def DifficultySpike(self, int_spike) -> None:
        self.difficulty += int_spike
    def MonsterMove(self) -> None:
        self.Monster_chance = random.randint(0,((30-self.difficulty)*fps))
        if self.Monster_chance == 1 and self.cooldown_teller <= 0:
            self.cooldown_teller = 3*fps
            self.progress += 1
        elif self.cooldown_teller > 0:
            self.cooldown_teller -= 1
    def Spawn(self) -> None:
        self.Monster_actief = True
        return self.Monster_actief
    def Attack(self) -> None:
        if self.attack_risk > self.Monster_chance:
            return True
        else:
            self.attack_risk += 0.1 + (0.1 * self.difficulty)

        

class Camera:
    def __init__(self, cameraNummer:int) -> None:
        self.cameraClicked = 0
        self.cameraButtonStatus = 0
        self.cameraNummer = cameraNummer
    def camera_gebruiken(self, button:Button,):
        global cameraButtonStatus1, cameraButtonStatus2, cameraButtonStatus3, cameraButtonStatus4
        if button.check_click(pos) == 1 and self.cameraClicked == 0 :
            self.cameraClicked = 1
            self.cameraButtonStatus = 1
            if self.cameraNummer == 1:
                cameraButtonStatus1 = self.cameraButtonStatus
                cameraButtonStatus2 = False
                cameraButtonStatus3 = False
                cameraButtonStatus4 = False
            if self.cameraNummer == 2:
                cameraButtonStatus1 = False
                cameraButtonStatus2 = self.cameraButtonStatus
                cameraButtonStatus3 = False
                cameraButtonStatus4 = False
            if self.cameraNummer == 3:
                cameraButtonStatus1 = False
                cameraButtonStatus2 = False
                cameraButtonStatus3 = self.cameraButtonStatus
                cameraButtonStatus4 = False
            if self.cameraNummer == 4:
                cameraButtonStatus1 = False
                cameraButtonStatus2 = False
                cameraButtonStatus3 = False
                cameraButtonStatus4 = self.cameraButtonStatus
            Camera_sound.play()
        elif button.check_click(pos) == 0 and self.cameraClicked == 1:
            self.cameraClicked = 0


camera1 = Camera(1)
camera2 = Camera(2)
camera3 = Camera(3)
camera4 = Camera(4)

Colson = Monster("colsonJumpscare.png", 0)
    

BatterijTotaal = 800
BatterijStatus = True
Lc1, Rc1 = 100, 100
Lc2, Rc2 = 100, 100
Lc3, Rc3 = 100, 100
pos = (0,0,0,0)
Lbuttonstatus, RButtonStatus, cameraButtonStatus = 0, 0, 0
Lclicked, Rclicked, cameraClicked = 0, 0, 0
Stage_area_monster = False
Dining_area_monster = False
Left_hallway_monster = False
Right_hallway_monster = False
Left_door_monster = False
Right_door_monster = False
Hallway_keuze = 0
Random_factor_keuze = 0
Area_lijst = [Stage_area_monster,Dining_area_monster,Hallway_keuze,Left_hallway_monster,Left_door_monster,Right_hallway_monster,Right_door_monster]
Fnaf_ambience.play()
Colson_actief = Colson.Spawn()
jumpscare = False
Colson.DifficultySpike(15)
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
        Lullaby.play()
        time.sleep(1)
        Fnaf_laugh.play()
        time.sleep(6)
        Colson.monsterTonen(0,0)
        Jumpscare_sound.play()
        frame.blit((fontEinde.render("0/10", True, (255, 0, 0))), ((1400), (140))) 
        pygame.display.flip()
        time.sleep(0.7)
        break
    elif jumpscare == False:
        for event in pygame.event.get():
            if LbuttonDoor.check_click(pos) == 1 and Lclicked == False and BatterijStatus == 1 and cameraButtonStatus == False:
                Lbuttonstatus = not Lbuttonstatus  # wisselt tussen True en False
                Door_sound.play()
                if Lbuttonstatus == True:
                    Lc1 = 255
                    Lc2 = 0
                    Lc3 = 0
                    BatterijVerbruik += 1
                else:
                    Lc1 = 100
                    Lc2 = 100
                    Lc3 = 100
                    BatterijVerbruik -= 1
                Lclicked = True
            elif LbuttonDoor.check_click(pos) == 0 and Lclicked == True:
                Lclicked = False
                
            if RbuttonDoor.check_click(pos) == 1 and Rclicked == False and BatterijStatus == 1 and cameraButtonStatus == False:
                RButtonStatus = not RButtonStatus  # wisselt tussen True en False
                Door_sound.play()
                if RButtonStatus == True:
                    Rc1 = 255
                    Rc2 = 0
                    Rc3 = 0
                    BatterijVerbruik += 1
                else:
                    Rc1 = 100
                    Rc2 = 100
                    Rc3 = 100
                    BatterijVerbruik -= 1
                Rclicked = True
            elif RbuttonDoor.check_click(pos) == 0 and Rclicked == True:
                Rclicked = False

            if buttonCamera.check_click(pos) == 1 and cameraClicked == False:
                cameraButtonStatus = not cameraButtonStatus  # wisselt tussen True en False
                if cameraButtonStatus == True:
                    BatterijVerbruik += 1
                else:
                    BatterijVerbruik -= 1
                cameraClicked = True
            elif buttonCamera.check_click(pos) == 0 and cameraClicked == True:
                cameraClicked = False
    if Colson_actief:
        Area_lijst[Colson.progress] = True
        Colson.MonsterMove()
        if Colson.progress == 2 and Random_factor_keuze == 0:
            Colson.progress = 3
        elif Colson.progress == 2 and Random_factor_keuze == 1:
            Colson.progress = 5
        if Colson.progress == 4:
            attack_check = Colson.Attack()
            if attack_check == True and Lbuttonstatus == False:
                jumpscare = True
            elif attack_check == True and Lbuttonstatus == True:
                Colson.progress = 0
                attack_check = False
        if Colson.progress == 6:
            attack_check = Colson.Attack()
            if attack_check == True and RButtonStatus == False:
                jumpscare = True
            elif attack_check == True and RButtonStatus == True:
                Colson.progress = 0
                attack_check = False
        if BatterijTotaal <= 0:
            BatterijStatus = False
            RButtonStatus = False
            Lbuttonstatus = False
            Power_out.play()
        if (tijd % 30) == 0:
            tijdKlok += 1
            BatterijTotaal -= BatterijVerbruik
            Random_factor = random.randint(0,120)
            Random_factor_keuze = random.randint(0,1)
            if Random_factor == 60:
                Fnaf_ambience.play()
            elif Random_factor == 59:
                Fnaf_laugh.play()
            elif Random_factor == 58:
                Lullaby.play()
        
        
        if tijdKlok == 60:
            Colson.DifficultySpike(1)
            uur += 1
            tijdKlok = 0

        klok = font.render(str(f"{Colson.progress}l{Colson_actief} {Colson.Monster_chance}"), True, (255,255,255))
        Batterij = font.render(str(BatterijTotaal), True, (255,255,255))
        if uur == 6:
            break 


        frame.fill((0,0,0))
        if cameraButtonStatus == False:
            if RButtonStatus == False and Lbuttonstatus == False:
                frame.blit(background_office, (0, 0))
            elif RButtonStatus == True and Lbuttonstatus == True:
                frame.blit(office_both_close,(0,0))
            elif RButtonStatus:
                frame.blit(office_right_close,(0,0))
            elif Lbuttonstatus:
                frame.blit(office_left_close,(0,0))
            RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
            LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
        else:
            camera1.camera_gebruiken(buttonCamera1)
            if cameraButtonStatus1 == True:
                frame.blit(show_stage, (0, 0))
                if Colson.progress == 0:
                    frame.blit(colsonNormaal, (800,250))
            camera2.camera_gebruiken(buttonCamera2)
            if cameraButtonStatus2 == True:
                frame.blit(dining_area, (0, 0)) 
                if Colson.progress == 1:
                    frame.blit(colsonNormaal, (800,250))
            camera3.camera_gebruiken(buttonCamera3)  
            if cameraButtonStatus3 == True:
                frame.blit(east_hall, (0, 0))
                if Colson.progress == 3:
                    frame.blit(colsonNormaal, (800,250))
            camera4.camera_gebruiken(buttonCamera4)
            if cameraButtonStatus4 == True:
                frame.blit(west_hall, (0, 0))
                if Colson.progress == 5:
                    frame.blit(colsonNormaal, (800,250))
            buttonCamera1.draw_button("show", 100,100,100)
            buttonCamera2.draw_button("dining", 100,100,100)
            buttonCamera3.draw_button("east", 100,100,100)
            buttonCamera4.draw_button("west", 100,100,100)
        buttonCamera.draw_button("camera", 100,100,100)
        frame.blit(klok, (0, 1020))
        frame.blit(Batterij, (0, 920)) 

        pygame.display.flip()
        tijd += 1 # doe 1 bij variabele tijd


pygame.quit() # stop pygame als de while loop is gedaan 