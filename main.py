import pygame, sys
from settings import*
from level import Level
pygame.init()
#from player import*
keys = pygame.key.get_pressed()

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("First")
clock=pygame.time.Clock()

level=Level()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    level.run()
    #if keys[pygame.K_RIGHT]:
       # image1 ='img_3.png'
    #if keys[pygame.K_LEFT]:
      #  image1='img.png'

    pygame.display.update()
    clock.tick(60)

