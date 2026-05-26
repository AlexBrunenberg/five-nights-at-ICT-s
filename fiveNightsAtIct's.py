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

while True:
    pygame.event.pump() # start pygame
    clock.tick(fps) # zet de fps op 60
    toetsen = pygame.key.get_pressed()  # maak een variabele om te kijken of een toets word ingedrukt

    if (tijd % 60) == 0:
        tijdKlok += 1
    if tijdKlok == 60:
        uur += 1
        tijdKlok = 0
    klok = font.render(tijdKlok)


    if toetsen[pygame.K_q]: # stop de pygame door q in te drukken of door het kruisje rechts boven aan te klikken in pygame
         break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    
    frame.fill((0,0,0))

    pygame.display.flip()
    tijd += 1 # doe 1 bij variabele tijd


pygame.quit() # stop pygame als de while loop is gedaan 