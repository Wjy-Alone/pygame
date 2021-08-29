import pygame
from pygame.sprite import Sprite
import random

class Enemy_plane_2(Sprite):
    def __init__(self,screen,my_settings):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings

        self.image = pygame.image.load('images/enemy_plane_2_red.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(0, 462)
        self.rect.centery = random.randint(-600, 0)

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.my_settings.enemy_plane_speed
        self.rect.centery = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)