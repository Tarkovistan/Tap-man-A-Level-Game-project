import pygame

npcs = [pygame.image.load("Images/man_npc.png"), pygame.image.load("Images/lady_npc.png"),
        pygame.image.load("Images/old_man_npc.png")]


class npc(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.hitbox = (self.x, self.y, 46, 84)
        self.talking = False

    def draw1(self, win):
        if self.visible:
            win.blit(npcs[0], (self.x, self.y))  # Draws man
            self.hitbox = (self.x, self.y, 46, 84)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def draw2(self, win):
        if self.visible:
            win.blit(npcs[1], (self.x, self.y))  # Draws lady npc
            self.hitbox = (self.x, self.y, 46, 84)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def draw3(self, win):
        if self.visible:
            win.blit(npcs[2], (self.x, self.y))  # Draws old man npc
            self.hitbox = (self.x, self.y, 46, 84)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

