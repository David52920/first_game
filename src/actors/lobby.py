from mimetypes import init
from actors.scene import Scene
from objects.tilesets import *
from pygame_widgets.button import Button
import pygame_widgets, pygame



class LobbyScene(Scene):
    TILE_WIDTH = 64
    TILE_HEIGHT = 32

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
        self.cameraX = 15
        self.cameraY = 12

    def initScene(self):
        button = Button(self.screen, 5, 5, 100, 25, text="Return to login")
        button.onClick = self.game.returnToLogin
        button.radius = 12
        button.inactiveColour = (235, 198, 106)
        button.hoverColour = (240, 226, 192)
        button.pressedColour = (235, 182, 54)
        self.addActor(button)

    def update(self, events=None):
        pygame_widgets.update(events)
        self.cameraX += self.game.difference[0]
        self.cameraY += self.game.difference[1]

    def render(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                tile = self.map[i][j].type
                x = (i * self.TILE_WIDTH / 2) - (j * self.TILE_WIDTH / 2) - self.TILE_WIDTH / 2
                y = (i * self.TILE_HEIGHT / 2) + (j * self.TILE_HEIGHT / 2) - self.TILE_HEIGHT / 2
                self.screen.blit(tile, (((self.game.width / 2) + x) - self.cameraX, y - self.cameraY))

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