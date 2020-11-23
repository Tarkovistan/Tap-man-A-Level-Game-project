import pygame
walkRight = [pygame.image.load('Images/R1.png'), pygame.image.load('Images/R2.png'),  # Walking right animation [List]
             pygame.image.load('Images/R3.png'),
             pygame.image.load('Images/R4.png'), pygame.image.load('Images/R5.png'),
             pygame.image.load('Images/R6.png'),
             pygame.image.load('Images/R7.png'), pygame.image.load('Images/R8.png'),
             pygame.image.load('Images/R9.png')]

class menu_player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = False
        self.walk_count = 0

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.right:
            win.blit(walkRight[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
