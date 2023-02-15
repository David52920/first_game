from src.objects.tile import Tile
from src.util.assetmanager import assetManager


class GrassTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("grass")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class GrassAltTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("grassalt")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class ConcreteTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("concrete")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class ConcreteAltTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("concretealt")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class DirtTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("dirt")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class DirtSandTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("dirstand")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class BrickTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("brick")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class RockTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("rock")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class SnowTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("snow")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

class StoneTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = assetManager.getAsset("stone")
        self.rect.width = self.type.get_width()
        self.rect.height = self.type.get_height()
        self.xOffset = self.rect.width / 2
        self.yOffset = self.rect.height / 2

