import pygame
import random
import sys

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clase para la paleta
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.rect.width) // 2
        self.rect.y = HEIGHT - 20
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

# Clase para la bola
class Ball(pygame.sprite.Sprite):
    def __init__(self, paddle):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.change_x = random.choice([-2, 2])
        self.change_y = -2
        self.paddle = paddle

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x <= 0 or self.rect.x >= WIDTH - self.rect.width:
            self.change_x *= -1
        if self.rect.y <= 0:
            self.change_y *= -1
        if self.rect.colliderect(self.paddle.rect):
            self.change_y *= -1
        if self.rect.y > HEIGHT:
            game_over()

    def reset(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.change_x = random.choice([-2, 2])
        self.change_y = -2

# Clase para los objetivos
class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def game_over():
    pygame.display.set_caption("Game Over")
    game_over_font = pygame.font.Font(None, 36)
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pinball")

# Grupos de sprites
all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()
balls = pygame.sprite.Group()
targets = pygame.sprite.Group()

# Crear objetos
paddle = Paddle()
ball = Ball(paddle)

# Agregar sprites a los grupos
all_sprites.add(paddle)
all_sprites.add(ball)
paddles.add(paddle)
balls.add(ball)

# Crear objetivos
for i in range(5):
    target = Target(random.randint(100, WIDTH - 100), random.randint(50, HEIGHT // 2))
    all_sprites.add(target)
    targets.add(target)

# Variable para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.change_x = -5
            elif event.key == pygame.K_RIGHT:
                paddle.change_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and paddle.change_x < 0:
                paddle.change_x = 0
            elif event.key == pygame.K_RIGHT and paddle.change_x > 0:
                paddle.change_x = 0

    # Actualizar sprites
    all_sprites.update()

    # Verificar colisiones entre la bola y los objetivos
    targets_hit = pygame.sprite.spritecollide(ball, targets, True)
    for target in targets_hit:
        ball.change_y *= -1

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar sprites en la pantalla
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
