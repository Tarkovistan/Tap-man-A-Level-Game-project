import pygame

button = pygame.image.load("Images/button.png")  # Menu button overlay.
class menu_button(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_pressed = False

    def draw(self, win):
        win.blit(button, (self.x, self.y))