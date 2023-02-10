import abc
import pygame
from src.loader import Loader

class Scene:
    def __init__(self):
        self.actors = []
        self.loader = Loader(pygame)     
        self.background = None

    @abc.abstractclassmethod
    def update(self):
        pass

    @abc.abstractclassmethod
    def render(self):
       pass

    @abc.abstractclassmethod
    def addActor(self, actor):
       pass

    @abc.abstractclassmethod
    def dispose(self):
       pass

    def isWidget(self, widget):
        widgetList = ["Button", "ButtonArray", "ComboBox", "Common", "DropDown", "ProgressBar", "Slider", "TextBox", "Toggle"]
        widgetClass = type(widget).__name__
        if widgetClass in widgetList:
            return True
        else:
            return False

    def addActor(self, actor):
        self.actors.append(actor)

    def hideActors(self):
        for actor in self.actors:
            if self.isWidget(actor):
                actor.hide()

    def showActors(self):
        for actor in self.actors:
            if self.isWidget(actor):
                actor.show()