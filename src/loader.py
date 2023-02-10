import os

class Loader:
    location = ""

    def __init__(self, pygame):
        self.pygame = pygame

    def loadImage(self, location):
       return self.pygame.image.load(os.path.join(location)).convert()

    def loadSprite(self):
        pass




