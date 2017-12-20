import pygame as pg
from Colors import *
from Vector import *
from Projectile import *
from random import randint

class Enemy:
    def __init__(self, vec, color):
        self.Vec = vec
        self.Color = color
        self.Rect = pg.rect.Rect((vec.X, vec.Y, 50, 50))
        self.Projectiles = list()
        self.Counter = 0
        self.Moving = False
        self.Dead = False

    # Region Methods
    def CreateProjectile(self, Player):
        x, y = self.Rect.midtop
        self.Projectiles.append(Projectile(Vector(x, y), "Enemy", Player))

    def Move(self, screen, Player):
        x, y = screen.get_size()
        if self.Moving == True:
            self.Rect.move_ip(-3, 0)
            if self.Rect.left - 10 <= 0:
                self.Rect.move_ip(0, 75)
                self.Moving = False
        elif self.Moving == False:
            self.Rect.move_ip(3, 0)
            if self.Rect.right + 10 >= x:
                self.Rect.move_ip(0, 75)
                self.Moving = True
        self.Counter -= 1
        if randint(0,15) == 3 and self.Counter <= 0:
            self.CreateProjectile(Player)
            self.Counter = 60
    # End region Methods

    # -----------------------------------------------------------------------------------------------------------

    # Region Update & Draw
    def Update(self, screen, Player):
        print(self.Rect.top)
        x, y = screen.get_size()
        self.Move(screen, Player)

        for Projectile in self.Projectiles:
            Projectile.Update(screen)
            Projectile.Draw(screen)

            if Projectile.Rect.y > y:
                self.Projectiles.remove(Projectile)
    def Draw(self, screen):
        pg.draw.rect(screen, self.Color, self.Rect)

    # End Region Update & Draw
