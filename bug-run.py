import time
import random
import pygame
import LvlReader

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bug Run')

black = (0,0,0)
white = (255,255,255)
bug_width = 44

clock = pygame.time.Clock()
crashed = False
bugImg = pygame.image.load('Bug1.png')
bugImg = pygame.transform.scale(bugImg, (44, 44))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def bug(x,y):
    gameDisplay.blit(bugImg, (x,y))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    levels = LvlReader.LevelReader().readInLevel('level1')

    # Need to set the values outside the loop, maybe pop out of the loop every object?    
    thing_startx = levels[0]['x']
    thing_starty = levels[0]['y']
    thing_width = levels[0]['w']
    thing_height = levels[0]['h']
    thing_speed = levels[0]['s']

    thingCount = 1
    dodged = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0        
        x += x_change

        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        bug(x,y)
        things_dodged(dodged)

        if x > display_width - bug_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+bug_width > thing_startx and x + bug_width < thing_startx+thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()