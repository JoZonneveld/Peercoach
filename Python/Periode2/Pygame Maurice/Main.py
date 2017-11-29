import pygame
import Game


class Engine:
    def __init__(self):
        pygame.init()
        dimension = (1280, 720)

        Game.screen = pygame.display.set_mode(dimension, 0)
        pygame.display.set_caption("HELLO WORLD")

    def update_keys(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_F4]:
                self.running = False

        if keys[pygame.K_LEFT]:
            Game.player.move_left()
        if keys[pygame.K_RIGHT]:
            Game.player.move_right()

    def update(self):
        Game.player.update()
        Game.ball.update()

    def draw(self):
        Game.screen.fill((255, 255, 255))
        Game.player.draw(Game.screen)
        Game.ball.draw(Game.screen)

        pygame.display.update()

    def loop(self):
        while Game.running:
            self.update_keys()
            self.update()
            self.draw()
            pygame.time.Clock().tick(60)

game = Engine()
game.loop()
# pygame.quit()
