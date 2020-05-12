import pygame
import time
import button_handler

class Drawing_Handler():
    button_creator = button_handler.Button_Handler()    
    bugImg = pygame.image.load('Bug1.png')
    bugImg = pygame.transform.scale(bugImg, (44, 44))

    def bug(self, gameDisplay, x, y):
        gameDisplay.blit(self.bugImg, (x,y))

    def text_display(self, text, gameDisplay, display_width, display_height):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = button_creator.text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
    
    def things(self, gameDisplay, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
