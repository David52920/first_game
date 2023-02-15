from src.objects.gameobject import GameObject
import pygame

class Camera(GameObject):
    def __init__(self, *origin, width=0, height=0):
        super().__init__(*origin)
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Comic Sans MS', 11)
        self.cameraObjects = []
        self.width = width
        self.height = height
        print(self.rect)

    def addCameraObject(self, obj):
        self.cameraObjects.append(obj)

    def render(self):
        pygame.draw.rect(self.screen, 'yellow', self.rect, 5)




