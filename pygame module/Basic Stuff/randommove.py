import pygame,sys,time
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation')

DOWNLEFT = 1
DOWNRIGHT = 2
UPLEFT = 3
UPRIGHT = 4

MOVESPEED = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 120, 255)
RANDOMM= (120,200,220)
GREEN = (0, 255, 0)


b1 = {'rect':pygame.Rect(300,80,50,100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200,200,20,20), 'color':GREEN, 'dir':UPRIGHT}
b3 = {'rect':pygame.Rect(100,150,60,60), 'color':BLUE, 'dir':UPLEFT}
b4 = {'rect':pygame.Rect(0,0,60,60), 'color':RANDOMM, 'dir':UPRIGHT}
blocks = [b1, b2, b3, b4]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #window.fill(BLACK)
    for b in blocks:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED


        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNLEFT

        if b['rect'].bottom > WINDOWHEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT

        if b['rect'].left < 0:
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT

        if b['rect'].right > WINDOWWIDTH:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT


        pygame.draw.rect(window,b['color'],b['rect'])

    pygame.display.update()
    time.sleep(0.02)