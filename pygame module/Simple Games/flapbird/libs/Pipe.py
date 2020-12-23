import pygame
from .vector import vector

class Pipe():
    def __init__(self, Display, path, pos, speed):
        self.img = pygame.image.load(path)
        self.w = self.img.get_width()
        self.rect = self.img.get_rect()
        self.pos = vector(pos)
        self.rect.move_ip(self.pos.x,self.pos.y)
        self.speed = vector(speed)
        self.Display = Display

    def render(self):
        self.Display.blit(self.img,(self.pos.x,self.pos.y))
    
    def update_pos(self):
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.rect.move_ip(self.speed.x,self.speed.y)

    def is_collided_with(self,target):
        return self.rect.colliderect(target.rect)