import pygame as pg
from Colors import *
class Rectangle:
    def __init__(self, x, y, w, h): #constructor
        self.Rect = pg.rect.Rect((x, y, w, h)) #create rectangle

    def Update(self, screen):
        # print(x, y)
        x, y = screen.get_size()
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            if self.Rect.left - 10 >= 0:
                self.Rect.move_ip(-5, 0)
        if key[pg.K_RIGHT]:
            if self.Rect.right + 10 <= x:
                self.Rect.move_ip(5, 0)
        if key[pg.K_UP]:
            if self.Rect.top - 10 >= 0:
                self.Rect.move_ip(0, -5)
        if key[pg.K_DOWN]:
            self.Rect.move_ip(0, 5)

    def Draw(self, screen):
        pg.draw.rect(screen, Blue, self.Rect)
