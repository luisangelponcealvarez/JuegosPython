import pygame

# Configuración de la ventana
pygame.init()
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del Dinosaurio")
# Creación del dinosaurio
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = height - dino_height - 50
dino = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

# Creación de las barras
bar_width = 30
bar_height = 80
bar_gap = 150
bar_x = width
bar_y = height - bar_height - 50
bar1 = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
bar2 = pygame.Rect(bar_x + bar_gap, bar_y, bar_width, bar_height)
# Velocidad del juego y movimiento de los elementos
clock = pygame.time.Clock()
speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimiento del dinosaurio
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dino.y == dino_y:
        dino.y -= 100
    elif dino.y < dino_y:
        dino.y += 10

    # Movimiento de las barras
    bar1.x -= speed
    bar2.x -= speed

    # Si las barras salen de la pantalla, las volvemos a colocar al final
    if bar1.x < -bar_width:
        bar1.x = width
    if bar2.x < -bar_width:
        bar2.x = width
    # Verificar si el dinosaurio ha chocado con una de las barras
    if dino.colliderect(bar1) or dino.colliderect(bar2):
        print("¡Perdiste!")
        pygame.quit()
        quit()

    # Dibujar los elementos en la pantalla
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), dino)
    pygame.draw.rect(window, (0, 0, 0), bar1)
    pygame.draw.rect(window, (0, 0, 0), bar2)
    pygame.display.update()

    # Limitar la velocidad del juego
    clock.tick(30)
