from scenes.scene import Scene
from scenes.lobby import LobbyScene
from pygame_widgets.button import Button
import pygame_widgets, pygame

from src.objects.entities.player import Player

class LoginScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.initScene()
        self.hideActors()
    def refresh(self):
        pass

    def initScene(self):
        self.button = Button(self.screen, self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 150, 100, 25, text = "Login")
        self.button.onClick = self.login
        self.button.radius = 12
        self.button.inactiveColour=(235, 198, 106)
        self.button.hoverColour=(240, 226, 192)
        self.button.pressedColour=(235, 182, 54)
        self.addActor(self.button)

    def update(self):
        pass

    def render(self, events = None):
        pygame_widgets.update(events)

    def login(self):
        self.game.addPlayer(Player(0,0))
        lobby = LobbyScene(self.game)
        self.game.addScene(lobby)
        self.game.changeScene(lobby)

    def handleMouseButtonUp(self, mousePos):
        pass

    def handleMouseButtonDown(self, mousePos):
        pass

    def handleMouseMotion(self, mousePos):
        pass

    def handleKeyDown(self, keys):
        if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
            self.game.running = False
