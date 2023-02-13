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
        self.mapWidth = 80
        self.mapHeight = 80
        self.map = [[0] * self.mapHeight for _ in range(self.mapWidth)]
        self.fillMap()
        self.xBoundsPos = 5000
        self.xBoundsNeg = 5000
        self.yBoundsPos = 5000
        self.yBoundsNeg = 100
        self.mapXOffset = 250
        self.cameraXOffset = 0
        self.cameraYOffset = 0
        self.dragging = False
        self.difference = (0, 0)
        self.selectedTile = (0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 7)
        self.lastpos = (-10000, -10000)

    def refresh(self):
        self.cameraXOffset = 0
        self.cameraYOffset = 0
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
            if self.lastpos == pygame.mouse.get_pos(): # stop dragging when user doesnt move the mouse but is still holding the mouse button
                self.dragging = False
            if (self.cameraXOffset >= -self.xBoundsNeg and self.cameraXOffset <= self.xBoundsPos) and (self.cameraYOffset >= -self.yBoundsNeg and self.cameraYOffset <= self.yBoundsPos):
                self.cameraXOffset -= self.difference[0]
                self.cameraYOffset -= self.difference[1]
            elif (self.cameraXOffset > self.xBoundsPos or self.cameraXOffset < -self.xBoundsNeg):
                self.cameraXOffset = -math.floor(abs(self.cameraXOffset) / 100.00) * 100 if self.cameraXOffset < 0 else math.floor(self.cameraXOffset / 100.00) * 100
            elif (self.cameraYOffset > self.yBoundsPos or self.cameraYOffset < -self.yBoundsNeg):
                self.cameraYOffset = -math.floor(abs(self.cameraYOffset) / 100.00) * 100 if self.cameraYOffset < 0 else math.floor(self.cameraYOffset / 100.00) * 100

    def render(self, events=None):
        self.screen.fill((7, 126, 217))
        for tileX in range(len(self.map)):
            for tileY in range(len(self.map[tileX])):
                tile = self.map[tileX][tileY].type
                worldX = (((tileX - tileY) * self.TILE_WIDTH_HALF) - self.cameraXOffset) + self.mapXOffset
                worldY = ((tileX + tileY) * self.TILE_HEIGHT_HALF) - self.cameraYOffset
                self.screen.blit(tile, (worldX, worldY))

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
        screenX += (self.cameraXOffset - self.mapXOffset)
        screenY += self.cameraYOffset
        tileX = math.floor((((self.TILE_WIDTH_HALF * (-self.TILE_HEIGHT_HALF + (screenY +  self.TILE_HEIGHT_HALF)) /  self.TILE_HEIGHT_HALF) + (screenX +  self.TILE_WIDTH_HALF)) /  self.TILE_WIDTH_HALF) / 2) - 1
        tileY = math.ceil((((-self.TILE_HEIGHT_HALF * ( self.TILE_WIDTH_HALF + (screenX + self.TILE_WIDTH)) / self.TILE_WIDTH_HALF) + (screenY + self.TILE_HEIGHT)) /  self.TILE_HEIGHT_HALF) / 2) 
        return (tileX, tileY)

    def handleMouseButtonUp(self, mouseEvent):
        self.dragging = False

    def handleMouseButtonDown(self, mouseEvent):
        if mouseEvent.get_pressed()[0]:
            mx, my = mouseEvent.get_pos()
            tile = self.getTile(mx, my)
            print(tile)

    def handleMouseMotion(self, mouseEvent):
        mx, my = mouseEvent.get_rel()
        if mouseEvent.get_pressed()[0]:
            self.dragging = True
            self.difference = ((mx) / 2, (my) / 2)
            self.lastpos = mouseEvent.get_pos()

    def handleKeyDown(self, keys):
        pass
