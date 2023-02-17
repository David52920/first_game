from scenes.scene import Scene
from objects.camera import Camera
from pygame_widgets.button import Button

import pygame_widgets, pygame



from objects.gamemap import GameMap

class LobbyScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.players = game.players
        self.camera = Camera(0, 0, game.gameWidth - 200, game.gameHeight - 200)
        self.gameMap = GameMap(game, self.camera).fillMap()
        self.currentPlayer = self.players[0]
        self.clock = game.clock
        self.currentTime = game.currentTime
        self.initScene()
        self.hideActors()

    def initScene(self):
        button = Button(self.screen, 5, 5, 100, 25, text="Return")
        button.onClick = self.game.returnToLogin
        button.radius = 12
        button.inactiveColour = (235, 198, 106)
        button.hoverColour = (240, 226, 192)
        button.pressedColour = (235, 182, 54)
        self.addActor(button)

    def update(self):
        self.clock.tick(100)
        self.camera.update(self.currentPlayer)
        self.currentTime += self.clock.get_time()
        #print( self.clock.get_time())
        if self.currentTime > 15:
            for player in self.players:
                if player.moving:
                   player.move()

    def render(self, events=None):
        self.screen.fill((7, 126, 217))
        self.gameMap.render()
        self.renderPlayers()
        pygame_widgets.update(events)
        #self.camera.render()

    def renderPlayers(self):
        for player in self.players:
            player.render()

    def handleMouseButtonUp(self, mouseEvent):
        self.dragging = False

    def handleMouseButtonDown(self, mouseEvent):
        if mouseEvent.get_pressed()[0]:
            mx, my = mouseEvent.get_pos()
            self.gameMap.selectedTile = self.gameMap.getTile(mx, my)
            if self.gameMap.selectedTile:
                tileX = self.gameMap.selectedTile.position.x + 1 # add 1 to get correct tile because coords is off by 1
                tileY = self.gameMap.selectedTile.position.y
                self.currentPlayer.setDestination(self.gameMap.getCoords(tileX, tileY))
                

    def handleMouseMotion(self, mouseEvent):
        pass

    def handleKeyDown(self, keys):
        pass
