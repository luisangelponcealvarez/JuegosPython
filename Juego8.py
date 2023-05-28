import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego Pygame")

# Definir el reloj del juego
reloj = pygame.time.Clock()

# Definir las dimensiones y la posición inicial del personaje
personaje_ancho = 50
personaje_alto = 50
personaje_x = (ANCHO_PANTALLA - personaje_ancho) / 2
personaje_y = ALTO_PANTALLA - personaje_alto

# Definir las dimensiones y la posición inicial del obstáculo
obstaculo_ancho = 100
obstaculo_alto = 100
obstaculo_x = random.randint(0, ANCHO_PANTALLA - obstaculo_ancho)
obstaculo_y = -obstaculo_alto

# Definir las dimensiones y la posición inicial del objeto
objeto_ancho = 30
objeto_alto = 30
objeto_x = random.randint(0, ANCHO_PANTALLA - objeto_ancho)
objeto_y = -objeto_alto

# Definir la puntuación inicial
puntuacion = 0

# Función para dibujar el personaje
def dibujar_personaje(x, y):
    pygame.draw.rect(pantalla, BLANCO, (x, y, personaje_ancho, personaje_alto))

# Función para dibujar el obstáculo
def dibujar_obstaculo(x, y):
    pygame.draw.rect(pantalla, BLANCO, (x, y, obstaculo_ancho, obstaculo_alto))

# Función para dibujar el objeto
def dibujar_objeto(x, y):
    pygame.draw.rect(pantalla, BLANCO, (x, y, objeto_ancho, objeto_alto))

# Función para mostrar la puntuación en la pantalla
def mostrar_puntuacion(puntos):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render("Puntuación: " + str(puntos), True, BLANCO)
    pantalla.blit(texto, (10, 10))

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Mover el personaje
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personaje_x > 0:
        personaje_x -= 5
    if teclas[pygame.K_RIGHT] and personaje_x < ANCHO_PANTALLA - personaje_ancho:
        personaje_x += 5

    # Mover el obstáculo hacia abajo
    obstaculo_y += 3

    # Si el obstáculo sale de la pantalla, generar uno nuevo y sumar puntos
    if obstaculo_y > ALTO_PANTALLA:
        obstaculo_x = random.randint(0, ANCHO_PANTALLA - obstaculo_ancho)
        obstaculo_y = -obstaculo_alto
        puntuacion += 1

    # Mover el objeto hacia abajo
    objeto_y += 5

    # Si el objeto sale de la pantalla, generar uno nuevo
    if objeto_y > ALTO_PANTALLA:
        objeto_x = random.randint(0, ANCHO_PANTALLA - objeto_ancho)
        objeto_y = -objeto_alto

    # Comprobar si el personaje colisiona con el obstáculo
    if personaje_y < obstaculo_y + obstaculo_alto and personaje_y + personaje_alto > obstaculo_y and personaje_x < obstaculo_x + obstaculo_ancho and personaje_x + personaje_ancho > obstaculo_x:
        jugando = False

    # Comprobar si el personaje recoge el objeto
    if personaje_y < objeto_y + objeto_alto and personaje_y + personaje_alto > objeto_y and personaje_x < objeto_x + objeto_ancho and personaje_x + personaje_ancho > objeto_x:
        puntuacion += 10
        objeto_x = random.randint(0, ANCHO_PANTALLA - objeto_ancho)
        objeto_y = -objeto_alto

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar el personaje, el obstáculo, el objeto y mostrar la puntuación
    dibujar_personaje(personaje_x, personaje_y)
    dibujar_obstaculo(obstaculo_x, obstaculo_y)
    dibujar_objeto(objeto_x, objeto_y)
    mostrar_puntuacion(puntuacion)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas del juego
    reloj.tick(60)

# Salir del juego
pygame.quit()
