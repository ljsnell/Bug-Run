import pygame

class Button_Handler:
    black = (0,0,0)
    
    def button(self, gameDisplay, msg, x, y, w, h, ic, ac):
        mouse = pygame.mouse.get_pos()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
    
    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()