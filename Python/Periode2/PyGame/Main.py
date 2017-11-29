from Rect import *
from Colors import *
#starting pygame
pg.init()
screen = pg.display.set_mode([800,600]) #window size
pg.display.set_caption("Naam") # Name Window
clock = pg.time.Clock() # setting a clock


#CREATE GAME OBJECTS
Rect = Rectangle(200,300,50,50) #creating a Rect
#END CREATE GAME OBJECTS

#CREATE LIST
Objects = list()
#ADD GAME OBJECTS TO LIST
Objects.append(Rect)
#END CREATE LIST

running = True #loop condition
while running:
    screen.fill(White) #create background color

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    for Object in Objects:
        Object.Update(screen)
        Object.Draw(screen)

    pg.display.update() #update display
    clock.tick(60) # set framerate

quit() #quit the code
