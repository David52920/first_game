import abc
from src.objects.gameobject import GameObject
from src.util.util import Position

class Tile(GameObject):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = None

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type
