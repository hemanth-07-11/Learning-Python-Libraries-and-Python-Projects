import pygame
from .vector import vector

class Bird():
    def __init__(self, Display, path, pos, speed):
        self.Display = Display
        self.img = pygame.image.load(path)
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.rect = self.img.get_rect()
        self.pos = vector(pos)
        self.rect.move_ip(self.pos.x,self.pos.y)
        self.speed = vector(speed)
        self.dead = 0
        self.boost = 0

    def render(self):
        self.Display.blit(self.img,(self.pos.x,self.pos.y))

    def rescale(self,proportion):
        self.img = pygame.transform.scale(self.img, (int(self.w*proportion),
                                    int(self.h*proportion)))
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.rect = self.img.get_rect()
        self.rect.move_ip(self.pos.x,self.pos.y)
    
    def update_pos(self):
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y 

        if(self.pos.y + self.h >= 476):
            self.pos.y = 476-self.h
            self.dead = 1
        if(self.pos.y < 0):
            self.speed.y = 0
            self.pos.y = 1

    def jump(self):
        self.speed.y = -7