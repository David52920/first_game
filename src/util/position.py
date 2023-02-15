class Position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def equals(self, pos2):
        if not isinstance(pos2, Position): return
        return self.x == pos2.x and self.y == pos2.y and self.z == pos2.z

    def distanceTo(self, pos2):
        if not isinstance(pos2, Position): return
        d1 = pos2.x - self.x
        d2 = pos2.Y - self.y
        d3 = pos2.z - self.z
        return math.sqrt(d1^2 + d2^2)

    def __cmp__(self, other):
        if self.x != other.x:
            return self.x == other.x
        if self.y != other.y:
            return self.y == other.y
        if self.z != other.z:
            return self.z == other.z
        return 0

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z = 0
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z = 0
        return self

    def __mul__(self, value):
        self.x *= value
        self.y *= value
        self.z = 0
        return self

    def __copy__(self):
        return Position(self)

    def __getitem__(self, key):
        return (self.x, self.y, self.z)[key]

    def __setitem__(self, key, value):
        r = [self.x, self.y, self.z]
        r[key] = value
        self.x, self.y, self.z = r

    def __len__(self):
        return 3

    def __repr__(self):
        return '<position(%d, %d, %d)>' % (self.x, self.y, self.z)