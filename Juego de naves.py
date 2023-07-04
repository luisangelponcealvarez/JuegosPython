import pygame
import sys
import random
pygame.init()

width = 800
height = 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Juego de naves")

Black = (0,0,0)
white = (255,255,255)

corr_list = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0,600)
    corr_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(Black)
    for coord in corr_list:
        pygame.draw.circle(screen, white,coord,2)
        coord[1] += 1
        if coord[1] > 600:
            coord[1] =0 
    pygame.display.flip()
    clock.tick(30)