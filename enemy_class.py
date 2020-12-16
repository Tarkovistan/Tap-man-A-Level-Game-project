import pygame


class enemy(object):  # ENEMY

    walk_left = [pygame.image.load('Images/L1E.png'), pygame.image.load('Images/L2E.png'),
                 pygame.image.load('Images/L3E.png'),
                 pygame.image.load('Images/L4E.png'), pygame.image.load('Images/L5E.png'),
                 pygame.image.load('Images/L6E.png'),
                 pygame.image.load('Images/L7E.png'), pygame.image.load('Images/L8E.png'),
                 pygame.image.load('Images/L9E.png'),
                 pygame.image.load('Images/L10E.png'), pygame.image.load('Images/L11E.png')]

    walk_right = [pygame.image.load('Images/R1E.png'), pygame.image.load('Images/R2E.png'),
                  pygame.image.load('Images/R3E.png'),
                  pygame.image.load('Images/R4E.png'), pygame.image.load('Images/R5E.png'),
                  pygame.image.load('Images/R6E.png'), pygame.image.load('Images/R7E.png'),
                  pygame.image.load('Images/R8E.png'),
                  pygame.image.load('Images/R9E.png'), pygame.image.load('Images/R10E.png'),
                  pygame.image.load('Images/R11E.png')]

    E_walk_left = [pygame.image.load("Images/E_L1E.png"),pygame.image.load('Images/E_L2E.png'),
                 pygame.image.load('Images/E_L3E.png'),
                 pygame.image.load('Images/E_L4E.png'), pygame.image.load('Images/E_L5E.png'),
                 pygame.image.load('Images/E_L6E.png'),
                 pygame.image.load('Images/E_L7E.png'), pygame.image.load('Images/E_L8E.png'),
                 pygame.image.load('Images/E_L9E.png'),
                 pygame.image.load('Images/E_L10E.png'), pygame.image.load('Images/E_L11E.png')]

    E_walk_right = [pygame.image.load("Images/E_R1E.png"),pygame.image.load('Images/E_R2E.png'),
                 pygame.image.load('Images/E_R3E.png'),
                 pygame.image.load('Images/E_R4E.png'), pygame.image.load('Images/E_R5E.png'),
                 pygame.image.load('Images/E_R6E.png'),
                 pygame.image.load('Images/E_R7E.png'), pygame.image.load('Images/E_R8E.png'),
                 pygame.image.load('Images/E_R9E.png'),
                 pygame.image.load('Images/E_R10E.png'), pygame.image.load('Images/E_R11E.png')]



    def __init__(self, x, y, width, height, end, vel, num, empowered):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walk_count = 0
        self.vel = vel
        self.path = (self.x, self.end)
        self.hitbox = (self.x + 20, self.y + 6, 29, 52)
        self.health = 10
        self.boss1_health = 30
        self.visible = True
        self.num = num
        self.empowered = False



    def draw(self, win):
        self.move()

        if self.empowered:
            if self.visible:

                self.move()

                if self.walk_count + 1 >= 33:
                    self.walk_count = 0

                if self.vel < 0:
                    win.blit(self.E_walk_left[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                else:
                    win.blit(self.E_walk_right[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                self.hitbox = (self.x + 20, self.y + 6, 29, 52)  # DRAWING & MOVING HITBOX (enemy)
                # pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
                if self.width > 64:
                    pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 70, self.hitbox[1] - 100, 200, 30))  # RED
                    pygame.draw.rect(win, (0, 255, 0),
                                     (self.hitbox[0] - 70, self.hitbox[1] - 100, 200 - (6.6 * (30 - self.boss1_health)),
                                      30))  # GREEN
                else:
                    pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 16, self.hitbox[1] - 20, 50, 10))  # RED
                    pygame.draw.rect(win, (0, 255, 0),
                                     (self.hitbox[0] - 16, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)),
                                      10))  # GREEN

                self.hitbox = (self.x + 17, self.y + 2, 31, 57)

        if not self.empowered:
            if self.visible:  # If health is not 0
                if self.walk_count + 1 >= 33:
                    self.walk_count = 0

                if self.vel < 0:
                    win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                else:
                    win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                self.hitbox = (self.x + 20, self.y + 6, 29, 52)  # DRAWING & MOVING HITBOX (enemy)
                # pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)

                if self.width > 64:
                    pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 70, self.hitbox[1] - 100, 200, 30))  # RED
                    pygame.draw.rect(win, (0, 255, 0),
                                     (self.hitbox[0] - 70, self.hitbox[1] - 100, 200 - (6.6 * (30 - self.boss1_health)),
                                      30))  # GREEN
                else:
                    pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 16, self.hitbox[1] - 20, 50, 10))  # RED
                    pygame.draw.rect(win, (0, 255, 0),
                                     (self.hitbox[0] - 16, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)),
                                      10))  # GREEN

                self.hitbox = (self.x + 17, self.y + 2, 31, 57)


    def move(self):
        if self.num == 1:
            if self.vel < 0:                                #
                if self.x + self.vel > self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0
            else:
                if self.x - self.vel < self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0
        if self.num == 0:
            if self.vel > 0:
                if self.x < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0

            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0


    def hit(self):
        if self.health > 0:
            self.health -= 1
            print("hit")
        else:
            self.visible = False

    def hit_boss(self):
        if self.boss1_health > 0:
            self.boss1_health -= 1
            print ("hit")
        else:
            self.visible = False


"""def draw_empowered(self, win):
        self.move()

        if self.visible:  # If health is not 0

            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.vel < 0:
                win.blit(self.E_walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.E_walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            self.hitbox = (self.x + 20, self.y + 6, 29, 52)  # DRAWING & MOVING HITBOX (enemy)
            # pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
"""