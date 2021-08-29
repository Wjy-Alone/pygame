import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,my_settings,screen,plane):
        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, my_settings.bullet_width, my_settings.bullet_height)
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        self.y = float(self.rect.y)

        self.color = my_settings.bullet_color
        self.speed = my_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)