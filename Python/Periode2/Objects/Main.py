class Game:
    def __init__(self, player, obs):
        self.Player = player
        self.Obs = obs

class Player:
    def __init__(self, name, hp, vec):
        self.Name = name
        self.HP = hp
        self.Vec = vec

    def Move(self):
        self.Vec.X -= 15

class Obstakel:
    def __init__(self, color, rect):
        self.Color = color
        self.Rect = rect

class Rect:
    def __init__(self, x, y, w, h):
        self.X = x
        self.Y = y
        self.W = w
        self.H = h

class Vector:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def function():
    print("func")

function()
# player = Player("Karel", 1000, Vector(115, 100))
#
# obs = Obstakel("blauw", Rect(10, 15, 100, 50))
#
# game = Game(player, obs)
#
# print(game.Player.Vec.X)
# game.Player.Move()
# print(game.Player.Vec.X)

