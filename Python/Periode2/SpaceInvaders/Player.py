from Colors import *
from Projectile import *
from Vector import *

class Player:
    def __init__(self, vec, color):
        self.Vec = vec
        self.Color = color
        self.Rect = pg.rect.Rect((vec.X, vec.Y, 50, 50))
        self.Projectiles = list()
        self.Counter = 0
        self.Dead = False

    #Region Methods
    def CreateProjectile(self, Enemys):
        x, y = self.Rect.midtop
        self.Projectiles.append(Projectile(Vector(x,y), "Player", Enemys))

    def Keyhandelers(self, screen, Enemys):
        x, y = screen.get_size()
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            if self.Rect.left - 10 >= 0:
                self.Rect.move_ip(-5, 0)
        if key[pg.K_RIGHT]:
            if self.Rect.right + 10 <= x:
                self.Rect.move_ip(5, 0)

        self.Counter -= 1

        if key[pg.K_SPACE]:
            if self.Counter <= 0:
                self.CreateProjectile(Enemys)
                self.Counter = 45;
    #End region Methods

    # -----------------------------------------------------------------------------------------------------------

    #Region Update & Draw
    def Update(self, screen, Enemys):

        self.Keyhandelers(screen, Enemys)

        for Projectile in self.Projectiles:
            Projectile.Update(screen)
            Projectile.Draw(screen)

            if Projectile.Rect.y < 0:
                self.Projectiles.remove(Projectile)

    def Draw(self, screen):
        pg.draw.rect(screen, self.Color, self.Rect)
    #End Region Update & Draw