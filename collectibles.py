import pygame


W, H = (1280, 720)
win = pygame.display.set_mode((W, H))

from non_animated_images import fireball2

class collectibles(object):
    def __init__(self, x, y, width, height, visible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 62, 71)
        self.visible = False


    def draw(self):
        if self.visible:
            win.blit(fireball2,(self.x, self.y))

            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
