import pygame
import sys
from plane import Plane
import game_function as gf
from settings import Settings
from pygame.sprite import Group
from show_num import Show_num

def run_game():
    game_start = True

    clock = pygame.time.Clock()

    pygame.init()

    bg_image = pygame.image.load('images/bg.bmp')
    
    my_settings = Settings()
    

    screen = pygame.display.set_mode(my_settings.screen_size)

    my_plane = Plane(screen,my_settings)
    
    bullets = Group()
    enemy_planes = Group()

    pygame.display.set_caption(my_settings.screen_name)

    start_image = pygame.image.load('images/start_msg.png')

    while game_start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    game_start = False
                    break
        screen.blit(bg_image, (0,0))
        screen.blit(start_image, (0,0))
        pygame.display.update()
    while True:
        sn = Show_num(screen,my_settings.score)
        max_score = Show_num(screen, my_settings.his_score_max)
        max_score.num_rect.top = screen.get_rect().top + 20
        max_score.num_rect.centerx = screen.get_rect().centerx
        gf.check_events(my_plane,screen,bullets,my_settings)
        my_plane.update()
        gf.update_bullets(bullets,enemy_planes,my_settings)
        gf.update_enemy_planes(my_plane,enemy_planes,screen,my_settings,bullets)
        gf.create_enemy_planes(screen, enemy_planes, my_settings)
        gf.update_screen(screen,my_plane,bg_image,my_settings,bullets,enemy_planes,sn,max_score)
        clock.tick(my_settings.FPS)
        gf.fit_score(my_settings)
        #print(score)

run_game()