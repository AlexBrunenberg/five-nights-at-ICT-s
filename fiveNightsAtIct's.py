import pygame

pygame.init() #Initieert pygame

BREEDTE = 1920 #Geeft de breedte en hoogte aan
HOOGTE = 1080

frame = pygame.display.set_mode((BREEDTE, HOOGTE)) #maakt de frame het gegeven breedte en hoogte

pygame.mixer.init()
Fnaf_laugh = pygame.mixer.Sound("fnaf-freddys-laugh.mp3")
Fnaf_ambience = pygame.mixer.Sound("fnaf-ambience-extended_trim.mp3")
Camera_sound = pygame.mixer.Sound("fnaf-open-camera-sound.mp3")
Lullaby = pygame.mixer.Sound("bonnies-lullaby.mp3")
Door_sound = pygame.mixer.Sound("animatronic-in-door.mp3")
Jumpscare_sound = pygame.mixer.Sound("animatronic-in-door.mp3")
Power_out = pygame.mixer.Sound("powerdown.mp3")

clock = pygame.time.Clock() #Klok start, tijd begint te lopen
fps = 60
tijd = 0
tijdKlok = 0
uur = 0
Schermstatus = False
font = pygame.font.SysFont("Arial", 60) #Font en lettergrootte
BatterijVerbruik = 1

background_office = pygame.image.load("2DeurenOpen.png")
background_office = pygame.transform.scale(background_office, (BREEDTE, HOOGTE))
office_left_open = pygame.image.load("RDeurOpen.png")
office_left_open = pygame.transform.scale(office_left_open, (BREEDTE, HOOGTE))
office_right_open = pygame.image.load("LDeurOpen.png")
office_right_open = pygame.transform.scale(office_right_open, (BREEDTE, HOOGTE))
office_both_open = pygame.image.load("fnafBackground.png")
office_both_open = pygame.transform.scale(office_both_open, (BREEDTE, HOOGTE))
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

buttonCamera1 = Button(1700, 300, 120, 120,(255,255,255))
buttonCamera2 = Button(1700, 600, 120, 120,(255,255,255))
buttonCamera3 = Button(1700, 900, 120, 120,(255,255,255))

class Monster:
    def __init__(self, afbeelding) -> None:
        self.afbeelding = pygame.image.load(afbeelding)
        self.afbeelding = pygame.transform.scale(self.afbeelding, (BREEDTE/2, HOOGTE/2))
    def monsterTonen(self) -> None:
        frame.blit(self.afbeelding,(250,250))

class Camera:
    def __init__(self):
        self.cameraClicked = 0
        self.cameraButtonStatus = 0
    def camera_gebruiken(self, button:Button, monster:Monster):
        if button.check_click(pos) == 1 and self.cameraClicked == False:
            self.cameraButtonStatus = not self.cameraButtonStatus  # wisselt tussen True en False
            if self.cameraButtonStatus == True:
                # BatterijVerbruik += 1
                print("monster")
                frame.blit(monster, (255,255))
                
            # else:
                # BatterijVerbruik -= 1
            self.cameraClicked = True
        elif buttonCamera1.check_click(pos) == 0 and self.cameraClicked == True:
            self.cameraClicked = False

camera1 = Camera()

monster = Monster("colsonJumpscare.png")
    

BatterijTotaal = 800
BatterijStatus = True
Lc1, Rc1 = 100, 100
Lc2, Rc2 = 100, 100
Lc3, Rc3 = 100, 100
pos = (0,0,0,0)
Lbuttonstatus, RButtonStatus, cameraButtonStatus = 0, 0, 0
Lclicked, Rclicked, cameraClicked = 0, 0, 0
while True:
    pygame.event.pump() # start pygame
    clock.tick(fps) # zet de fps op 60
    toetsen = pygame.key.get_pressed()  # maak een variabele om te kijken of een toets word ingedrukt

    if toetsen[pygame.K_q]: # stop de pygame door q in te drukken of door het kruisje rechts boven aan te klikken in pygame
         break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if LbuttonDoor.check_click(pos) == 1 and Lclicked == False and BatterijStatus == 1:
            Lbuttonstatus = not Lbuttonstatus  # wisselt tussen True en False
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
            
        if RbuttonDoor.check_click(pos) == 1 and Rclicked == False and BatterijStatus == 1:
            RButtonStatus = not RButtonStatus  # wisselt tussen True en False
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

    if BatterijTotaal <= 0:
        BatterijStatus = False
        RButtonStatus = False
        Lbuttonstatus = False
    if (tijd % 60) == 0:
        tijdKlok += 1
        BatterijTotaal -= BatterijVerbruik
    if tijdKlok == 60:
        uur += 1
        tijdKlok = 0
    klok = font.render(str(uur), True, (255,255,255))
    Batterij = font.render(str(BatterijTotaal), True, (255,255,255))
    if uur == 6:
        break 


    frame.fill((0,0,0))
    if cameraButtonStatus == False:
        RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
        LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
        if RButtonStatus == False and Lbuttonstatus == False:
            frame.blit(background_office, (0, 0))
            RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
            LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
        elif RButtonStatus == True and Lbuttonstatus == True:
            frame.blit(office_both_open,(0,0))
            RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
            LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
        elif RButtonStatus:
            frame.blit(office_right_open,(0,0))
            RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
            LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
        elif Lbuttonstatus:
            frame.blit(office_left_open,(0,0))
            RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
            LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
    
    
    else:
        buttonCamera1.draw_button("", 100,100,100)
        buttonCamera2.draw_button("", 100,100,100)
        buttonCamera3.draw_button("", 100,100,100)
        camera1.camera_gebruiken(buttonCamera1, monster)
        camera1.camera_gebruiken(buttonCamera2, monster)   
        camera1.camera_gebruiken(buttonCamera3, monster)
    buttonCamera.draw_button("camera", 100,100,100)
    frame.blit(klok, (0, 1020))
    frame.blit(Batterij, (0, 920)) 

    pygame.display.flip()
    tijd += 1 # doe 1 bij variabele tijd


pygame.quit() # stop pygame als de while loop is gedaan 