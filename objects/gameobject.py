import abc
from src.util.util import Position
from src.objects.rectangle import Rectangle


class GameObject(abc.ABC):
    def __init__(self, origin, width=0, height=0, xOffset=0, yOffset=0):
        self.rect = Rectangle(origin, width, height)
        self.position = origin
        self.offset = Position(xOffset, yOffset)
        self.zIndex = 0





