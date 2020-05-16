import pygame

scree_width = 1280
screen_height = 960

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    pygame.display.flip()
    clock.tick(60) 