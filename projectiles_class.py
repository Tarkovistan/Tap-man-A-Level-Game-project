import pygame
from non_animated_images import fireball3
# Bullet class
class projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 16 * facing  # facing = -1 or 1 (Direction of bullet)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


    def draw2(self, win):
        win.blit(fireball3, (self.x, self.y))
