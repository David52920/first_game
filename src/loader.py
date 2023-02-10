import os, pygame

class Loader:
    location = ""

    def __init__(self):
        pass

    def loadImage(self, location):
       return pygame.image.load(os.path.join(location)).convert()

    def loadSprite(self):
        pass


loader = Loader()



