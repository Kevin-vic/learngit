import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((600,170),0,32)
pygame.display.set_caption("Hello,world!")
background = pygame.image.load('C:\\Users\\Administrator\\Desktop\\my_bg.jpg').convert()
while True:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    pygame.display.update()