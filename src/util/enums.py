from enum import Enum


Object = lambda **kwargs: type("Object", (), kwargs)


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
