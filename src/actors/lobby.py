from mimetypes import init
from actors.scene import Scene
from objects.tilesets import *
from pygame_widgets.button import Button
import pygame_widgets, pygame, math, pygame.freetype



class LobbyScene(Scene):
    TILE_WIDTH = 64
    TILE_HEIGHT = 32
    TILE_WIDTH_HALF = TILE_WIDTH / 2
    TILE_HEIGHT_HALF = TILE_HEIGHT / 2

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.initScene()
        self.hideActors()
        self.mapWidth = 32
        self.mapHeight = 24
        self.map = [[0] * self.mapHeight for _ in range(self.mapWidth)]
        self.fillMap()
        self.cameraX = 0
        self.cameraY = 0
        self.dragging = False
        self.difference = (0, 0)
        self.selectedTile = (0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 7)

    def refresh(self):
        self.cameraX = 0
        self.cameraY = 0
        self.dragging = False
        self.difference = (0, 0)
        self.selectedTile = (0, 0)

    def initScene(self):
        button = Button(self.screen, 5, 5, 100, 25, text="Return to login")
        button.onClick = self.game.returnToLogin
        button.radius = 12
        button.inactiveColour = (235, 198, 106)
        button.hoverColour = (240, 226, 192)
        button.pressedColour = (235, 182, 54)
        self.addActor(button)

    def update(self):
        if self.dragging:
            if (self.cameraX >= -500 and self.cameraX <= 500) and (self.cameraY >= -500 and self.cameraY <= 500):
                self.cameraX -= self.difference[0]
                self.cameraY -= self.difference[1]
            elif (self.cameraX > 500 or self.cameraX < -500):
                self.cameraX = -math.floor(abs(self.cameraX) / 100.00) * 100 if self.cameraX < 0 else math.floor(self.cameraX / 100.00) * 100
            elif (self.cameraY > 500 or self.cameraY < -500):
                self.cameraY = -math.floor(abs(self.cameraY) / 100.00) * 100 if self.cameraY < 0 else math.floor(self.cameraY / 100.00) * 100

    def render(self, events=None):
        for tileX in range(len(self.map)):
            for tileY in range(len(self.map[tileX])):
                tile = self.map[tileX][tileY].type
                worldX = ((tileX - tileY) * self.TILE_WIDTH_HALF) - self.cameraX
                worldY = ((tileX + tileY) * self.TILE_HEIGHT_HALF) - self.cameraY
                self.screen.blit(tile, (250 + worldX, worldY))
                text_surface = self.font.render("(" + str(worldX) +", " + str(worldY) + ")", False,  (0, 0, 0))
                self.screen.blit(text_surface, (265 + worldX, 5 + worldY))

        pygame_widgets.update(events)

    def fillMap(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 5 or i == 7 or j == 3 or j == 5:
                    tile = StoneTile(i, j)
                elif i == 6 or j == 4:
                    tile = BrickTile(i,j)
                else:
                    tile = GrassTile(i, j)
                self.map[i][j] = tile
   
    def getTile(self, screenX, screenY):
        xTile = math.floor(( self.TILE_WIDTH_HALF * ((- self.TILE_HEIGHT_HALF + (screenY +  self.TILE_HEIGHT_HALF)) /  self.TILE_HEIGHT_HALF) + (screenX +  self.TILE_WIDTH_HALF)) /  self.TILE_WIDTH_HALF / 2)
        yTile = math.ceil((((- self.TILE_HEIGHT_HALF * ( self.TILE_WIDTH_HALF + (screenX + self.TILE_WIDTH)) / self.TILE_WIDTH_HALF) + (screenY + self.TILE_HEIGHT)) /  self.TILE_HEIGHT_HALF) / 2);
        return (xTile, yTile)

    def handleMouseButtonUp(self, mouseEvent):
        self.dragging = False

    def handleMouseButtonDown(self, mouseEvent):
        if mouseEvent.get_pressed()[0]:
            mx, my = mouseEvent.get_pos()
            tile = self.getTile(mx - 250, my)
            print(tile)

    def handleMouseMotion(self, mouseEvent):
        mx, my = mouseEvent.get_rel()
        if mouseEvent.get_pressed()[0]:
            self.dragging = True
            self.difference = ((mx) / 2, (my) / 2)

    def handleKeyDown(self, keys):
        pass
