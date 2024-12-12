import pygame
import sys
import random

# Initialisiere Pygame
pygame.init()

# Bildschirmgröße und Farben
CHAR_SIZE = 32
MAP = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','B','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1','B','1'],
    ['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],
    ['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1',' ','1','1','1',' ','1','1','-','1','1',' ','1','1','1',' ','1','1'],
    ['1',' ',' ',' ',' ','1',' ','1','s','W','o','1',' ','1',' ',' ',' ',' ','1'],
    ['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],
    ['1',' ',' ',' ','1',' ',' ',' ',' ','P',' ',' ',' ',' ','1',' ',' ',' ','1'],
    ['1','B','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','B','1'],
    ['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],
    ['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

MAP_RATIO = (len(MAP[0]), len(MAP))
WIDTH, HEIGHT = (MAP_RATIO[0] * CHAR_SIZE, MAP_RATIO[1] * CHAR_SIZE)

# Initialisiere das Spielfeld
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
    for row in MAP
]

# Pacman und Gegner
pacman_pos = [1, 1]  # Spieler oben in der Mitte
pacman_speed = [0, 0]

def get_random_direction():
    return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

# Der Gegner startet auf der Position des 'W'
enemy_pos = None
for y in range(len(MAP)):
    for x in range(len(MAP[y])):
        if MAP[y][x] == 'W':
            enemy_pos = [x, y]  # Set the enemy's starting position at 'W'
            break

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
                pygame.draw.rect(screen, BLUE, (x * CHAR_SIZE, y * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE))
            elif level[y][x] == 1:
                pygame.draw.circle(screen, WHITE, (x * CHAR_SIZE + CHAR_SIZE // 2, y * CHAR_SIZE + CHAR_SIZE // 2), 5)

    # Pacman zeichnen
    pygame.draw.circle(screen, YELLOW, (pacman_pos[0] * CHAR_SIZE + CHAR_SIZE // 2, pacman_pos[1] * CHAR_SIZE + CHAR_SIZE // 2), CHAR_SIZE // 2 - 2)

    # Gegner zeichnen
    pygame.draw.circle(screen, GREEN, (enemy_pos[0] * CHAR_SIZE + CHAR_SIZE // 2, enemy_pos[1] * CHAR_SIZE + CHAR_SIZE // 2), CHAR_SIZE // 2 - 2)

    # Spielende-Nachricht
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Spiel Ende!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(10)

# Pygame beenden
pygame.quit()
sys.exit()
