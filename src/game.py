import pygame, sys
from inputhandler import InputHandler

from actors.login import LoginScene
from src.loader import Loader

class Game:
    def __init__(self):
        self.pygame = pygame
        self.pygame.display.set_caption("First Game")
        self.pygame.init()
        self.screen = pygame.display.set_mode([800, 800])
        self.inputhandler = None
        self.running = True
        self.currentscene = None
        self.scenes = [LoginScene(self)]
        self.changeScene(self.scenes[0])
        self.gameObjects = []
        self.initGameLoop()

    def initGameLoop(self):
        while self.running:
            if self.inputhandler == None:
                self.inputhandler = InputHandler(self, self.pygame)
            for event in self.pygame.event.get():
               if event.type == self.pygame.QUIT:
                   self.pygame.quit()
                   sys.exit()
               elif event.type == self.pygame.KEYDOWN:
                    self.inputhandler.handleKeyPress()
               elif event.type == self.pygame.MOUSEBUTTONDOWN:
                    self.inputhandler.handleMouseDown()

            self.screen.fill((0,0,0))

            background = Loader(pygame).loadImage(".\\res\\game_background.jpg")
            self.screen.blit(background, background.get_rect(center = self.screen.get_rect().center))

            self.updateScene()
            self.renderScene()

            self.pygame.display.update()
        self.pygame.quit()

    def updateScene(self):
        self.currentscene.update()

    def renderScene(self):
        self.currentscene.render()

    def changeScene(self, selected_scene):
        for scene in self.scenes:
            if scene == selected_scene:
                if self.currentscene:
                    self.currentscene.hideActors()
                self.currentscene = scene
                self.currentscene.showActors()

    def addScene(self, scene):
        self.scenes.append(scene)

    def returnToLogin(self):
        self.currentscene.hideActors()
        self.changeScene(self.scenes[0])


