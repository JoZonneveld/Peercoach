import pygame as pg
from Rect import *


pg.init()
screen = pg.display.set_mode([800,600])
white = [255, 255, 255]
red = [255, 0, 0]
pg.display.set_caption("My program")

rect = Rectangle(screen, red, 399,150,100,50)
#399,150,100,50

running = True
while running:

    rect.Update()

    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
            quit()
    pg.display.update()
quit()
