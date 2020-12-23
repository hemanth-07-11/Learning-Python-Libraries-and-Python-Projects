import pygame, sys, os
from pygame.locals import *        #load constants

red = (255, 0, 0)

#initialize pygame
pygame.init()

#set up window
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Display the position of mouse pointer')

#Set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption('Mouse moving detect')
pygame.display.flip()

while True:
    #main game loop
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()