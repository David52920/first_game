from objects.tilesets import *
from src.util.position import Position

import pygame, math

class GameMap:
    TILE_WIDTH = 64
    TILE_HEIGHT = 32
    TILE_WIDTH_HALF = TILE_WIDTH / 2
    TILE_HEIGHT_HALF = TILE_HEIGHT / 2
    MAP_WIDTH = 25
    MAP_HEIGHT = 25

    def __init__(self, game, camera):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.gameWidth = game.gameWidth
        self.gameHeight = game.gameHeight
        self.camera = camera
        self.map = [[0] * self.MAP_HEIGHT for _ in range(self.MAP_WIDTH)]
        self.xBounds = Position()
        self.yBounds = Position()
        self.selectedTile = None
        self.players = game.players

    def fillMap(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 5 or i == 7 or j == 3 or j == 5:
                    tile = StoneTile(i, j)
                else:
                    tile = GrassTile(i, j)
                self.map[i][j] = tile
        return self

    def render(self):
        for tileX in range(len(self.map)):
            for tileY in range(len(self.map[tileX])):

                worldX = (((tileX - tileY) * self.TILE_WIDTH_HALF) - self.camera.offset.x) 
                worldY = ((tileX + tileY) * self.TILE_HEIGHT_HALF) - self.camera.offset.y

                if worldX <= -self.TILE_WIDTH or worldX >= self.gameWidth: continue
                if worldY <= -self.TILE_HEIGHT or worldY >= self.gameHeight: continue
                
                self.screen.blit(self.map[tileX][tileY].type, (worldX, worldY))

    def getTile(self, screenX, screenY):
        screenX += self.camera.offset.x
        screenY += self.camera.offset.y
        tileX = math.floor((((self.TILE_WIDTH_HALF * (-self.TILE_HEIGHT_HALF + (screenY +  self.TILE_HEIGHT_HALF)) /  self.TILE_HEIGHT_HALF) + (screenX +  self.TILE_WIDTH_HALF)) /  self.TILE_WIDTH_HALF) / 2) - 1
        tileY = math.ceil((((-self.TILE_HEIGHT_HALF * ( self.TILE_WIDTH_HALF + (screenX + self.TILE_WIDTH)) / self.TILE_WIDTH_HALF) + (screenY + self.TILE_HEIGHT)) /  self.TILE_HEIGHT_HALF) / 2) 
        if tileX < 0 or tileY < 0 or tileX > self.MAP_WIDTH - 1 or tileY > self.MAP_HEIGHT - 1: return
        return self.map[tileX][ tileY]


