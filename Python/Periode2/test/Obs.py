class Vector:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Obs:
    def __init__(self, vorm, color, heigth, width, vec):
        self.Vorm = vorm
        self.Color = color
        self.Heigth = heigth
        self.Width = width
        self.Vec = vec

    def Move(self):
        self.Vec.X -= 1