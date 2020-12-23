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
    x_speed = 0
    y_speed = 0
    x_pos = 10
    y_pos = 10
    #Game loop
    while not done:
        #Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        #Game logic
        x_pos += x_speed
        y_pos += y_speed
        if x_pos > 690:
            x_pos = 0
        elif x_pos < 0:
            x_pos = 690
        if y_pos > 490:
            y_pos = 0
        elif y_pos < 0:
            y_pos = 490
        #Drawing
        screen.fill(WHITE) #Clear screen
        draw_stick_figure(screen, x_pos, y_pos)
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps
        
    pygame.quit()

if __name__ == "__main__":
    main()