from scenes.scene import Scene
from objects.camera import Camera
from pygame_widgets.button import Button
from src.util.position import Position
import pygame_widgets



from objects.gamemap import GameMap

class LobbyScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.players = game.players
        self.initScene()
        self.hideActors()
        self.camera = Camera(0, 0, game.gameWidth - 200, game.gameHeight - 200)
        self.camera.offset.x = 100
        self.camera.offset.y = 100
        self.gameMap = GameMap(game, self.camera).fillMap()
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
        for player in self.players:
            player.update()

    def render(self, events=None):
        self.screen.fill((7, 126, 217))
        self.gameMap.render()
        self.renderPlayers()
        self.camera.render()
        pygame_widgets.update(events)

    def renderPlayers(self):
        for player in self.players:
            player.render()

    def handleMouseButtonUp(self, mouseEvent):
        self.dragging = False

    def handleMouseButtonDown(self, mouseEvent):
        if mouseEvent.get_pressed()[0]:
            mx, my = mouseEvent.get_pos()
            self.gameMap.selectedTile = self.gameMap.getTile(mx, my)
            #if self.gameMap.selectedTile:
                #self.players[0].offset = Position(mx - self.gameMap.selectedTile.xOffset , my - self.gameMap.selectedTile.yOffset)
                #self.camera.offset.x = mx * 0.5
                #self.camera.offset.y = my * 0.5
                #print(self.camera.position, self.players[0].position)

    def handleMouseMotion(self, mouseEvent):
        mx, my = mouseEvent.get_rel()
        if mouseEvent.get_pressed()[1]:
            self.dragging = True
            self.difference = ((mx) / 2, (my) / 2)
            self.lastpos = mouseEvent.get_pos()

    def handleKeyDown(self, keys):
        pass
