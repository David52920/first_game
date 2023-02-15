import abc
from src.objects.gameobject import GameObject

class Tile(GameObject):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.type = None

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type
