import pygame,sys,random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)

pygame.display.set_caption("Block Food simple")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

foodCounter = 0
NEWFOOD = 50
FOODSIZE = 5
player = pygame.Rect(100,50,20,20)
foods = []
for i in range(1):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE)
                             ,FOODSIZE,FOODSIZE))

moveLeft = False
moveRight = False
moveUp= False
moveDown = False

MOVESPEED = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = True
                moveUp = False

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0,WINDOWHEIGHT-player.height)
                player.left = random.randint(0,WINDOWWIDTH-player.width)
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE))

    foodCounter +=1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE)
                                 , FOODSIZE, FOODSIZE))

    window.fill(BLACK)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    pygame.draw.rect(window,WHITE,player)
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
    for i in range(1):
        pygame.draw.rect(window,RED,foods[i])
    pygame.display.update()
    mainClock.tick(40)