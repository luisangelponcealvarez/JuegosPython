import pygame
import sys
pygame.init()

# Definiendo colores
Black = (0, 0, 0)
white = (255, 255, 255)

# cordenadas de la pantalla
cord_x = 400
cord_y = 400

# animación
speed_x = 3
speed_y = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # logica del juego
    if (cord_x > 400 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 400 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y

    # crear ventana
    size = ((400, 400))
    screen = pygame.display.set_mode(size)
