from Player import *
from Vector import *
from Projectile import *
from Colors import *
from Enemy import *
#starting pygame
pg.init()
screen = pg.display.set_mode([800,600]) #window size
pg.display.set_caption("Naam") # Name Window
clock = pg.time.Clock() # setting a clock


#CREATE GAME OBJECTS
# Rect = Rectangle(200,300,50,50) #creating a Rect
Player = Player(Vector(375, 525), Green)
Enemy0 = Enemy(Vector(50, 50), Blue)
Enemy1 = Enemy(Vector(125, 50), Blue)
#END CREATE GAME OBJECTS

#CREATE LIST
Enemys = list()
#ADD GAME OBJECTS TO LIST
Enemys.append(Enemy0)
Enemys.append(Enemy1)
#END CREATE LIST

running = True #loop condition
while running:
    screen.fill(White) #create background color

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    Player.Update(screen, Enemys)
    Player.Draw(screen)

    for Enemy in Enemys:
        Enemy.Update(screen, Player)
        Enemy.Draw(screen)

        if Enemy.Dead == True:
            Enemys.remove(Enemy)

    pg.display.update() #update display
    clock.tick(60) # set framerate

quit() #quit the code
