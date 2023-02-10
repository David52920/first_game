import pygame

class InputHandler:
    def __init__(self, game):
        self.game = game

    def handleKeyPress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
            self.game.running = False

    def handleMouseDown(self):
        mouse = pygame.mouse.get_pos()
        print(mouse)