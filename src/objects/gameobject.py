import abc
from src.util.position import Position
from src.util.rectangle import Rectangle


class GameObject(abc.ABC):
    def __init__(self, *origin, xOffset=0, yOffset=0):
        self.rect = Rectangle(*origin)
        self.position = Position(self.rect.x, self.rect.y)
        self.offset = Position(xOffset, yOffset)
        self.zIndex = 0





