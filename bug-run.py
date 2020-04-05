import pygame


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

def bug(x,y):
    gameDisplay.blit(bugImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

gameExit = False

while not gameExit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
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
    bug(x,y)

    if x > display_width - bug_width or x < 0:
        gameExit = True
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()