import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir el tamaño de la ventana del juego
ANCHO_VENTANA = 800
ALTURA_VENTANA = 600

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("Mi Juego")

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = ALTURA_VENTANA // 2

    def update(self):
        # Obtener la posición del ratón
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Clase de los obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_VENTANA
        self.rect.y = random.randrange(ALTURA_VENTANA)

    def update(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = ANCHO_VENTANA
            self.rect.y = random.randrange(ALTURA_VENTANA)

# Clase de los elementos recolectables
class Elemento(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_VENTANA
        self.rect.y = random.randrange(ALTURA_VENTANA)

    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.x = ANCHO_VENTANA
            self.rect.y = random.randrange(ALTURA_VENTANA)

# Crear todos los sprites
todos_los_sprites = pygame.sprite.Group()
jugador = Jugador()
todos_los_sprites.add(jugador)

obstaculos = pygame.sprite.Group()
for i in range(10):
    obstaculo = Obstaculo()
    obstaculos.add(obstaculo)
    todos_los_sprites.add(obstaculo)

elementos = pygame.sprite.Group()
for i in range(5):
    elemento = Elemento()
    elementos.add(elemento)
    todos_los_sprites.add(elemento)

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 20)

# Variable para el bucle principal del juego
jugando = True

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar los sprites
    todos_los_sprites.update()

    # Comprobar colisiones con obstáculos
    colisiones_obstaculos = pygame.sprite.spritecollide(jugador, obstaculos, False)
    if colisiones_obstaculos:
        jugando = False

    # Comprobar colisiones con elementos recolectables
    colisiones_elementos = pygame.sprite.spritecollide(jugador, elementos, True)
    for elemento in colisiones_elementos:
        puntuacion += 1

    # Limpiar la pantalla
    ventana.fill(NEGRO)

    # Dibujar los sprites
    todos_los_sprites.draw(ventana)

    # Dibujar la puntuación
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, BLANCO)
    ventana.blit(texto_puntuacion, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
