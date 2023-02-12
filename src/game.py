import pygame, sys
from inputhandler import InputHandler

from actors.login import LoginScene
from src.loader import loader

class Game:
    def __init__(self):
        pygame.display.set_caption("First Game")
        pygame.init()
        self.height = 800
        self.width = 800
        self.screen = pygame.display.set_mode([800, 800])
        self.inputhandler = None
        self.running = True
        self.currentscene = None
        self.initialMx = 0
        self.initialMy = 0
        self.dragging = False
        self.difference = (0, 0)
        self.background = loader.loadImage("res/game_background.jpg")
        self.scenes = [LoginScene(self)]
        self.changeScene(self.scenes[0])
        self.gameObjects = []
        self.initGameLoop()

    def initGameLoop(self):
        while self.running:
            if self.inputhandler == None:
                self.inputhandler = InputHandler(self)
            mx, my = pygame.mouse.get_pos()
            event_list = pygame.event.get()
            for event in event_list:
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               elif event.type == pygame.KEYDOWN:
                    self.inputhandler.handleKeyPress()
               elif event.type == pygame.MOUSEBUTTONUP:
                   self.dragging = False
                   self.difference = (0, 0)
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   if self.initialMx != mx or self.initialMy != my and not self.dragging:
                        self.dragging = True
                        self.initialMx = mx
                        self.initialMy = my
               elif event.type == pygame.MOUSEMOTION:
                   if self.dragging:
                       self.difference = (-(mx - self.initialMx) / 100, -(my - self.initialMy) / 100)

            self.screen.fill((0,0,0))

            self.screen.blit(self.background, self.background.get_rect(center = self.screen.get_rect().center))

            self.updateScene(event_list)
            self.renderScene()

            pygame.display.update()
        pygame.quit()

    def updateScene(self, events):
        self.currentscene.update(events)

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


