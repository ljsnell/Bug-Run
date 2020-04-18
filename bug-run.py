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
red = (255,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

bug_width = 44

clock = pygame.time.Clock()
crashed = False
bugImg = pygame.image.load('Bug1.png')
bugImg = pygame.transform.scale(bugImg, (44, 44))

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Bug Run", largeText)        
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        #pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        #pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        
        mouse = pygame.mouse.get_pos()

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,450,100,50))
        pygame.draw.rect(gameDisplay, red, (550,450,100,50))

        # Go button text
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ((150+(100/2)), (450+(50/2)))
        gameDisplay.blit(textSurf, textRect)

        # Quit button text
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("QUIT", smallText)
        textRect.center = ((550+(100/2)), (450+(50/2)))
        gameDisplay.blit(textSurf, textRect)


        pygame.display.update()
        clock.tick(15)

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
    
    for block in levels:
        print(block['id'])
        nextBlock = False
        while not nextBlock:
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
                things(block['x'], thing_starty, block['w'], block['h'], black)
                thing_starty += block['s']
                bug(x,y)
                things_dodged(dodged)
    
                if x > display_width - bug_width or x < 0:
                    crash()
    
                if thing_starty > display_height:
                    thing_starty = 0 - thing_height                    
                    dodged += 1
                    nextBlock = True
    
                if y < thing_starty+thing_height:
                    if x > block['x'] and x < block['x'] + block['w'] or x+bug_width > block['x'] and x + bug_width < block['x']+block['w']:
                        crash()
    
                pygame.display.update()
                clock.tick(60)
# https://pythonprogramming.net/placing-text-pygame-buttons/?completed=/making-interactive-pygame-buttons/
game_intro()
game_loop()
pygame.quit()
quit()