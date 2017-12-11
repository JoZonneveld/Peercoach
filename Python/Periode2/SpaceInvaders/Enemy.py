import pygame as pg
from Colors import *
from Vector import *
import random

class Enemy:
    def __init__(self, vec, color):
        self.Vec = vec
        self.Color = color
        self.Rect = pg.rect.Rect((vec.X, vec.Y, 50, 50))
        self.Projectiles = list()
        self.Counter = 0
        self.Moving = False

    def CreateProjectile(self):
        x, y = self.Rect.midtop
        self.Projectiles.append(Projectile(x, y))

    def Move(self, screen):
        x, y = screen.get_size()
        if self.Moving == True:
            self.Rect.move_ip(-5, 0)
            if self.Rect.left - 10 <= 0:
                self.Rect.move_ip(0, 75)
                self.Moving = False
        elif self.Moving == False:
            self.Rect.move_ip(5, 0)
            if self.Rect.right + 10 >= x:
                self.Rect.move_ip(0, 75)
                self.Moving = True


    def Update(self, screen):
        x, y = screen.get_size()
        self.Move(screen)
        #     self.Rect.move_ip(-5, 0)
        # if self.Rect.right + 10 <= x:
        #     self.Rect.move_ip(5, 0)

        self.Counter -= 1



        for Projectile in self.Projectiles:
            Projectile.Update(screen)
            Projectile.Draw(screen)
    def Draw(self, screen):
        pg.draw.rect(screen, self.Color, self.Rect)
