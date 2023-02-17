from src.objects.gameobject import GameObject
from src.util.assetmanager import assetManager

import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0)
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.image = assetManager.getAsset("player")
        rect = self.image.get_rect(center=(x,y))
        self.rect.width = rect.width
        self.rect.height = rect.height
        self.speed = 0.2
        self.moving = False
        self.destination = (0, 0)
        self.dx = 0
        self.dy = 0

    def setDestination(self, pos):
        self.destination = pos
        self.dx = self.destination[0] - self.rect.centerx
        self.dy = self.destination[1] - self.rect.centery
        self.moving = True

    def move(self):
        if self.rect.centerx != self.destination[0]:
            if self.dx > 0:
                self.rect.centerx += 1
            elif self.dx < 0:
                self.rect.centerx -= 1
        if self.rect.centery != self.destination[1]:
            if self.dy > 0:
                self.rect.centery += 1
            elif self.dy < 0:
                self.rect.centery -= 1
        elif self.rect.center == self.destination:
            self.moving = False

    def render(self):
        self.screen.blit(self.image, self.rect)




