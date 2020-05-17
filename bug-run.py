import random
import pygame
import button_handler
from level_utils import lvl_reader
from level_utils import level_selector
from level_utils import quit_game
from drawing import dodge_counter
from drawing import drawing_handler
from objects import bug

dodge_handler = dodge_counter.Dodge_Handler()
level_selector = level_selector.Level_Selector()
button_creator = button_handler.Button_Handler()
drawing_creator = drawing_handler.Drawing_Handler()
quitter = quit_game.Quit()
player_bug = bug.Bug()

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bug Run')

black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
bright_green = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)
yellow = (230, 230, 0)
bright_yellow = (255, 255, 0)

bug_width = 44

pause = False

clock = pygame.time.Clock()

levelPassed = False
level_to_play = 'level1.json'
level_counter = 0

largeText = pygame.font.SysFont("comicsansms",115)

def game_intro():
    global levelPassed
    intro = True    
    while intro:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if levelPassed == False:
                        game_loop()
                    else:
                        nextLevel()

        gameDisplay.fill(white)        
        TextSurf, TextRect = button_creator.text_objects("Bug Run", largeText)        
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        if levelPassed == False:
            button_creator.button(gameDisplay, "GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        else:
            button_creator.button(gameDisplay, "Next Level!", 150, 450, 125, 50, green, bright_green, nextLevel)

        button_creator.button(gameDisplay, "QUIT", 550, 450, 100, 50, red, bright_red, quitter.quitgame)
        button_creator.button(gameDisplay, "Select Level", 0, 0, 150, 50, yellow, bright_yellow, pickLvl)

        pygame.display.update()
        clock.tick(15)

def nextLevel():
    global level_to_play
    global level_counter
    level_counter = level_counter + 1
    levels = ['level1.json', 'level2.json', 'level3.json']
    try:
        level_to_play = levels[level_counter]
    except:
        level_counter = 0
        level_to_play = levels[level_counter]
    game_loop()

def pickLvl():
    global level_to_play
    level_to_play = level_selector.lvlSelector()

def paused():    
    TextSurf, TextRect = button_creator.text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button_creator.button(gameDisplay, "Continue",150,450,100,50,green,bright_green,unpause)
        button_creator.button(gameDisplay, "QUIT", 550, 450, 100, 50, red, bright_red, quitter.quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pause = False

def crash():    
    global levelPassed
    TextSurf, TextRect = button_creator.text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    levelPassed = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if levelPassed == False:
                        game_loop()
                    else:
                        nextLevel()
        if levelPassed == False:
            button_creator.button(gameDisplay, "Play Again",150,450,150,50,green,bright_green,game_loop)
        else:
            button_creator.button(gameDisplay, "Next Level",150,450,150,50,green,bright_green,nextLevel)
        button_creator.button(gameDisplay, "Quit",550,450,100,50,red,bright_red, quitter.quitgame)

        pygame.display.update()
        clock.tick(15)
    levelPassed = False

def game_loop():
    global pause
    global levelPassed
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    crashed = False
    levels = lvl_reader.LevelReader().readInLevel(level_to_play)

    thing_starty = -600

    thingCount = 1
    dodged = 0
    # Add msg at start of level
    drawing_creator.lvlTitle(gameDisplay, white, levels, display_width, display_height, largeText)

    for block_list in levels['block_list']:
        nextBlock = False
        while not nextBlock:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        if event.key == pygame.K_RIGHT:
                            x_change = 5
                        if event.key == pygame.K_p:
                            pause = True
                            paused()
    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x_change = 0        
                x += x_change
    
                gameDisplay.fill(white)
                drawing_creator.things(gameDisplay, thing_starty, block_list)
                thing_starty += block_list[0]['s']
                drawing_creator.bug(gameDisplay, x,y, player_bug.vulnerable)
                dodge_handler.things_dodged(gameDisplay, dodged)
    
                if x > display_width - bug_width or x < 0:
                    crash()
    
                if thing_starty > display_height:
                    thing_starty = 0 - block_list[0]['h']
                    dodged += 1
                    nextBlock = True
                    if crashed == True:
                        player_bug.vulnerable = True
    
                if y < thing_starty+block_list[0]['h']:
                    for block in block_list:                        
                        crashed = False
                        if x > block['x'] and x < block['x'] + block['w']\
                            or x+bug_width > block['x'] and x + bug_width < block['x']+block['w']:
                            if block['id'] == 1:
                                if player_bug.vulnerable == True:
                                    crash()
                                else:
                                    crashed = True

                            if block['id'] == 2:
                                player_bug.vulnerable = False                   
                        
                pygame.display.update()
                clock.tick(60)
    
    levelPassed = True

game_intro()
game_loop()
pygame.quit()
quit()