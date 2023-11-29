import sys
import time
import pygame

pygame.init()

bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,0)

screen_image = pygame.display.set_mode((1300,800))
screen_rect = screen_image.get_rect()

pygame.display.set_caption("哆啦a梦的复仇")

ship_image = pygame.image.load('images/ship.bmp')
ship_rect = ship_image.get_rect()
ship_rect.center = screen_rect.center

backbroad_image = pygame.image.load('images/backbroad.bmp')
backbroad_rect = backbroad_image.get_rect()
backbroad_rect.center = screen_rect.center

bullet_image = pygame.image.load('images/bullet.bmp')
bullet_rect = bullet_image.get_rect()
bullet_rect.midbottom = ship_rect.midtop

txt_font = pygame.font.SysFont(None,48)
txt_image = txt_font.render('58',True,bg_color2,bg_color3)
txt_rect = txt_image.get_rect()
txt_rect.x = 1120
txt_rect.y = 740

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ship_rect.x -= 30
            if event.key == pygame.K_d:
                ship_rect.x += 30
            if event.key == pygame.K_w:
                ship_rect.y -= 30
            if event.key == pygame.K_s:
                ship_rect.y += 30 
                
    screen_image.fill(bg_color1)
    screen_image.blit(backbroad_image,backbroad_rect)
    screen_image.blit(ship_image,ship_rect)
    screen_image.blit(bullet_image,bullet_rect)
    screen_image.blit(txt_image,txt_rect)
    pygame.display.flip()