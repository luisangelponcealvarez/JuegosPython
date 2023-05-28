import pygame
import random

# Dimensiones de la ventana del juego
ANCHO = 800
ALTO = 400

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicialización de Pygame
pygame.init()

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

reloj = pygame.time.Clock()

# Posiciones y velocidades iniciales de los objetos del juego
paleta1_x = 50
paleta1_y = ALTO // 2 - 50
paleta2_x = ANCHO - 50
paleta2_y = ALTO // 2 - 50
pelota_x = ANCHO // 2
pelota_y = ALTO // 2
pelota_vel_x = random.choice([-1, 1])
pelota_vel_y = random.choice([-1, 1]) * random.randint(2, 4)
paleta_vel = 5

puntos_jugador1 = 0
puntos_jugador2 = 0

jugando = True

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Movimiento de las paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1_y > 0:
        paleta1_y -= paleta_vel
    if teclas[pygame.K_s] and paleta1_y < ALTO - 100:
        paleta1_y += paleta_vel
    if teclas[pygame.K_UP] and paleta2_y > 0:
        paleta2_y -= paleta_vel
    if teclas[pygame.K_DOWN] and paleta2_y < ALTO - 100:
        paleta2_y += paleta_vel

    # Movimiento de la pelota
    pelota_x += pelota_vel_x
    pelota_y += pelota_vel_y

    # Colisiones de la pelota con las paletas
    if pelota_x <= paleta1_x + 20 and paleta1_y <= pelota_y <= paleta1_y + 100:
        pelota_vel_x *= -1
    elif pelota_x >= paleta2_x - 20 and paleta2_y <= pelota_y <= paleta2_y + 100:
        pelota_vel_x *= -1

    # Colisiones de la pelota con los límites superior e inferior
    if pelota_y <= 0 or pelota_y >= ALTO - 20:
        pelota_vel_y *= -1

    # Puntuación
    if pelota_x <= 0:
        puntos_jugador2 += 1
        pelota_x = ANCHO // 2
        pelota_y = ALTO // 2
        pelota_vel_x = random.choice([-1, 1])
        pelota_vel_y = random.choice([-1, 1]) * random.randint(2, 4)
    elif pelota_x >= ANCHO:
        puntos_jugador1 += 1
        pelota_x = ANCHO // 2
        pelota_y = ALTO // 2
        pelota_vel_x = random.choice([-1, 1])
        pelota_vel_y = random.choice([-1, 1]) * random.randint(2, 4)

    # Dibujar en la ventana del juego
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, NEGRO, (paleta1_x, paleta1_y, 20, 100))
    pygame.draw.rect(ventana, NEGRO, (paleta2_x, paleta2_y, 20, 100))
    pygame.draw.ellipse(ventana, NEGRO, (pelota_x, pelota_y, 20, 20))

    # Mostrar puntuación en la ventana
    fuente = pygame.font.Font(None, 36)
    texto_puntos = fuente.render(
        str(puntos_jugador1) + " - " + str(puntos_jugador2), True, NEGRO
    )
    ventana.blit(texto_puntos, (ANCHO // 2 - 50, 10))

    pygame.display.flip()
    reloj.tick(100)

pygame.quit()
