import pygame,sys
from pygame import *

pygame.init()

window = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Hello world")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,200,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

bfont = pygame.font.SysFont(None,48)

text = bfont.render('Hello world',True,WHITE,BLUE)
textRect = text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = window.get_rect().centery

window.fill(WHITE)

pygame.draw.polygon(window,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))

pygame.draw.line(window,BLUE,(60,60),(120,60),4)
pygame.draw.line(window,BLUE,(120,60),(60,120))
pygame.draw.line(window,BLUE,(60,120),(120,120),4)

pygame.draw.circle(window,BLUE,(300,50),20,0)

pygame.draw.ellipse(window,RED,(300,250,40,80),1)

pygame.draw.rect(window,RED,(textRect.left-20,textRect.top-20,textRect.width+40,textRect.height+40))

pixArray = pygame.PixelArray(window)
pixArray[480][380] = BLACK
del pixArray

window.blit(text,textRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()