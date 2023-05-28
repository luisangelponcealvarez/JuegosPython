import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Definir el tamaño de la ventana del juego
ANCHO_VENTANA = 800
ALTURA_VENTANA = 600

# Definir la velocidad del jugador y los elementos
VELOCIDAD_JUGADOR = 2
VELOCIDAD_ELEMENTOS = 1

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("Atrapa los elementos!")

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_VENTANA // 2
        self.rect.y = ALTURA_VENTANA - 70

    def update(self):
        # Obtener las teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= VELOCIDAD_JUGADOR
        if teclas[pygame.K_RIGHT]:
            self.rect.x += VELOCIDAD_JUGADOR

        # Mantener al jugador dentro de los límites de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO_VENTANA - self.rect.width:
            self.rect.x = ANCHO_VENTANA - self.rect.width

# Clase de los elementos
class Elemento(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += VELOCIDAD_ELEMENTOS
        if self.rect.y > ALTURA_VENTANA:
            self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
            self.rect.y = -self.rect.height

# Crear todos los sprites
todos_los_sprites = pygame.sprite.Group()
jugador = Jugador()
todos_los_sprites.add(jugador)

elementos = pygame.sprite.Group()
for _ in range(10):
    elemento = Elemento()
    elementos.add(elemento)
    todos_los_sprites.add(elemento)

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Tiempo
tiempo_total = 10
tiempo_restante = tiempo_total * 1000  # Convertir a milisegundos
reloj = pygame.time.Clock()

# Variable para el bucle principal del juego
jugando = True

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar los sprites
    todos_los_sprites.update()

    # Comprobar colisiones entre el jugador y los elementos
    colisiones = pygame.sprite.spritecollide(jugador, elementos, True)
    for _ in colisiones:
        puntuacion += 1

    # Calcular el tiempo restante
    tiempo_restante -= reloj.tick()
    if tiempo_restante <= 0:
        jugando = False

    # Limpiar la pantalla
    ventana.fill(BLANCO)

    # Dibujar los sprites
    todos_los_sprites.draw(ventana)

    # Dibujar la puntuación y el tiempo restante
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, NEGRO)
    ventana.blit(texto_puntuacion, (10, 10))
    texto_tiempo = fuente.render("Tiempo: " + str(tiempo_restante // 1000), True, NEGRO)
    ventana.blit(texto_tiempo, (ANCHO_VENTANA - 140, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Mostrar la puntuación final
texto_final = fuente.render("Puntuación final: " + str(puntuacion), True, NEGRO)
ventana.blit(texto_final, (ANCHO_VENTANA // 2 - 120, ALTURA_VENTANA // 2 - 20))
pygame.display.flip()

# Esperar 2 segundos antes de salir del juego
pygame.time.wait(1000)

# Cerrar Pygame
pygame.quit()
sys.exit()
