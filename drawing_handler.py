import pygame
import time
import button_handler

class Drawing_Handler():
    button_creator = button_handler.Button_Handler()    
    bugImg1 = pygame.image.load('Bug1.png')
    bugImg1 = pygame.transform.scale(bugImg1, (44, 44))
    bugImg2 = pygame.image.load('Bug2.png')
    bugImg2 = pygame.transform.scale(bugImg2, (44, 44))
    bugImg3 = pygame.image.load('Bug3.png')
    bugImg3 = pygame.transform.scale(bugImg3, (44, 44))
    animation_loop = 0

    def bug(self, gameDisplay, x, y):
        if self.animation_loop < 5:
            gameDisplay.blit(self.bugImg1, (x,y))
        elif self.animation_loop < 10:
            gameDisplay.blit(self.bugImg2, (x,y))
        else:
            gameDisplay.blit(self.bugImg3, (x,y))
        self.animation_loop = self.animation_loop + 1
        if self.animation_loop > 15:
            self.animation_loop = 0

    def text_display(self, text, gameDisplay, display_width, display_height):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = button_creator.text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
    
    def things(self, gameDisplay, thing_starty, block_list):
        for block in block_list:
            pygame.draw.rect(gameDisplay, tuple(block['color']), [block['x'], thing_starty, block['w'], block['h']])
