import pygame

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


"""    if enemies[0-3].visible:
           if player3.hitbox[1] < enemy1.hitbox[1] + enemy1.hitbox[3] and player3.hitbox[1] + player3.hitbox[3] > \
                   enemy1.hitbox[1]:
               if player3.hitbox[0] + player3.hitbox[2] > enemy1.hitbox[0] and player3.hitbox[0] < enemy1.hitbox[0] + \
                       enemy1.hitbox[2]:
                   player3.hit()
                   score -= 5

       if enemies[0].visible:
           if player3.hitbox[1] < enemy1.hitbox[1] + enemy2.hitbox[3] and player3.hitbox[1] + player3.hitbox[3] > \
                   enemy2.hitbox[1]:
               if player3.hitbox[0] + player3.hitbox[2] > enemy2.hitbox[0] and player3.hitbox[0] < enemy2.hitbox[0] + \
                       enemy2.hitbox[2]:
                   player3.hit()
                   score -= 5

       if enemy3.visible:
           if player3.hitbox[1] < enemy3.hitbox[1] + enemy3.hitbox[3] and player3.hitbox[1] + player3.hitbox[3] > \
                   enemy3.hitbox[1]:
               if player3.hitbox[0] + player3.hitbox[2] > enemy3.hitbox[0] and player3.hitbox[0] < enemy3.hitbox[0] + \
                       enemy3.hitbox[2]:
                   player3.hit()
                   score -= 5"""
