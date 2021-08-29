import pygame
import sys
from bullet import Bullet
from enemy_plane import Enemy_plane

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

def create_enemy_planes(screen,enemy_planes,my_settings):
    if len(enemy_planes) < 10:
        new_enemy_plane = Enemy_plane(screen, my_settings)
        enemy_planes.add(new_enemy_plane)

def update_bullets(bullets,enemy_planes):
    bullets.update()
    hit_list = pygame.sprite.groupcollide(bullets, enemy_planes, True, True)
    #print(hit_list)

def update_enemy_planes(my_plane,enemy_planes,screen):
    enemy_planes.update()
    for enemy_plane in enemy_planes.copy():
        if enemy_plane.rect.top >= screen.get_rect().bottom:
            enemy_planes.remove(enemy_plane)

    if pygame.sprite.spritecollideany(my_plane, enemy_planes):
        print("HIT!!!!!!!!!!!!!!!")

def update_screen(screen,my_plane,bg_image,my_settings,bullets,enemy_planes):
    screen.blit(bg_image, (0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    my_plane.blitme()
    enemy_planes.draw(screen)
    #my_enemy_plane.blitme()
    pygame.display.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
