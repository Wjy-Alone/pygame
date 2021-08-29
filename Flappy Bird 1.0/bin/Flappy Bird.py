import pygame
import sys
import random
import time
bg_image = pygame.image.load('bg.png')
bird_image1 = bird_image1_copy = pygame.image.load('bird1.png')
bird_image2 = bird_image2_copy = pygame.image.load('bird2.png')
pipe_down = pygame.image.load('pipe_down.png')
pipe_up = pygame.image.load('pipe_up.png')
land_image = pygame.image.load('land.png')
pipe_pos = [[[200,-150],[200,300]],[[360,-140],[360,320]],[[520,-170],[520,350]],[[680,-200],[680,280]]]
bird_x = 30
bird_y = 144
bird_width = 34
bird_height = 24
pipes_width = 52
pipes_height = 320
land_x = 0
G_down = 0.8
frame = 0
FPS = 60
clock = pygame.time.Clock()
s = 0
pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Flappy Bird")
def draw_bird(bird_x,bird_y):
    global frame
    if 0 <= frame <= 30:
        screen.blit(bird_image1, (bird_x,bird_y))
        frame += 1
    elif  30 < frame <= 60:
        screen.blit(bird_image2, (bird_x,bird_y))
        frame += 1
        if frame == 60:
            frame = 0
while_stats = False
while True:
    if while_stats:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= 40
                G_down = 0
    bird_image1 = pygame.transform.rotate(bird_image1_copy, -90*(G_down/15))
    bird_image2 = pygame.transform.rotate(bird_image2_copy, -90*(G_down/15))
    screen.blit(bg_image, (0,0))
    draw_bird(bird_x, bird_y)
    bird_y += G_down
    G_down += 0.1
    clock.tick(FPS)
    if bird_y <= 0 or bird_y >= 460:
        time.sleep(3)
        break 
    for i in range(4):
        a_x = bird_x
        a_y = bird_y
        b_x = pipe_pos[i][0][0]
        b_y = pipe_pos[i][0][1]
        a_width = bird_width
        a_height = bird_height
        b_width = pipes_width
        b_height = pipes_height
        screen.blit(pipe_down, (pipe_pos[i][0][0],pipe_pos[i][0][1]))
        screen.blit(pipe_up, (pipe_pos[i][0][0],pipe_pos[i][1][1]))
        pipe_pos[i][0][0] -= 1
        pipe_pos[i][1][0] -= 1
        if pipe_pos[i][0][0] <= -50:
            del pipe_pos[i]
        if len(pipe_pos) < 4:
            new_y = random.randint(-200, -100)
            size = random.randint(96, 192)
            pipe_pos.append([[pipe_pos[-1][0][0]+160,new_y],[pipe_pos[-1][0][0]+120,new_y+320+size]])
        if b_x <= a_x + a_width <= b_x + b_width and b_y <= a_y + a_height <= b_y + b_height:
            while_stats = True
            time.sleep(3)
            break
        if a_x <= b_x + b_width <= a_x + a_width and a_y <= b_y + b_height<= a_y + a_height:
            while_stats = True
            time.sleep(3)
            break
        b_x = pipe_pos[i][1][0]
        b_y = pipe_pos[i][1][1]
        if b_x <= a_x + a_width <= b_x + b_width and b_y <= a_y + a_height <= b_y + b_height:
            while_stats = True
            time.sleep(3)
            break
        if a_x <= b_x + b_width <= a_x + a_width and a_y <= b_y <= a_y + a_height:
            while_stats = True
            time.sleep(3)
            break
    screen.blit(land_image, (land_x,460))
    land_x -= 1
    if land_x <= -47:
        land_x = 0
    if s == 1:
        time.sleep(3)
    s+=1
    pygame.display.update()