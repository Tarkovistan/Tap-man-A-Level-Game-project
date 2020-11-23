import pygame
import sqlite3
import random
from main_menu_class import menu_player
from npc_class import npc
from projectiles_class import projectile
from player_class import player
from enemy_class import enemy
from menu_button_class import menu_button
from non_animated_images import menubg, wall, bg, bg2, bg3, bubble, bubble_2 #icon, title, button


npcs = [pygame.image.load("Images/man_npc.png"), pygame.image.load("Images/lady_npc.png"),
        pygame.image.load("Images/old_man_npc.png")]
npcs_spoken_to = 0

pygame.init()  # Initiate pygame
W, H = (1280, 720)
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

running = True  # Start the menu
run = False
run_l1 = False
run_l2 = False
run_l3 = False
main_run = False

font1 = pygame.font.SysFont("comicsans", 60, True)  # Font
font2 = pygame.font.SysFont("comicsans", 25, True)  # NPC Font
font3 = pygame.font.SysFont("comicsans", 20, True)  # Lady npc Font
font_option = pygame.font.SysFont("comicsans", 30, True) # Option Font

play_text = font1.render("PLAY", 1, (0, 80, 0))
quit_text = font1.render("QUIT", 1, (0, 80, 0))
message1 = font2.render("Welcome adventurer!",1, (0, 0, 0))
message1_2 = font2.render("I hope you are liking it here...", 1, (0, 0, 0))
message1_3 = font2.render("There's been sightings of goblins", 1,(0, 0, 0))
message1_4= font2.render("lurking around the corner and", 1, (0, 0, 0))
message1_5 = font2.render("we need you to get rid of some of", 1, (0, 0, 0))
message1_6 = font2.render("those creatures, are you up for it?", 1, (0, 0, 0))
option1 = font_option.render("Y - Yes I'm up for it", 1, (255, 255, 255))
option1_2 = font_option.render("N - I need a minute to think ", 1, (255, 255, 255))

message2 = font3.render("I see you found my friend Balgruuf,", 1, (0, 0, 0))
message2_2 = font3.render("you can see that this is not a game.", 1, (0, 0, 0))
message2_3 = font3.render("The situation is getting worse with every breath", 1, (0, 0, 0))
message2_4 = font3.render("we take so I won't take anymore of your time", 1, (0, 0, 0))
message2_5 = font3.render("If you want to make a difference I need", 1, (0, 0, 0))
message2_6 = font3.render("you to take care of something, if you succeed,", 1, (0, 0, 0))
message2_7 = font3.render("praise won't be the only thing you'll get.", 1, (0, 0, 0))

message3 = font3.render("I see you are competent adventurer.", 1, (0, 0, 0))
message3_2 = font3.render("Our village is looking up at you now", 1, (0, 0, 0))
message3_3 = font3.render("The last wave of enemies was seen nearby and", 1, (0, 0, 0))
message3_4 = font3.render("you're the man to do it. If you pull this off", 1, (0, 0, 0))
message3_5 = font3.render("we will forever be in your service. However" ,1, (0, 0, 0))
message3_6 = font3.render("I warn you, those things are... well, ", 1, (0, 0, 0))
message3_7 = font3.render("something we haven't seen before. ", 1, (0, 0, 0))



button_play = menu_button((W / 2) - 200, (H / 2) - 250, 100, 200)
button_quit = menu_button((W / 2) - 200, (H / 2) + 50, 100, 200)


menubgX = 0
menubgX2 = menubg.get_width()  # Moving background




shoot_loop = 0
speed = 50
score = 0


player1 = menu_player(100, 445, 64, 64)  # Menu
player2 = player(650, 600, 100, 100)  # Game
player3 = player(200, 510, 100, 100)  # All mini games

old_man_npc = npc(1130, 370, 46, 84)  # Old man NPC
old_man_npc_2 = npc(1130, 370, 46, 84)  # After level is finished

lady_npc = npc(190, 190, 46, 84)  # Lady NPC
lady_npc_2 = npc(190, 190, 46, 84)  # After level is finished

