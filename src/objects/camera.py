from src.objects.gameobject import GameObject
from src.util.util import Position

class Camera(GameObject):
    def __init__(self, origin, width=0, height=0):
        super().__init__(x,y)
        self.cameraObjects = []
        self.width = width
        self.height = height
        self.coordinates = {"TOPLEFT": origin, 
                            "BOTTOMLEFT": Position(origin.X, origin.Y - self.height), 
                            "TOPRIGHT": Position(origin.X + self.width, y), 
                            "BOTTOMRIGHT": Position(origin.X + self.width, y - self.width)}

    def addCameraObject(self, obj):
        self.cameraObjects.append(obj)




