import pygame

class Plane():
    def __init__(self,screen,my_settings):
        self.screen = screen
        self.my_settings = my_settings

        self.image = pygame.image.load('images/plane_red.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_left = False
        self.moving_reight = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.my_settings.plane_speed
        if self.moving_reight and self.rect.right < self.screen_rect.right:
            self.centerx += self.my_settings.plane_speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.my_settings.plane_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.my_settings.plane_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def reset_plane(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)