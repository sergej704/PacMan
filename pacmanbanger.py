import pygame
import sys
import random

# Initialisiere Pygame
pygame.init()

# Bildschirmgröße und Farben
tile_size = 30
cols, rows = 30, 30
screen_width, screen_height = cols * tile_size, rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman")

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Level-Design (0 = leer, 1 = Punkt, 2 = Wand)
level = [
    [2] * cols
] + [
    [2] + [1] * (cols - 2) + [2] if i % 2 == 0 else [2] + [1, 2] * ((cols // 2) - 1) + [1, 2]
    for i in range(rows - 2)
] + [
    [2] * cols
]

# Pacman und Gegner
pacman_pos = [1, 1]
pacman_speed = [0, 0]

enemy_pos = [cols - 2, rows - 2]

def get_random_direction():
    return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

enemy_direction = get_random_direction()

# Hauptspiel-Schleife
clock = pygame.time.Clock()
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Steuerung
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                pacman_speed = [0, -1]
            if event.key in (pygame.K_DOWN, pygame.K_s):
                pacman_speed = [0, 1]
            if event.key in (pygame.K_LEFT, pygame.K_a):
                pacman_speed = [-1, 0]
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                pacman_speed = [1, 0]
            if event.key == pygame.K_ESCAPE:
                running = False

    if not game_over:
        # Bewegung von Pacman
        new_pos = [pacman_pos[0] + pacman_speed[0], pacman_pos[1] + pacman_speed[1]]
        if level[new_pos[1]][new_pos[0]] != 2:  # Kollision mit Wänden verhindern
            pacman_pos = new_pos

        # Punkt einsammeln
        if level[pacman_pos[1]][pacman_pos[0]] == 1:
            level[pacman_pos[1]][pacman_pos[0]] = 0

        # Gegner-Bewegung
        enemy_new_pos = [enemy_pos[0] + enemy_direction[0], enemy_pos[1] + enemy_direction[1]]
        if level[enemy_new_pos[1]][enemy_new_pos[0]] != 2:  # Kollision mit Wänden verhindern
            enemy_pos = enemy_new_pos
        else:
            enemy_direction = get_random_direction()

        # Überprüfen, ob Pacman vom Gegner erwischt wird
        if pacman_pos == enemy_pos:
            game_over = True

        # Überprüfen, ob alle Punkte eingesammelt wurden
        if all(cell != 1 for row in level for cell in row):
            game_over = True

    # Bildschirm aktualisieren
    screen.fill(BLACK)

    # Level zeichnen
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 2:
                pygame.draw.rect(screen, BLUE, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif level[y][x] == 1:
                pygame.draw.circle(screen, WHITE, (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), 5)

    # Pacman zeichnen
    pygame.draw.circle(screen, YELLOW, (pacman_pos[0] * tile_size + tile_size // 2, pacman_pos[1] * tile_size + tile_size // 2), tile_size // 2 - 2)

    # Gegner zeichnen
    pygame.draw.circle(screen, GREEN, (enemy_pos[0] * tile_size + tile_size // 2, enemy_pos[1] * tile_size + tile_size // 2), tile_size // 2 - 2)

    # Spielende-Nachricht
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Spiel Ende!", True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(10)

# Pygame beenden
pygame.quit()
sys.exit()
