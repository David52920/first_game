from scenes.scene import Scene
from objects.camera import Camera
from pygame_widgets.button import Button
from src.util.util import Position

import pygame_widgets



from objects.gamemap import GameMap

class LobbyScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.initScene()
        self.hideActors()
        self.camera = Camera(Position(0,0))
        self.gameMap = GameMap(game.gameWidth, game.gameHeight, self.camera)
        self.gameMap.fillMap()
        self.dragging = False
        self.difference = (0, 0)
        self.lastpos = (-10000, -10000)

    def initScene(self):
        button = Button(self.screen, 5, 5, 100, 25, text="Return")
        button.onClick = self.game.returnToLogin
        button.radius = 12
        button.inactiveColour = (235, 198, 106)
        button.hoverColour = (240, 226, 192)
        button.pressedColour = (235, 182, 54)
        self.addActor(button)

    def update(self):
        pass

    def render(self, events=None):
        self.screen.fill((7, 126, 217))
        self.gameMap.render()
        pygame_widgets.update(events)

    def handleMouseButtonUp(self, mouseEvent):
        self.dragging = False

    def handleMouseButtonDown(self, mouseEvent):
        if mouseEvent.get_pressed()[0]:
            mx, my = mouseEvent.get_pos()
            self.gameMap.selectedTile = self.gameMap.getTile(mx, my)

    def handleMouseMotion(self, mouseEvent):
        mx, my = mouseEvent.get_rel()
        if mouseEvent.get_pressed()[1]:
            self.dragging = True
            self.difference = ((mx) / 2, (my) / 2)
            self.lastpos = mouseEvent.get_pos()

    def handleKeyDown(self, keys):
        pass
