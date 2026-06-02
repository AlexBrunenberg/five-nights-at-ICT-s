import pygame

pygame.init() #Initieert pygame

BREEDTE = 1920 #Geeft de breedte en hoogte aan
HOOGTE = 1080

frame = pygame.display.set_mode((BREEDTE, HOOGTE)) #maakt de frame het gegeven breedte en hoogte

clock = pygame.time.Clock() #Klok start, tijd begint te lopen
fps = 60
tijd = 0
tijdKlok = 0
uur = 0
Schermstatus = False
font = pygame.font.SysFont("Arial", 60) #Font en lettergrootte
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
    
LbuttonDoor = Button(300, 500, 120,120,(0,255,0))
buttonCamera = Button(900, 960, 120, 120,(255,255,255))
RbuttonDoor = Button(1600, 500, 120,120,(0,255,0))
class Camera:
    def __init__(self,x,y,width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    
        
BatterijVerbruik = 1
BatterijTotaal = 800
Lc1, Rc1 = 100, 100
Lc2, Rc2 = 100, 100
Lc3, Rc3 = 100, 100
pos = (0,0,0,0)
Lbuttonstatus, Rbuttonstatus = 0, 0
Lclicked, Rclicked = 0,0
while True:
    pygame.event.pump() # start pygame
    clock.tick(fps) # zet de fps op 60
    toetsen = pygame.key.get_pressed()  # maak een variabele om te kijken of een toets word ingedrukt

    if toetsen[pygame.K_q]: # stop de pygame door q in te drukken of door het kruisje rechts boven aan te klikken in pygame
         break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if LbuttonDoor.check_click(pos) == 1 and Lclicked == False:
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


            
        if RbuttonDoor.check_click(pos) == 1 and Rclicked == False:
            Rbuttonstatus = not Rbuttonstatus  # wisselt tussen True en False
            if Rbuttonstatus == True:
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


    if (tijd % 60) == 0:
        tijdKlok += 1
    if tijdKlok == 60:
        uur += 1
        tijdKlok = 0
    klok = font.render(str(uur), True, (255,255,255))
    if uur == 6:
        break 

    print(BatterijVerbruik)

    frame.fill((0,0,0))
    RbuttonDoor.draw_button("door", Rc1,Rc2,Rc3)
    LbuttonDoor.draw_button("door", Lc1,Lc2,Lc3)
    frame.blit(klok, (0, 1020))

    pygame.display.flip()
    tijd += 1 # doe 1 bij variabele tijd


pygame.quit() # stop pygame als de while loop is gedaan 