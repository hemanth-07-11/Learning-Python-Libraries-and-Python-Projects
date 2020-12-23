import pygame
import sys, random

FPS = 15
PIXEL_SIZE = 20
INITIAL_SNAKE_LENGTH = 3
HORIZONTAL_SIZE = 600
VERTICAL_SIZE = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (25,0,0)
BLUE = (255, 0, 255)
ASH = (70, 75, 71)
GREEN = (0, 255, 0)
RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

def main():
    global DISPLAY_SURF, GAMECLOCK
    pygame.init()
    DISPLAY_SURF = pygame.display.set_mode((HORIZONTAL_SIZE, VERTICAL_SIZE), 0, 32)
    GAMECLOCK = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")
    DISPLAY_SURF.fill(DARKGREY)
    Restart = True
    while Restart:
        RunGame()
        RestartText()
        pygame.time.wait(5000)

def RestartText():
    Font = pygame.font.Font('freesansbold.ttf', 10)
    restart_surf = Font.render("Restarting in 5 seconds", True, GREEN)
    restart_surf_rect = restart_surf.get_rect()
    DISPLAY_SURF.fill(DARKGREY)
    DISPLAY_SURF.blit(restart_surf, restart_surf_rect)
    pygame.display.update()

def RunGame():
    snake_body = []
    dir = RIGHT
    xpos = (HORIZONTAL_SIZE/2 // PIXEL_SIZE)*PIXEL_SIZE
    ypos = (VERTICAL_SIZE/2 //PIXEL_SIZE)*PIXEL_SIZE
    snake_head = (xpos, ypos)
    # create initial snake
    for i in range(INITIAL_SNAKE_LENGTH-1, -1, -1):
        snake_body.append((snake_head[0] - i*PIXEL_SIZE, snake_head[1]))
    # create random insect
    insect_pos = GetRandomInsectPosition(snake_body)
    while True:
        if dir == RIGHT:
            xpos = xpos + PIXEL_SIZE if xpos < HORIZONTAL_SIZE - PIXEL_SIZE else 0
        elif dir == LEFT:
            xpos = xpos - PIXEL_SIZE if xpos >= PIXEL_SIZE else HORIZONTAL_SIZE - PIXEL_SIZE
        elif dir == DOWN:
            ypos = ypos + PIXEL_SIZE if ypos < VERTICAL_SIZE - PIXEL_SIZE else 0
        elif dir == UP:
            ypos = ypos - PIXEL_SIZE if ypos >= PIXEL_SIZE else VERTICAL_SIZE - PIXEL_SIZE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if dir != DOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                    dir = UP
                elif dir != UP and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    dir = DOWN
                elif dir != RIGHT and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    dir = LEFT
                elif dir != LEFT and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    dir = RIGHT
        if (xpos, ypos) in snake_body:
            Bold_Font = pygame.font.Font('freesansbold.ttf', 20)
            GameOver_Surf = Bold_Font.render("Game Over! score: %s" % str(len(snake_body) - INITIAL_SNAKE_LENGTH), True, GREEN)
            GameOver_Surf_Rect = GameOver_Surf.get_rect()
            GameOver_Surf_Rect.topleft = (HORIZONTAL_SIZE/3, VERTICAL_SIZE/2)
            DISPLAY_SURF.blit(GameOver_Surf, GameOver_Surf_Rect)
            pygame.display.update()
            pygame.time.wait(1000)
            return
        snake_head = (xpos, ypos)
        snake_body.append(snake_head)
        if insect_pos == snake_head:
            insect_pos = GetRandomInsectPosition(snake_body)
        else:
            snake_body = snake_body[1:]  # Remove tail
        DISPLAY_SURF.fill(DARKGREY)
        # DrawGrid()
        for body_pix in snake_body:
            pygame.draw.rect(DISPLAY_SURF, GREEN, (body_pix[0], body_pix[1], PIXEL_SIZE, PIXEL_SIZE))
        pygame.draw.rect(DISPLAY_SURF, WHITE, (insect_pos[0], insect_pos[1], PIXEL_SIZE, PIXEL_SIZE))

        normal_font = pygame.font.Font('freesansbold.ttf', 18)
        score_surf = normal_font.render('Score: %s' % (len(snake_body) - INITIAL_SNAKE_LENGTH), True, BLUE)
        score_rect = score_surf.get_rect()
        score_rect.topleft = (HORIZONTAL_SIZE - 100, 10)
        DISPLAY_SURF.blit(score_surf, score_rect)

        pygame.display.update()
        GAMECLOCK.tick(FPS)

def DrawGrid():
    for num in range(0, HORIZONTAL_SIZE + PIXEL_SIZE, PIXEL_SIZE):
        pygame.draw.line(DISPLAY_SURF, ASH, (num, 0), (num, VERTICAL_SIZE))
    for num in range(0, VERTICAL_SIZE + PIXEL_SIZE, PIXEL_SIZE):
        pygame.draw.line(DISPLAY_SURF, ASH, (0, num), (HORIZONTAL_SIZE, num))

def GetRandomInsectPosition(SnakeBody):
    x = random.randrange(0, HORIZONTAL_SIZE, PIXEL_SIZE)
    y = random.randrange(0, VERTICAL_SIZE, PIXEL_SIZE)
    (x, y) = (x, y) if (x, y) not in SnakeBody else GetRandomInsectPosition(SnakeBody)
    return (x,y)

if __name__ == '__main__':
    main()
