from pygame import *
import pygame as pg
import random as ran
#define some Colors
Black=[0,0,0]
orange=[255, 140, 0]
pink=[255, 0, 170]

# Start up
pg.init()

# open up display screen
Size=[1000,700]
gameScreen=pg.display.set_mode(Size)

#name of window
pg.display.set_caption("Bouncing Hexagon")

#starting point of Hexagon
HCX=50 #hex corner in x axis
HCY=50 #hex corner in y axis
movingSpeedX=10
movingSpeedY=10
#Hex Color Intialized to orange
hexColor=[255, 140, 0]
#Random Color Generator Function for each bounce
def RandomColor():
    Red= ran.randint(0,255)
    Green=ran.randint(0,255)
    Blue=ran.randint(0,255)
    return [Red,Green,Blue]
done=False
Refresher=pg.time.Clock()

#main loop
while done==False:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=True

    #bounds checking in the horizontal
    if (HCX+75)>1000:
        movingSpeedX=movingSpeedX*-1
        hexColor=RandomColor()
    if (HCX-25)<0:
        movingSpeedX=movingSpeedX*-1
        hexColor=RandomColor()
    HCX+=movingSpeedX
    #bounds checking in the vertical
    if (HCY+100)>700:
        movingSpeedY=movingSpeedY*-1
        hexColor=RandomColor()
    if (HCY)<0:
        movingSpeedY=movingSpeedY*-1
        hexColor=RandomColor()
    HCY+=movingSpeedY


    gameScreen.fill(Black)


    #hexagonPoints=[]
    pg.draw.polygon(gameScreen, hexColor ,[[HCX,HCY],[(HCX+50),HCY],[(HCX+75),(HCY+50)],[(HCX+50),(HCY+100)],[HCX,(HCY+100)],[(HCX-25),(HCY+50)]])           

    pg.display.flip()

# FPS (Frames per Second)
    Refresher.tick(20)

pg.quit()