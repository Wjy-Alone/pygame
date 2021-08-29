import pygame
import sys
from bullet import Bullet
from enemy_plane import Enemy_plane
from enemy_plane_2 import Enemy_plane_2
import random
import time

def check_events(my_plane,screen,bullets,my_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                my_plane.moving_left = True
            if event.key == pygame.K_d:
                my_plane.moving_reight = True
            if event.key == pygame.K_w:
                my_plane.moving_up = True
            if event.key == pygame.K_s:
                my_plane.moving_down = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < my_settings.bullet_max:
                    new_bullet = Bullet(my_settings, screen, my_plane)
                    bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                my_plane.moving_left = False
            if event.key == pygame.K_d:
                my_plane.moving_reight = False
            if event.key == pygame.K_w:
                my_plane.moving_up = False
            if event.key == pygame.K_s:
                my_plane.moving_down = False

def quit_game(screen):
    game_over_image = pygame.image.load('images/game_over.bmp')
    screen.blit(game_over_image,(0,0))
    pygame.display.update()
    print("Game Over")
    time.sleep(3)
    sys.exit()

def reset_game(my_settings,enemy_planes,bullets,my_plane,screen):
    my_settings.plane_leave -= 1
    if my_settings.plane_leave > 0:
        enemy_planes.empty()
        bullets.empty()

        my_plane.reset_plane()

        time.sleep(my_settings.reset_time)

    else:
        quit_game(screen)

def create_enemy_planes(screen,enemy_planes,my_settings):
    if len(enemy_planes) < 10:
        new_enemy_plane = Enemy_plane(screen, my_settings)
        enemy_planes.add(new_enemy_plane)
        c_num = random.randint(0, 10)
        if c_num == 5:
            new_enemy_plane_2 = Enemy_plane_2(screen, my_settings)
            enemy_planes.add(new_enemy_plane_2)

def update_bullets(bullets,enemy_planes,my_settings):
    bullets.update()
    hit_list = pygame.sprite.groupcollide(bullets, enemy_planes, False, True)
    if (len(hit_list)) > 0:
        my_settings.score += 1
def update_enemy_planes(my_plane,enemy_planes,screen,my_settings,bullets):
    enemy_planes.update()
    for enemy_plane in enemy_planes.copy():
        if enemy_plane.rect.top >= screen.get_rect().bottom:
            enemy_planes.remove(enemy_plane)
            my_settings.score -= 1
        if enemy_plane.rect.left < screen.get_rect().left:
            enemy_planes.remove(enemy_plane)
    if pygame.sprite.spritecollideany(my_plane, enemy_planes):
        reset_game(my_settings, enemy_planes, bullets, my_plane, screen)     
    if my_settings.score <= -10:
        my_settings.score = 0
        reset_game(my_settings, enemy_planes, bullets, my_plane, screen)
def fit_score(my_settings):
    if int(my_settings.score) > int(my_settings.his_score_max):
        with open('score_max.txt','w') as file:
            file.write(str(my_settings.score))

    if 10 <= my_settings.score <= 20:
        my_settings.enemy_plane_speed = 0.5
    elif 20 < my_settings.score <= 30:
        my_settings.enemy_plane_speed = 0.6
    elif 30 < my_settings.score <= 40:
        my_settings.enemy_plane_speed = 0.7
    elif 40 < my_settings.score <= 50:
        my_settings.enemy_plane_speed = 0.8
    elif 50 < my_settings.score <= 60:
        my_settings.enemy_plane_speed = 0.9
    elif 60 < my_settings.score <= 70:
        my_settings.enemy_plane_speed = 1.0
    elif 70 < my_settings.score <= 80:
        my_settings.enemy_plane_speed = 1.1
    elif 80 < my_settings.score <= 90:
        my_settings.enemy_plane_speed = 1.2
    elif 90 < my_settings.score <= 100:
        my_settings.enemy_plane_speed = 1.3

def update_screen(screen,my_plane,bg_image,my_settings,bullets,enemy_planes,sn,max_score):
    screen.blit(bg_image, (0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    my_plane.blitme()
    enemy_planes.draw(screen)
    sn.show_num()
    max_score.show_num()
    pygame.display.update()


    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
