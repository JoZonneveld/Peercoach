from Colors import *
from Vector import *
import pygame as pg

class Projectile:
    def __init__(self, vec, kind, hitters): #constructor
        self.Kind = kind
        self.Hitters = hitters
        self.Hit = False
        self.Rect = pg.rect.Rect((vec.X, vec.Y, 5, 30)) #create rectangle

    def CheckCollision(self):
        if self.Kind == "Player":
            for Hitter in self.Hitters:
                if self.Rect.midtop[1] <= Hitter.Rect.bottom and self.Rect.midtop[1] >= Hitter.Rect.top:
                    if self.Rect.midtop[0] >= Hitter.Rect.bottomleft[0] and self.Rect.midtop[0] <= Hitter.Rect.bottomright[0]:
                        Hitter.Dead = True
                        self.Hit = True


    def Update(self, screen):
        #print(self.Rect.bottom)
        if self.Kind == "Player":
            self.Rect.move_ip(0, -8)
        else:
            self.Rect.move_ip(0, 8)

        self.CheckCollision()



    def Draw(self, screen):
        pg.draw.rect(screen, Red, self.Rect)
