import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquiva los obstáculos")

# Definir los colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Definir las propiedades del personaje
character_width = 50
character_height = 50
character_x = width // 2 - character_width // 2
character_y = height - character_height
character_speed = 5

# Definir las propiedades del obstáculo
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

# Definir las propiedades del objeto
object_width = 30
object_height = 30
object_x = random.randint(0, width - object_width)
object_y = -object_height
object_speed = 2

score = 0

# Función para dibujar el personaje
def draw_character(x, y):
    pygame.draw.rect(screen, white, (x, y, character_width, character_height))

# Función para dibujar el obstáculo
def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, (x, y, obstacle_width, obstacle_height))

# Función para dibujar el objeto
def draw_object(x, y):
    pygame.draw.rect(screen, white, (x, y, object_width, object_height))

# Función para mostrar la puntuación
def show_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Puntuación: " + str(score), True, white)
    screen.blit(text, (10, 10))

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el personaje
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # Mover el obstáculo
    obstacle_y += obstacle_speed
    if obstacle_y > height:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1

    # Mover el objeto
    object_y += object_speed
    if object_y > height:
        object_x = random.randint(0, width - object_width)
        object_y = -object_height

    # Detectar colisiones
    if (
        character_y < obstacle_y + obstacle_height
        and character_y + character_height > obstacle_y
        and character_x < obstacle_x + obstacle_width
        and character_x + character_width > obstacle_x
    ):
        running = False

    if (
        character_y < object_y + object_height
        and character_y + character_height > object_y
        and character_x < object_x + object_width
        and character_x + character_width > object_x
    ):
        score += 10
        object_x = random.randint(0, width - object_width)
        object_y = -object_height

    # Dibujar los objetos en la pantalla
    draw_character(character_x, character_y)
    draw_obstacle(obstacle_x, obstacle_y)
    draw_object(object_x, object_y)
    show_score(score)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
