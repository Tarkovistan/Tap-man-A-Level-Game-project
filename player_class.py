import pygame

W, H = (1280, 720)
win = pygame.display.set_mode((W, H))

# win = pygame.display.set_mode((W, H))
character_walking = [pygame.image.load("Images/knight_left.png"), pygame.image.load("Images/knight_right.png"),
                     pygame.image.load("Images/knight_up.png"), pygame.image.load("Images/knight_down.png")]


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.standing = True
        self.right = False
        self.up = False
        self.down = True
        self.left = False
        self.walk_count = 0
        self.jump_count = 10
        self.is_jump = False
        self.hitbox = (self.x, self.y, 50, 88)

    def draw(self, win):
        if not self.standing:
            if self.right:
                win.blit(character_walking[1], (self.x, self.y))
            elif self.left:
                win.blit(character_walking[0], (self.x, self.y))
            if self.up:
                win.blit(character_walking[2], (self.x, self.y))
            if self.down:
                win.blit(character_walking[3], (self.x, self.y))

        else:
            if self.right:
                win.blit(character_walking[1], (self.x, self.y))
            elif self.up:
                win.blit(character_walking[2], (self.x, self.y))
            elif self.down:
                win.blit(character_walking[3], (self.x, self.y))
            else:
                win.blit(character_walking[0], (self.x, self.y))

        self.hitbox = (self.x, self.y, 50, 88)  # DRAWING & MOVING HITBOX
        pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)

    def hit(self):  # Resets the char when hits the enemy
        self.is_jump = False
        self.down = True
        self.jump_count = 10
        self.x = 650
        self.y = 510
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5", 1, (255, 0, 0,))
        win.blit(text, (640, 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 101
                    pygame.quit()
