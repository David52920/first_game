import abc

class Tile(abc.ABC):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.type = None

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type
