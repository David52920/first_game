from src.objects.tile import Tile
from src.util.assetmanager import assetManager
from src.util.util import Position


class GrassTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("grass")

class GrassAltTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("grassalt")

class ConcreteTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("concrete")

class ConcreteAltTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("concretealt")

class DirtTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("dirt")

class DirtSandTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("dirstand")

class BrickTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("brick")

class RockTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("rock")

class SnowTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("snow")

class StoneTile(Tile):
    def __init__(self, position=Position()):
        super().__init__(position)
        self.type = assetManager.getAsset("stone")

