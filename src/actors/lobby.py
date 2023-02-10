from mimetypes import init
from actors.scene import Scene
from pygame_widgets.button import Button
import pygame_widgets

class LobbyScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pygame = game.pygame
        self.screen = game.screen
        self.initScene()
        self.hideActors()

    def initScene(self):
        button = Button(self.screen, 5, 5, 100, 25, text = "Return to login")
        button.onClick = self.game.returnToLogin
        button.radius = 12
        button.inactiveColour=(235, 198, 106)
        button.hoverColour=(240, 226, 192)
        button.pressedColour=(235, 182, 54)
        self.addActor(button) 

    def update(self):
        events = self.pygame.event.get()
        for actor in self.actors:
            if self.isWidget(actor):
                pygame_widgets.update(events)

    def render(self):
        board = self.loader.loadImage(".\\res\\bejeweled\\background.png")
        self.screen.blit(board, board.get_rect(center = self.screen.get_rect().center))
        self.pygame.display.flip()