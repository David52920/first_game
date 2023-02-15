from src.util.util import Position


class Rectangle:
    def __init__(self, origin=Position(), width=0, height=0):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.center = Position(origin.X + (self.width / 2), origin.Y + (self.height / 2))
        self.topLeft = origin
        self.topRight = origin.X + self.width
        self.bottomLeft = origin.Y - self.height
        self.bottomRight = origin.X + self.width, origin.Y - self.width
        self.tup = (self.topLeft, self.topRight, self.bottomRight, self.bottomLeft)

    def __repr__(self):
        return str(self.tup)
