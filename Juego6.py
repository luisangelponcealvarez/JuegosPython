import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables del juego
paddle_width = 10
paddle_height = 60
ball_radius = 10
paddle_speed = 7
ball_speed_x = 3
ball_speed_y = 3

# Inicializar las paletas y la pelota
paddle1_x = 0
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width
paddle2_y = height // 2 - paddle_height // 2
ball_x = width // 2
ball_y = height // 2
ball_dx = ball_speed_x
ball_dy = ball_speed_y

# Variables de puntuación
score1 = 0
score2 = 0
font = pygame.font.Font(None, 20)

# Variables de la ventana de ganador
winner_text = pygame.font.Font(None, 48)
show_winner = False
winner = ""

# Variables de la pantalla de inicio
start_text = pygame.font.Font(None, 36)
show_start = True

clock = pygame.time.Clock()

def show_winner_screen(winner):
    screen.fill(BLACK)
    text = winner_text.render(f"¡{winner} ha ganado!", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

def show_start_screen():
    screen.fill(BLACK)
    text = start_text.render("Presiona ENTER para comenzar", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

show_start_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de las paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed

    # Actualizar la posición de la pelota
    ball_x += ball_dx
    ball_y += ball_dy

    # Comprobar colisión con las paletas
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_dx = ball_speed_x
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_dx = -ball_speed_x

    # Comprobar colisión con los bordes de la pantalla
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_dy = -ball_dy

    # Comprobar si se ha anotado un punto
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dx = ball_speed_x
        ball_dy = ball_speed_y
    if ball_x > width:
        score1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dx = -ball_speed_x
        ball_dy = -ball_speed_y

    # Comprobar si alguien ha ganado
    if score1 == 5:
        show_winner = True
        winner = "Jugador 1"
    elif score2 == 5:
        show_winner = True
        winner = "Jugador 2"

    # Mostrar la ventana de ganador
    if show_winner:
        show_winner_screen(winner)
        score1 = 0
        score2 = 0
        show_winner = False
        show_start_screen()

    # Dibujar en la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(100)

# Salir del juego
pygame.quit()
