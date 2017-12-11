from Colors import *
import pygame as pg

class Projectile:
    def __init__(self, x, y): #constructor
        self.Rect = pg.rect.Rect((x, y, 5, 30)) #create rectangle

    def Update(self, screen):
        self.Rect.move_ip(0, -8)

    def Draw(self, screen):
        pg.draw.rect(screen, Red, self.Rect)
