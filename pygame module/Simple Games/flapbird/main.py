import pygame
import time
import random

from libs.Pipe import Pipe
from libs.Font import Font
from libs.Bird import Bird

def gameStart():
    clock = pygame.time.Clock()
    font = Font(gameDisplay)

    bg = pygame.image.load('src/bg.png')

    bird = Bird(gameDisplay, 'src/1.png',(30,50),(0,0))
    bird.rescale(0.1)

    wall_control = 0
    walls = []
    
    while not bird.dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bird.dead = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        gameDisplay.blit(bg,(0,0))

        bird.speed.y += 0.3
        bird.update_pos()
        bird.render()

        if(wall_control == 100):
            place = random.randint(200,414)
            walls.append(Pipe(gameDisplay, 'src/bp.png',(634,place),(-5,0)))
            walls.append(Pipe(gameDisplay, 'src/tp.png',(634,place-150-423),(-5,0)))
            wall_control = 0
        else:
            wall_control += 1

        for i,wall in enumerate(walls):
            wall.update_pos()
            if (wall.pos.x < 0-wall.w):
                del walls[i]
            wall.render()
            if(wall.is_collided_with(bird)):
                bird.dead = 1

        pygame.display.update()
        clock.tick(60)

    font.write("dead")

pygame.init()

gameDisplay = pygame.display.set_mode((634,476))
pygame.display.set_caption('Flopy Bird')

game_continue = 1

while(game_continue):
    loop = 1
    gameStart()
    game_continue = 0
    now =  pygame.time.get_ticks()
    while (pygame.time.get_ticks() - now < 1000 and loop):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_continue = 1
                    loop = 0
                    break

pygame.quit()
