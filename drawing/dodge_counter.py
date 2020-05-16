import pygame

black = (0,0,0)
class Dodge_Handler():

    def things_dodged(self, gameDisplay, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, black)
        gameDisplay.blit(text,(0,0))
