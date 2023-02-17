from src.util.position import Position

class Rectangle:
    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, Rectangle):
                self.x = arg.x
                self.y = arg.y
                self.width = arg.width
                self.height = arg.height
            if isinstance(arg, tuple) and len(arg) == 4:
                arg1 = arg[0]
                arg2 = arg[1]
                arg3 = arg[2]
                arg4 = arg[3]
                if (isinstance(arg1,int) or isinstance(arg1,float)) and \
                    (isinstance(arg2,int) or isinstance(arg2,float)) and \
                    (isinstance(arg3,int) or isinstance(arg3,float)) and \
                    (isinstance(arg4,int) or isinstance(arg4,float)):
                    self.x = arg1
                    self.y = arg2
                    self.width = arg3
                    self.height = arg4
                else:
                    raise TypeError("Tuple object must contain int or float.")
            elif isinstance(arg, tuple) and len(arg) == 2:
                arg1 = arg[0]
                arg2 = arg[1]
                if (isinstance(arg1,int) or isinstance(arg1,float)) and \
                    (isinstance(arg2,int) or isinstance(arg2,float)):
                    self.x = arg1
                    self.y = arg2
                    self.width = 0
                    self.height = 0
                else:
                    raise TypeError("Tuple object must contain int or float.")
            else:
                raise TypeError('Argument must be rectangle style object or tuple')
        if len(args) == 2:
            arg1 = args[0]
            arg2 = args[1]
            if (isinstance(arg1,int) or isinstance(arg1,float)) and \
                (isinstance(arg2,int) or isinstance(arg2,float)):
                self.x = arg1
                self.y = arg2
                self.width = 0
                self.height = 0
            else:
                raise TypeError('Argument must contain x and y or tuple')
        elif len(args) == 4:
            arg1 = args[0]
            arg2 = args[1]
            arg3 = args[2]
            arg4 = args[3]
            if (isinstance(arg1,int) or isinstance(arg1,float)) and \
                (isinstance(arg2,int) or isinstance(arg2,float)) and \
                (isinstance(arg3,int) or isinstance(arg3,float)) and \
                (isinstance(arg4,int) or isinstance(arg4,float)):
                self.x = arg1
                self.y = arg2
                self.width = arg3
                self.height = arg4
            else:
                raise TypeError("Tuple object must contain int or float.")
        else:
            raise Exception("Must supply values.")

        self.size = self.width, self.height
        self.area = self.width * self.height
        self.center = Position(self.x + (self.width / 2), self.y + (self.height / 2))
        self.top = self.x
        self.left = self.y
        self.bottom = self.y + self.height
        self.right = self.x + self.width

        self.topLeft = self.x, self.y
        self.topRight = self.x + self.width, self.y
        self.bottomLeft = self.x, self.y - self.height
        self.bottomRight = self.x + self.width, self.y + self.height
    
    def updateSize(self, width, height):
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.area = self.width * self.height
        self.center = Position(self.x + (self.width / 2), self.y + (self.height / 2))
        self.top = self.x
        self.left = self.y
        self.bottom = self.y + self.height
        self.right = self.x + self.width

        self.topLeft = self.x, self.y
        self.topRight = self.x + self.width, self.y
        self.bottomLeft = self.x, self.y - self.height
        self.bottomRight = self.x + self.width, self.y + self.height

    def collided(self, b):
        return self.x + self.width > b.x and b.x + b.width > self.x and \
               self.y + self.height > b.y and b.y + b.height > self.y

    def __cmp__(self, other):
        if self.x != other.x:
            return self.x == other.x
        if self.y != other.y:
            return self.y == other.y
        if self.width != other.width:
            return self.w == other.width
        if self.height != other.height:
            return self.height == other.height
        return 0

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __copy__(self):
        return Rectangle(self)

    def __getitem__(self, key):
        return (self.x, self.y, self.width, self.height)[key]

    def __setitem__(self, key, value):
        r = [self.x, self.y, self.width, self.height]
        r[key] = value
        self.x, self.y, self.width, self.height = r

    def __coerce__(self, *other):
        try:
            return self, Rectangle(*other)
        except TypeError:
            return None

    def __len__(self):
        return 4

    def __repr__(self):
        return '<rect(%d, %d, %d, %d)>' % (self.x, self.y, self.width, self.height)
