from src.objects.gameobject import GameObject
import pygame

class Player(GameObject):
    def __init__(self, pos):
        super().__init__(x=pos.X, y=pos.Y)
        self.image = pygame.image.load('').convert_alpha()
        self.rectangle = self.image.get_rect(center=pos)
        self.speed = 5

    def update(self):
        self.rectangle.center += self.position * self.speed




