from src.objects.gameobject import GameObject

class Tile(GameObject):
    def __init__(self, x, y, width=0, height=0):
        super().__init__(x, y, width, height)
        self.type = None

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type
