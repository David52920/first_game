import os, pygame
from pathlib import Path

class Loader:
    location = ""

    def __init__(self):
        pass

    def loadImage(self, location):
        dirname = Path(__file__).parent.parent.parent.absolute()
        return pygame.image.load(os.path.join(dirname, location)).convert_alpha()

    def loadSprite(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

loader = Loader()



