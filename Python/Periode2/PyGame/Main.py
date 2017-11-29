from Rect import *
from Colors import *
#starting pygame
pg.init()
screen = pg.display.set_mode([800,600]) #window size
pg.display.set_caption("Pygame") # Name Window
clock = pg.time.Clock() # setting a clock

Rect = Rectangle(200,300,50,50) #creating a Rect

running = True #loop condition
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    screen.fill(Black) #create background color

    Rect.Draw(screen) #call Rect Draw
    Rect.Update(screen) #call Rect Update

    pg.display.update() #update display
    clock.tick(60) # set framerate

quit() #quit the code
