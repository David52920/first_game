from src.objects.gameobject import GameObject
from src.objects.rectangle import Rectangle
from src.util.util import Position

class Camera(GameObject):
    def __init__(self, origin=Position(), width=0, height=0):
        super().__init__(origin)
        self.cameraObjects = []
        self.width = width
        self.height = height

    def addCameraObject(self, obj):
        self.cameraObjects.append(obj)