man_npc = npc(730, 530, 46, 84)  # Man NPC
man_npc_2 = npc(730, 530, 46, 84)  # After level is finished


enemy1 = enemy(1400, 545, 64, 64, 0)  # Game
enemy2 = enemy(1400, 545, 64, 64, 0)  # Game
enemy3 = enemy(1600, 545, 64, 64, 0)  # Game





def redraw_menu_window():
    global click_play, click_quit
    click_play = pygame.draw.rect(win, (255, 0, 0), (button_play.x + 95, button_play.y + 55, 250, 85))
    click_quit = pygame.draw.rect(win, (255, 0, 0), (button_quit.x + 95, button_quit.y + 55, 250, 85))
    win.blit(menubg, (menubgX, 137))
    win.blit(menubg, (menubgX2, 137))
    win.blit(wall, (0, 0))
    win.blit(wall, (0, 583))
    player1.draw(win)
    button_play.draw(win)  # W = about 250px, H = about 80px
    button_quit.draw(win)
    win.blit(play_text, (600, 187))
    win.blit(quit_text, (600, 487))

    pygame.display.update()


def redraw_game_window():
    win.blit(bg, (0, 0))
    player2.draw(win)
    man_npc.draw1(win)
    man_npc_2.draw1(win)
    lady_npc.draw2(win)
    lady_npc_2.draw2(win)
    old_man_npc.draw3(win)
    old_man_npc_2.draw3(win)


    if man_npc.talking:
        win.blit(bubble, (man_npc.x - 310, man_npc.y - 360))
        win.blit(message1, (man_npc.x - 280, man_npc.y - 300))
        win.blit(message1_2, (man_npc.x - 280, man_npc.y - 270))
        win.blit(message1_3, (man_npc.x - 280, man_npc.y - 240))
        win.blit(message1_4, (man_npc.x - 280, man_npc.y - 210))
        win.blit(message1_5, (man_npc.x - 280, man_npc.y - 180))
        win.blit(message1_6, (man_npc.x - 280, man_npc.y - 150))

        win.blit(option1, (20, 660))
        win.blit(option1_2, (20, 690))


    if lady_npc.talking:
        win.blit(bubble_2, (lady_npc.x - 20, lady_npc.y + 60))
        win.blit(message2, (lady_npc.x + 10, lady_npc.y + 190))
        win.blit(message2_2, (lady_npc.x + 10, lady_npc.y + 220))
        win.blit(message2_3, (lady_npc.x + 10, lady_npc.y + 250))
        win.blit(message2_4, (lady_npc.x + 10, lady_npc.y + 280))
        win.blit(message2_5, (lady_npc.x + 10, lady_npc.y + 310))
        win.blit(message2_6, (lady_npc.x + 10, lady_npc.y + 340))
        win.blit(message2_7, (lady_npc.x + 10, lady_npc.y + 370))
    if old_man_npc.talking:
        win.blit(bubble, (old_man_npc.x - 310, old_man_npc.y - 360))
        win.blit(message3, (old_man_npc.x - 280, old_man_npc.y - 300))
        win.blit(message3_2, (old_man_npc.x - 280, old_man_npc.y - 270))
        win.blit(message3_3, (old_man_npc.x - 280, old_man_npc.y - 240))
        win.blit(message3_4, (old_man_npc.x - 280, old_man_npc.y - 210))
        win.blit(message3_5, (old_man_npc.x - 280, old_man_npc.y - 180))
        win.blit(message3_6, (old_man_npc.x - 280, old_man_npc.y - 150))




    pygame.display.update()


def redraw_game_2_window():

    win.blit(bg2, (0, 0))

    player3.draw(win)
    enemy1.draw(win)
    text = font1.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    for bullet in bullets:
        bullet.draw(win)

    if not enemy1.visible:
        enemy2.draw(win)
        enemy3.draw(win)
    man_npc.draw1(win)

    if not enemy1.visible and not  enemy2.visible and not enemy3.visible:
        man_npc .visible = True
        man_npc.x = 1000
        man_npc.draw1(win)
    pygame.display.update()


