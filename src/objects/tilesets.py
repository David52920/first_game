from src.objects.tile import Tile
from src.loader import loader


class GrassTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/grass1.png")

class GrassAltTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/grass2.png")

class ConcreteTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/concrete1.png")

class ConcreteAltTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/concrete2.png")

class DirtTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/dirt.png")

class DirtSandTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/dirtsand.png")

class BrickTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/brick.png")

class RockTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/rock.png")

class SnowTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/snow.png")

class StoneTile(Tile):
    def __init__(self, x = 0 , y = 0):
        super().__init__(x, y)
        self.type = loader.loadImage("res/tiles/stone.png")

