from actors.scene import Scene
from actors.lobby import LobbyScene
from pygame_widgets.button import Button
import pygame_widgets

class LoginScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pygame = game.pygame
        self.screen = game.screen
        self.initScene()
        self.hideActors()

    def initScene(self):
        self.button = Button(self.screen, self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 150, 100, 25, text = "Login")
        self.button.onClick = self.login
        self.button.radius = 12
        self.button.inactiveColour=(235, 198, 106)
        self.button.hoverColour=(240, 226, 192)
        self.button.pressedColour=(235, 182, 54)
        self.addActor(self.button)

    def update(self):
        events = self.pygame.event.get()
        for actor in self.actors:
            if self.isWidget(actor):
                pygame_widgets.update(events)

    def render(self):
        for actor in self.actors:
            if not self.isWidget(actor):
                actor.render()

    def login(self):
        lobby = LobbyScene(self.game)
        self.game.addScene(lobby)
        self.game.changeScene(lobby)