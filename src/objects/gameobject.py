import abc
from src.util.rectangle import Rectangle
import pygame

class GameObject(abc.ABC):
    def __init__(self, *origin, xOffset=0, yOffset=0):
        self.rect = pygame.Rect(*origin)
        self.position = pygame.Vector2(self.rect.x, self.rect.y)
        self.offset = pygame.Vector2(xOffset, yOffset)
        self.zIndex = 0
        self.center = self.rect.center





