import pygame, sys

from src.util.assetmanager import assetManager
from scenes.login import LoginScene


class Game:
    FRAME_RATE = 1000/30
    MAX_UPDATES_PER_DRAW = 5

    def __init__(self, gameWidth, gameHeight):
        self.nextFrame = pygame.time.get_ticks()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.currentTime = 0
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.running = True
        self.currentscene = None
        self.scenes = [LoginScene(self)]
        self.players = []
        self.changeScene(self.scenes[0])
        self.initGameLoop()

    def initGameLoop(self):
        while self.running:
            iterations = 0
            while (pygame.time.get_ticks() > self.nextFrame and iterations < self.MAX_UPDATES_PER_DRAW):
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

                self.updateScene()
                self.nextFrame = self.FRAME_RATE
                iterations += 1

            self.screen.fill((0,0,0))

            if isinstance(self.currentscene, LoginScene):
                if not hasattr(self, "background"):
                    self.currentBackground = assetManager.getAsset("login_background")
                self.screen.blit(self.currentBackground, self.currentBackground.get_rect(center = self.screen.get_rect().center))

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

    def addScene(self, scene):
        self.scenes.append(scene)

    def addPlayer(self, plyr):
        if len(self.players) > 0:
            for player in self.players:
                if plyr == player: return
        self.players.append(plyr)

    def returnToLogin(self):
        self.currentscene.hideActors()
        self.changeScene(self.scenes[0])


