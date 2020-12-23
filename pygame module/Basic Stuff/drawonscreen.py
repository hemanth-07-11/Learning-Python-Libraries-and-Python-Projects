import pygame
pygame.init()
win_x = 450
win_y = 450
#window size
win = pygame.display.set_mode((win_x,win_y))
#title
pygame.display.set_caption("Draw on Screen")

run = True
vel = 5
#initial position
x = win_x // 3
y = win_y // 3
width = 20
height = 20
i=1
while(run):
    pygame.time.delay(75)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            #trying to execute mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked mouse " + str(i) + " times")
            i = i+1
    
     # list of keys pressed   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DELETE]:
        # fill window screen with black background colour, same as deleting everything except initial rectangle on window
        win.fill((0,0,0))
    if keys[pygame.K_LEFT]:
        if x<=0 :
            x = win_x
        x = x - vel
        

    if keys[pygame.K_RIGHT]:
        if x>= win_x - vel:
            x= -vel
        x = x + vel

    if keys[pygame.K_UP]:
        if y<=0 :
            y=win_y
        y = y - vel

    if keys[pygame.K_DOWN]:
        if y>=win_y - vel:
            y = -vel
        y = y + vel
    
    # draws the initial rectangle on the window screen 
    pygame.draw.rect(win,(255,0,0) , (x,y,width,height))
    #have to keep updating the display everytime to view changes
    pygame.display.update()
pygame.quit()