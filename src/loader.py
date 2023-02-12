import os, pygame

class Loader:
    location = ""

    def __init__(self):
        pass

    def loadImage(self, location):
        dirname = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        return pygame.image.load(os.path.join(dirname, location)).convert_alpha()

    def loadSprite(self):
        pass


loader = Loader()



