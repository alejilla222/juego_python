import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego PyGame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (Frames per Second)
FPS = 60
clock = pygame.time.Clock()

# Función para mostrar el menú principal
def mostrar_menu():
    font = pygame.font.Font(None, 74)
    text = font.render("Presiona ENTER para jugar", True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (100, 250))
    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False

# Función para mostrar el mensaje de Game Over
def mostrar_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    screen.fill(WHITE)
    screen.blit(text, (250, 150))

    font_small = pygame.font.Font(None, 36)
    text_continuar = font_small.render("Presiona ENTER para continuar", True, BLACK)
    text_salir = font_small.render("Presiona ESC para salir", True, BLACK)
    screen.blit(text_continuar, (200, 300))
    screen.blit(text_salir, (200, 350))
    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Función para crear un enemigo
def crear_enemigo():
    enemigo = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
    velocidad = random.randint(5, 10)
    return enemigo, velocidad

# Función principal del juego
def main():
    jugador = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)
    enemigos = []
    puntuacion = 0
    corriendo = True
    
    # Bucle principal del juego
    while corriendo:
        screen.fill(WHITE)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= 5
        if keys[pygame.K_RIGHT] and jugador.right < WIDTH:
            jugador.x += 5

        # Crear enemigos periódicamente
        if random.randint(1, 30) == 1:
            enemigos.append(crear_enemigo())

        # Mover enemigos y detectar colisiones
        for enemigo, velocidad in enemigos[:]:
            enemigo.y += velocidad
            if enemigo.colliderect(jugador):
                mostrar_game_over()  # Mostrar pantalla de Game Over
                return  # Volver al menú principal
            if enemigo.y > HEIGHT:
                enemigos.remove((enemigo, velocidad))
                puntuacion += 1

        # Dibujar jugador y enemigos
        pygame.draw.rect(screen, BLACK, jugador)
        for enemigo, _ in enemigos:
            pygame.draw.rect(screen, RED, enemigo)

        # Mostrar puntuación
        font = pygame.font.Font(None, 36)
        text = font.render(f"Puntuación: {puntuacion}", True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Mostrar el menú principal y luego comenzar el juego
while True:
    mostrar_menu()
    main()
