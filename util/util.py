import math

def flipArray(arry):
    for index in range(math.floor(len(arry) / 2)):
        temp = arry[index]
        arry[index] = arry[len(arry) - index - 1]
        arry[len(arry) - index - 1] = temp
    return arry

def inverseArray(arry):
    m = len(arry)
    n = len(arry[0])
    inversedArray = [[0] * m for _ in range(n)]
    for i in range (n):
        for j in range(m):
            inversedArray[i][j] = arry[j][i]
    return inversedArray

class Position:
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def setX(self, x):
        self.X = x

    def setY(self, y):
        self.Y = y

    def setZ(self, z):
        self.Z = z

    def equals(self, pos2):
        if not isinstance(pos2, Position): return
        return self.X == pos2.X and self.Y == pos2.Y and self.Z == pos2.Z

    def distanceTo(self, pos2):
        if not isinstance(pos2, Position): return
        d1 = pos2.X - self.X
        d2 = pos2.Y - self.Y
        d3 = pos2.Z - self.Z
        return math.sqrt(d1^2 + d2^2)






