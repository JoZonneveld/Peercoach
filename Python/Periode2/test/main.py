from Player import *
from Obs import *
from Game import *

player = Player("Name", 100000)
#
# print(player.HitPoints)

obstakel = Obs("Bol", "Geel&rood", 10, 10, Vector(100, 10))

# a = True
# while(a):
#     print (obstakel.Vec.X)
#     obstakel.Move()
#
#     if obstakel.Vec.X <= 0:
#         a = False

game = Game(player, obstakel)

game.Obs.Vec.X

