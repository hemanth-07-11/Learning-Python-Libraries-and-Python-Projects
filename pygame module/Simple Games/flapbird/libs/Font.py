import pygame

class Font():
    def __init__(self, Display):
        pygame.font.init()
        self.Display = Display
        self.font = pygame.font.SysFont('firamono.ttf', 70)

    def write(self, text):
        text = self.font.render(text, False, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (315,240)
        self.Display.blit(text,textRect)
        pygame.display.update()