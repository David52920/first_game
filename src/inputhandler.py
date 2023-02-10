import pygame

class InputHandler:
    def __init__(self, game, pygame):
        self.game = game
        self.pygame = pygame

    def handleKeyPress(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_LCTRL] and keys[self.pygame.K_q]:
            self.game.running = False

    def handleMouseDown(self):
        mouse = pygame.mouse.get_pos()
        print(mouse)