import pygame
import sys
import random
pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Definiendo colores
Black = (0, 0, 0)
white = (255, 255, 255)

corr_list = []
for i in range(60):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    corr_list.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(Black)
    for coord in corr_list:
        pygame.draw.circle(screen, white, coord, 2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0

    pygame.display.flip()
    clock.tick(30)
