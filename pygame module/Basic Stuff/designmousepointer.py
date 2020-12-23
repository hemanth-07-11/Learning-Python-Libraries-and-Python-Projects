#Import packages
import pygame

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_stick_figure(screen, x, y):
    #Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    #Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    #Body
    pygame.draw.line(screen, BLUE, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    #Arms
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [1 + x, 17 + y], 2)       

def main(): 
    #Window init
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Hello Game")
    
    done = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    #Game loop
    while not done:
        #Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        #Game logic
        pos = pygame.mouse.get_pos()
        #Drawing
        screen.fill(WHITE) #Clear screen
        draw_stick_figure(screen, pos[0], pos[1])
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps
        
    pygame.quit()

if __name__ == "__main__":
    main()