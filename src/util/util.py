import math

class Position:
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y

    def setX(self, x):
        self.X = x

    def setY(self, u):
        self.Y = y

    def equals(self, pos2):
        if not isinstance(pos2, Position): return
        return self.X == pos2.X and self.Y == pos2.Y

    def distanceTo(self, pos2):
        if not isinstance(pos2, Position): return
        d1 = pos2.X - self.X
        d2 = pos2.Y - self.Y
        return math.sqrt(d1^2 + d2^2)






