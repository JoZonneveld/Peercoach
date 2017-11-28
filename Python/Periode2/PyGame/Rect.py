import pygame as pg
class Rectangle:
    def __init__(self, screen, color, x, y, w, h):
        self.Screen = screen
        self.Color = color
        self.X = x
        self.Y = y
        self.W = w
        self.H = h

    def Update(self):
        for i in pg.event.get():
            if i.type == pg.QUIT:
                running = False
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    self.X -= 1
                if i.key == pg.K_RIGHT:
                    self.X += 1
        pg.draw.rect(self.Screen, self.Color, (self.X, self.Y, 300, 300))
