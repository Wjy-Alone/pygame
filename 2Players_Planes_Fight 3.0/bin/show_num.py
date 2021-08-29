import pygame.font

class Show_num():
    def __init__(self,screen,num):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.num = num

        self.num_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_num()
    
    def prep_num(self):
        num_str = str(self.num)
        self.num_image = self.font.render(num_str, True, self.num_color)

        self.num_rect = self.num_image.get_rect()
        self.num_rect.right = self.screen_rect.right - 20
        self.num_rect.top = 20

    def show_num(self):
        self.screen.blit(self.num_image,self.num_rect)