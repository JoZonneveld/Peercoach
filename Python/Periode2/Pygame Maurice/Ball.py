import pygame
import Vector
import Game

class Ball:
    def __init__(self):
        self.radius = 50
        self.vec = Vector.Vector(1280 / 2 - self.radius / 2, 100)

        self.gravity = 0.5

        self.y_speed = 0
        self.y_max_speed = 20

        self.x_speed = 5

    def update(self):
        # self.y += 1
        # self.y += self.y_speed

        self.vec.x += self.x_speed

        self.y_speed += self.gravity
        if self.y_speed > self.y_max_speed:
            self.y_speed = self.y_max_speed
        self.vec.y += self.y_speed

        if self.vec.y + self.radius > Game.player.vec.y:
            if Game.player.vec.x <= self.vec.x <= Game.player.vec.x + Game.player.width:
                self.y_speed = -self.y_speed
                self.vec.y += self.y_speed

        if self.vec.x + self.radius > 1280 or self.vec.x < self.radius:
            self.x_speed = -self.x_speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.vec.x), int(self.vec.y)), int(self.radius), 0)
