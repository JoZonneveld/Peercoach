import pygame
import Game
import Vector


class Player:

    def __init__(self):
        self.width = 250
        self.height = 50
        self.vec = Vector.Vector(1280 / 2 - self.width / 2, 650)

    def move_left(self):
        self.vec.x -= 10

    def move_right(self):
        self.vec.x += 10

    def update(self):
        pass

    def draw(self, screen):
        s = pygame.Surface((int(self.width), int(self.height)))
        s.set_alpha(255)
        s.fill((0, 0, 0))
        screen.blit(s, (self.vec.x, self.vec.y))
