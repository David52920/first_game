import pygame, sys, os
from src.util.util import *

def launch():
    height = 800
    width = 800
    pygame.init()
    pygame.display.set_caption("First Game")
    pygame.display.set_mode([width, height])
    from game import Game
    Game(width, height)

if __name__ == '__main__':
    launch()
