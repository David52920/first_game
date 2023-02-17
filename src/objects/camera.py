from src.objects.gameobject import GameObject
import pygame


class Camera(GameObject):
    def __init__(self, *origin):
        super().__init__(*origin)
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.cameraObjects = []
        self.speed = 3.5
        self.cameraborders = {'left': 100, 'right': 100, 'top': 200, 'bottom': 200}
        self.moving = False

    def addCameraObject(self, obj):
        self.cameraObjects.append(obj)

    def update(self, target):
        pass

    def render(self):
        pygame.draw.rect(self.screen, 'yellow', self.rect, 5)




