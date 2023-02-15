from src.objects.gameobject import GameObject
from src.util.assetmanager import assetManager

import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.image = assetManager.getAsset("player")
        rect = self.image.get_rect(center=(x,y))
        self.rect.width = rect.width
        self.rect.height = rect.height
        self.speed = 0.2

    def update(self):
        self.rect.center = self.offset

    def render(self):
        self.screen.blit(self.image, (self.rect.center.x, self.rect.center.y))




