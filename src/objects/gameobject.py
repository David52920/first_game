import abc
from src.util.util import Position

class GameObject(abc.ABC):

    def __init__(self, x=0, y=0, xOffset=0, yOffset=0):
        self.position = Position(x,y)
        self.offset = Position(xOffset, yOffset)
        self.zIndex = 0





