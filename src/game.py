import pygame, sys

from src.util.assetmanager import assetManager
from actors.login import LoginScene

class Game:
    def __init__(self, gameWidth, gameHeight):
        self.screen = pygame.display.get_surface()
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.inputhandler = None
        self.running = True
        self.currentscene = None
        self.scenes = [LoginScene(self)]
        self.changeScene(self.scenes[0])
        self.gameObjects = []
        self.initGameLoop()

    def initGameLoop(self):
        while self.running:
            keys = pygame.key.get_pressed()
            event_list = pygame.event.get()
            for event in event_list:
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               elif event.type == pygame.KEYDOWN:
                    self.currentscene.handleKeyDown(keys)
               elif event.type == pygame.MOUSEBUTTONUP:
                    self.currentscene.handleMouseButtonUp(pygame.mouse)
               elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentscene.handleMouseButtonDown(pygame.mouse)
               elif event.type == pygame.MOUSEMOTION:
                    self.currentscene.handleMouseMotion(pygame.mouse)

            self.screen.fill((0,0,0))

            if isinstance(self.currentscene, LoginScene):
                if not hasattr(self, "background"):
                    self.currentBackground = assetManager.getAsset("login_background")
                self.screen.blit(self.currentBackground, self.currentBackground.get_rect(center = self.screen.get_rect().center))

            self.updateScene()
            self.renderScene(event_list)

            pygame.display.update()
        pygame.quit()

    def updateScene(self):
        self.currentscene.update()

    def renderScene(self, events):
        self.currentscene.render(events)

    def changeScene(self, selected_scene):
        for scene in self.scenes:
            if scene == selected_scene:
                if self.currentscene:
                    self.currentscene.hideActors()
                self.currentscene = scene
                self.currentscene.showActors()
                self.currentscene.refresh()

    def addScene(self, scene):
        self.scenes.append(scene)

    def returnToLogin(self):
        self.currentscene.hideActors()
        self.changeScene(self.scenes[0])


