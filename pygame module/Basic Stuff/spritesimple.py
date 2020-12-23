#Import packages
import pygame
import random

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Block(pygame.sprite.Sprite):
    """This class represents a block - Sprite class is parent"""
    def __init__(self, color, width, height):
        super().__init__()        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect() #Where is the sprite?
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, Block.size[0])
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > Block.size[1]:
            self.reset_pos()
            

class Ball(pygame.sprite.Sprite):
    """This class represents a ball - Sprite class is parent"""
    def __init__(self, color, width, height):
        super().__init__()        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height], 0)
        self.rect = self.image.get_rect() #Where is the sprite? 

class Bitmapped_graphic(pygame.sprite.Sprite):
    """This class represents a bitmapped graphic"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image_name").convert()
        self.rect = self.image.get_rect()
        
def main():
    #Window init
    pygame.init()
    size = (1280, 720)
    Block.size = size
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Hello Game")
    pygame.mouse.set_visible(False)
    
    #The following list of sprites is handled by Group
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    for i in range(50):
        block = Block(BLACK, 20, 15)
        block.rect.x = random.randrange(size[0])
        block.rect.y = random.randrange(size[1])
        block_list.add(block)
        all_sprites_list.add(block)
    player = Block(RED, 20, 15)
    all_sprites_list.add(player)
    done = False
    clock = pygame.time.Clock()
    score = 0
    #Game loop
    while not done:
        #Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        #Game logic
        pos = pygame.mouse.get_pos()
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        for block in blocks_hit_list:
            score += 1
            print(score)
        block_list.update()
        #Drawing
        screen.fill(WHITE) #Clear screen
        all_sprites_list.draw(screen)
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps
        
    pygame.quit()

if __name__ == "__main__":
    main()