def redraw_game_3_window():
    win.blit(bg3, (0, 0))
    player3.draw(win)
    enemy1.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def redraw_game_4_window():
    win.blit(bg3, (0, 0))
    player3.draw(win)

    pygame.display.update()


bullets = []
enemies = [enemy1, enemy2, enemy3]
npcs_l = [man_npc, lady_npc_2, old_man_npc_2]

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x2, mouse_y2 = pygame.mouse.get_pos()

    player1.right = True
    clock.tick(speed)
    menubgX -= 1
    menubgX2 -= 1

    if menubgX < menubg.get_width() * -1:  # Moving background
        menubgX = menubg.get_width()
    if menubgX2 < menubg.get_width() * -1:
        menubgX2 = menubg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if click_play.collidepoint(mouse_pos):  # If play is clicked, run the program
                print("hit")
                running = False
                main_run = True
            if click_quit.collidepoint(mouse_pos):  # If quit is clicked, quit the program
                print("hit")
                running = False
                quit()
    print((mouse_x, mouse_y))

    redraw_menu_window()

while main_run:

    run = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_run = False
            pygame.quit()
            quit()

    while run:

        clock.tick(27)  # FPS
        keys = pygame.key.get_pressed()  # Key is held

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run = False
                pygame.quit()
                quit()
        for npc in npcs_l:
            if npc.visible:
                if player2.hitbox[1] < npc.hitbox[1] + npc.hitbox[3] and player2.hitbox[1] + \
                        player2.hitbox[3] > npc.hitbox[1]:
                    if player2.hitbox[0] + player2.hitbox[2] > npc.hitbox[0] and player2.hitbox[0] < \
                            npc.hitbox[0] + npc.hitbox[2]:

                        if npcs_spoken_to == 0:
                            if npc == npcs_l[0]:
                                man_npc.talking = True
                                if keys[pygame.K_y]:
                                    #npcs_spoken_to += 1
                                    man_npc.talking = False
                                    npc.visible = False
                                    run = False
                                    run_l1 = True

                                if keys[pygame.K_n]:
                                    player2.x = player2.x - 40
                                    man_npc.talking = False

                        if npcs_spoken_to == 0:
                            if npc == npcs_l[1]:
                                print("Test")
                                lady_npc.talking = True
                                if keys[pygame.K_y]:
                                    #npcs_spoken_to += 1
                                    lady_npc.talking = False
                                    npcs_l[1].visible = False
                                    npc.talking = True
                                    run = False
                                    run_l2 = True

                                if keys[pygame.K_n]:
                                    player2.x = player2.x - 40
                                    lady_npc.talking = False

                        if npcs_spoken_to == 0:
                            if npc == npcs_l[2]:
                                print("Test")
                                old_man_npc.talking = True
                                if keys[pygame.K_y]:
                                    old_man_npc.talking = False
                                    npcs_l[2].visible = False
                                    npc.talking = True
                                    run = False
                                    run_l3 = True

                                if keys[pygame.K_n]:
                                    player2.x = player2.x - 40
                                    old_man_npc.talking = False






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if old_man_npc.talking:
            print("old man talking")
        if man_npc.talking:
            print("man talking")
        if lady_npc.talking:
            print("lady talking")

        if not lady_npc.talking:
            if not old_man_npc.talking:
                if not  man_npc.talking:

                    if keys[pygame.K_LEFT] and player2.x > player2.vel:
                        player2.x -= player2.vel
                        player2.left = True
                        player2.right = False
                        player2.standing = False
                        player2.down = False
                        player2.up = False

                    elif keys[pygame.K_RIGHT] and player2.x < W - (player2.width - 30):
                        player2.x += player2.vel
                        player2.left = False
                        player2.right = True
                        player2.standing = False
                        player2.down = False
                        player2.up = False

                    else:
                        player2.standing = True
                        player2.walk_count = 0

                    if keys[pygame.K_DOWN] and player2.y < H - player2.height - player2.vel:
                        player2.y += player2.vel
                        player2.is_jump = False
                        player2.down = True
                        player2.up = False
                        player2.standing = False
                        player2.right = False
                        player2.left = False

                    if keys[pygame.K_UP] and player2.y > player2.vel:
                        player2.y -= player2.vel
                        player2.right = False
                        player2.left = False
                        player2.is_jump = False
                        player2.down = False
                        player2.up = True
                        player2.standing = False

        redraw_game_window()

    while run_l1:
        clock.tick(27)
        keys = pygame.key.get_pressed()


        if enemies[2].visible:
            print ("visible")
        for enemy in enemies:
            if enemy.visible:
                if player3.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player3.hitbox[1] + player3.hitbox[3] > \
                        enemy.hitbox[1]:
                    if player3.hitbox[0] + player3.hitbox[2] > enemy.hitbox[0] and player3.hitbox[0] < enemy.hitbox[
                        0] + \
                            enemy.hitbox[2]:
                        player3.hit()
                        score -= 5


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_l1 = False
                run = True
                player2.x = 650

        for bullet in bullets:
            for enemy in enemies:

                if enemy.visible:
                    if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > \
                            enemy.hitbox[1]:
                        if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + \
                                enemy.hitbox[2]:
                            enemy.hit()
                            score += 1
                            bullets.pop(bullets.index(bullet))


            if 1280 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 3:
            shoot_loop = 0
        if keys[pygame.K_SPACE] and shoot_loop == 0:
            if player3.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 40:  # Adds a bullet to the screen when SPACE is pressed.
                bullets.append(
                    projectile(round((player3.x + player3.width // 2) - 20), round(player3.y + player3.height // 2), 6,
                               (0, 0, 0),
                               facing))

                # Bullet appears a the centre of the player
            shoot_loop = 1
        if man_npc.visible:
            if player3.hitbox[1] < man_npc.hitbox[1] + man_npc.hitbox[3] and player3.hitbox[1] + \
                    player3.hitbox[3] > man_npc.hitbox[1]:
                if player3.hitbox[0] + player3.hitbox[2] > man_npc.hitbox[0] and player3.hitbox[0] < \
                        man_npc.hitbox[0] + man_npc.hitbox[2]:
                    man_npc.visible = False

                    enemy1.visible = True

                    run = True
                    run_l1 = False



        if keys[pygame.K_LEFT] and player3.x > player3.vel:
            player3.x -= player3.vel
            player3.left = True
            player3.right = False
            player3.standing = False
            player3.down = False
            player3.up = False

        elif keys[pygame.K_RIGHT] and player3.x < W - (player3.width - 30):
            player3.x += player2.vel
            player3.left = False
            player3.right = True
            player3.standing = False
            player3.down = False
            player3.up = False
        else:
            player3.standing = True

        if not player3.is_jump:
            if keys[pygame.K_UP]:
                player3.is_jump = True
                player3.right = False
                player3.left = False
                player3.down = False
                player3.up = False

        else:
            if player3.jump_count >= -10:  # Jumping quadratic equation
                neg = 1
                if player3.jump_count < 0:
                    neg = -1
                player3.y -= player3.jump_count ** 2 * 0.5 * neg
                player3.jump_count -= 1
            else:
                player3.is_jump = False
                player3.jump_count = 10

        redraw_game_2_window()

    while run_l2:
        clock.tick(27)
        keys = pygame.key.get_pressed()
        print (player3.vel)
        if enemy1.visible:
            if player3.hitbox[1] < enemy1.hitbox[1] + enemy1.hitbox[3] and player3.hitbox[1] + player3.hitbox[3] > \
                    enemy1.hitbox[1]:
                if player3.hitbox[0] + player3.hitbox[2] > enemy1.hitbox[0] and player3.hitbox[0] < enemy1.hitbox[0] + \
                        enemy1.hitbox[2]:
                    player3.hit()
                    score -= 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_l2 = False
                run_l1 = False
                run = True
                player2.x = 650

        for bullet in bullets:
            if bullet.y - bullet.radius < enemy1.hitbox[1] + enemy1.hitbox[3] and bullet.y + bullet.radius > \
                    enemy1.hitbox[1]:
                if bullet.x + bullet.radius > enemy1.hitbox[0] and bullet.x - bullet.radius < enemy1.hitbox[0] + \
                        enemy1.hitbox[2]:
                    enemy1.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

            if 1280 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 3:
            shoot_loop = 0
        if keys[pygame.K_SPACE] and shoot_loop == 0:
            if player3.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 40:  # Adds a bullet to the screen when SPACE is pressed.
                bullets.append(
                    projectile(round((player3.x + player3.width // 2) - 20), round(player3.y + player3.height // 2), 6,
                               (0, 0, 0),
                               facing))

                # Bullet appears at the centre of the player
            shoot_loop = 1
        if keys[pygame.K_LEFT] and player3.x > player3.vel:
            player3.x -= player3.vel
            player3.left = True
            player3.right = False
            player3.standing = False
            player3.down = False
            player3.up = False

        elif keys[pygame.K_RIGHT] and player3.x < W - (player3.width - 30):
            player3.x += player2.vel
            player3.left = False
            player3.right = True
            player3.standing = False
            player3.down = False
            player3.up = False
        else:
            player3.standing = True

        if not player3.is_jump:
            if keys[pygame.K_UP]:
                player3.is_jump = True
                player3.right = False
                player3.left = False
                player3.down = False
                player3.up = False

        else:
            if player3.jump_count >= -10:  # Jumping quadratic equation
                neg = 1
                if player3.jump_count < 0:
                    neg = -1
                player3.y -= player3.jump_count ** 2 * 0.5 * neg
                player3.jump_count -= 1
            else:
                player3.is_jump = False
                player3.jump_count = 10

        redraw_game_3_window()

    while run_l3:
        clock.tick(27)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_l3 = False
                run = True
                player2.x = 650


        for bullet in bullets:
            if bullet.y - bullet.radius < enemy1.hitbox[1] + enemy1.hitbox[3] and bullet.y + bullet.radius > \
                    enemy1.hitbox[1]:
                if bullet.x + bullet.radius > enemy1.hitbox[0] and bullet.x - bullet.radius < enemy1.hitbox[0] + \
                        enemy1.hitbox[2]:
                    enemy1.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

            if 1280 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 10:
            shoot_loop = 0
        if keys[pygame.K_SPACE] and shoot_loop == 0:
            if player3.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 10:  # Adds a bullet to the screen when SPACE is pressed.
                bullets.append(
                    projectile(round((player3.x + player3.width // 2) - 20), round(player3.y + player3.height // 2), 6,
                               (0, 0, 0),
                               facing))

                # Bullet appears at the centre of the player
            shoot_loop = 1
        if keys[pygame.K_LEFT] and player3.x > player3.vel:
            player3.x -= player3.vel
            player3.left = True
            player3.right = False
            player3.standing = False
            player3.down = False
            player3.up = False

        elif keys[pygame.K_RIGHT] and player3.x < W - (player3.width - 30):
            player3.x += player2.vel
            player3.left = False
            player3.right = True
            player3.standing = False
            player3.down = False
            player3.up = False
        else:
            player3.standing = True

        if not player3.is_jump:
            if keys[pygame.K_UP]:
                player3.is_jump = True
                player3.right = False
                player3.left = False
                player3.down = False
                player3.up = False

        else:
            if player3.jump_count >= -10:  # Jumping quadratic equation
                neg = 1
                if player3.jump_count < 0:
                    neg = -1
                player3.y -= player3.jump_count ** 2 * 0.5 * neg
                player3.jump_count -= 1
            else:
                player3.is_jump = False
                player3.jump_count = 10

        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_SPACE:
        # run2 = False
        # run = True

        redraw_game_4_window()
