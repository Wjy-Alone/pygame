import pygame
import sys
from plane import Plane
import game_function as gf
from settings import Settings
from pygame.sprite import Group
#from enemy_plane import Enemy_plane

def run_game():
    clock = pygame.time.Clock()

    pygame.init()

    bg_image = pygame.image.load('images/bg.bmp')
    
    my_settings = Settings()

    screen = pygame.display.set_mode(my_settings.screen_size)

    my_plane = Plane(screen,my_settings)
    #my_enemy_plane = Enemy_plane(screen, my_settings)
    bullets = Group()
    enemy_planes = Group()

    pygame.display.set_caption(my_settings.screen_name)

    while True:
        gf.check_events(my_plane,screen,bullets,my_settings)
        my_plane.update()
        gf.update_bullets(bullets,enemy_planes)
        gf.update_enemy_planes(my_plane,enemy_planes,screen)
        gf.create_enemy_planes(screen, enemy_planes, my_settings)
        gf.update_screen(screen,my_plane,bg_image,my_settings,bullets,enemy_planes)
        clock.tick(my_settings.FPS)
run_game()