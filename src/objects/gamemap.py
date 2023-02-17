from objects.tilesets import *

import pygame, math

class GameMap:
    TILE_WIDTH = 64
    TILE_HEIGHT = 32
    TILE_WIDTH_HALF = TILE_WIDTH / 2
    TILE_HEIGHT_HALF = TILE_HEIGHT / 2
    MAP_WIDTH = 30
    MAP_HEIGHT = 30

    def __init__(self, game, camera):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.gameWidth = game.gameWidth
        self.gameHeight = game.gameHeight
        self.camera = camera
        self.camera.offset.x = -400
        self.camera.offset.y = -100
        self.map = [[0] * self.MAP_WIDTH for _ in range(self.MAP_HEIGHT)]
        self.xBounds = pygame.Vector2()
        self.yBounds = pygame.Vector2()
        self.selectedTile = None
        self.players = game.players

    def fillMap(self):
        #iterate left -> right first then top -> down
        for y in range(self.MAP_HEIGHT): 
            for x in range(self.MAP_WIDTH):
                if x == 5 or x == 7 or y == 3 or y == 5:
                    tile = StoneTile(x, y)
                else:
                    tile = GrassTile(x, y)
                self.map[y][x] = tile
        return self

    def render(self):
        for tileY in range (self.MAP_HEIGHT):
            for tileX in range (self.MAP_WIDTH):
                worldCoords = self.getCoords(tileX, tileY)
                if worldCoords[0] <= -self.TILE_WIDTH or worldCoords[0] >= self.gameWidth: continue
                if worldCoords[1] <= -self.TILE_HEIGHT or worldCoords[1] >= self.gameHeight: continue
                self.screen.blit(self.map[tileY][tileX].type, ( worldCoords[0], worldCoords[1] )) # currently draws all

    # 1, 0 => 32, 16 screen coord
    def getTile(self, worldCoordX, worldCoordY):
        worldCoordX += self.camera.offset.x
        worldCoordY += self.camera.offset.y
        tileX = math.floor((((self.TILE_WIDTH_HALF * (-self.TILE_HEIGHT_HALF + worldCoordY) /  self.TILE_HEIGHT_HALF) + worldCoordX) /  self.TILE_WIDTH_HALF) / 2)
        tileY = math.ceil((((-self.TILE_HEIGHT_HALF * ( self.TILE_WIDTH_HALF + (worldCoordX + self.TILE_WIDTH)) / self.TILE_WIDTH_HALF) + (worldCoordY + self.TILE_HEIGHT)) /  self.TILE_HEIGHT_HALF) / 2)
        print(tileX, tileY)
        if tileX < 0 or tileY < 0 or tileX > self.MAP_WIDTH - 1 or tileY > self.MAP_HEIGHT - 1: return
        return self.map[tileY][ tileX]

    def getCoords(self, tileX, tileY):
        worldCoordX = ((tileX - tileY) * self.TILE_WIDTH_HALF) - self.camera.offset.x
        worldCoordY = ((tileX + tileY) * self.TILE_HEIGHT_HALF) - self.camera.offset.y
        return worldCoordX, worldCoordY


