import pygame
import sys
import random
import math
import os
import imageio
import numpy as np
import time
import cv2

GAME_RUNNING = 1
GAME_STOP = 2

game_state = GAME_RUNNING

file_path = os.path.realpath(__file__)

directory = os.path.dirname(file_path)

sprites_path = os.path.join(directory, "PacManSprites")

music_path = os.path.join(directory, "music")

pygame.init()

CHAR_SIZE = 32
MAP = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1',' ','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1',' ','1'],
    ['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],
    ['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1',' ','1','1','1',' ','1','1',' ','1','1',' ','1','1','1',' ','1','1'],
    ['1',' ',' ',' ',' ','1',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ','1'],
    ['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],
    ['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],
    ['1',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ','1'],
    ['1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1'],
    ['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],
    ['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

MAP_RATIO = (len(MAP[0]), len(MAP))

MAP_HARD = [
#     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],#0
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#1
    ['1',' ','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1',' ',' ',' ','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1',' ','1'],#2
    ['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],#3
    ['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],#4
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],#5
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],#6
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#7
    ['1','1',' ','1','1','1',' ','1','1',' ','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1',' ','1','1',' ','1','1','1',' ','1','1'],#8
    ['1',' ',' ',' ',' ','1',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ','1'],#9
    ['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],#10
    ['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],#11
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ',' ',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],#12
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#13
    ['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],#14
    ['1',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ','1'],#15
    ['1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1'],#16
    ['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],#17
    ['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ',' ',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],#18
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#19
    ['1',' ',' ','1',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ','1',' ',' ','1'],#20
    ['1',' ','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1',' ',' ',' ','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1',' ','1'],#21
    ['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],#22
    ['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],#23
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],#24
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],#25
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#26
    ['1','1',' ','1','1','1',' ','1','1',' ','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1',' ','1','1',' ','1','1','1',' ','1','1'],#27
    ['1',' ',' ',' ',' ','1',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ','1'],#28
    ['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],#29
    ['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],#30
    ['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ',' ',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],#31
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#32
    ['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],#33
    ['1',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ','1'],#34
    ['1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1',' ','1'],#35
    ['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],#36
    ['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ',' ',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],#37
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],#38
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],#39
]

MAP_HARD_RATIO = (len(MAP_HARD[0]), len(MAP_HARD))

# Get the screen resolution
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Prozentsatz der Bildschirmgröße, den das Spielfeld einnehmen soll 
scale_percent = 0.7

# Berechne die Breite und Höhe des Spielfelds basierend auf dem Prozentsatz
scaled_width = screen_width * scale_percent
scaled_height = screen_height * scale_percent

# Berechne die neue CHAR_SIZE basierend auf der skalierten Bildschirmgröße
def calculate_char_size(scaled_width, scaled_height, map_width, map_height):
    max_width_char_size = scaled_width // map_width
    max_height_char_size = scaled_height // map_height
    return min(max_width_char_size, max_height_char_size)

# Berechne die neue CHAR_SIZE
CHAR_SIZE = calculate_char_size(scaled_width, scaled_height, len(MAP[0]), len(MAP))

# Berechne die neuen Dimensionen des Spielfelds
WIDTH = len(MAP[0]) * CHAR_SIZE
HEIGHT = len(MAP) * CHAR_SIZE

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman")

# Berechne die Position des Spielfelds in der Mitte des Bildschirms
x_pos = (screen_width - WIDTH) // 2
y_pos = (screen_height - HEIGHT) // 2

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINK = (255, 105, 180)

level = [
    [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
    for row in MAP
]

# Pacman
pacman_pos = [9, 1]  
pacman_speed = [0, 0]

def get_random_direction():
    return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

# Gegner-Verwaltung
NUM_ENEMIES = 4  
center_x, center_y = MAP_RATIO[0] // 2, MAP_RATIO[1] // 2

def calculate_direction_to_pacman(enemy_pos, pacman_pos, pacman_velocity):
    dx = pacman_pos[0] - enemy_pos[0]
    dy = pacman_pos[1] - enemy_pos[1]

    # Vorhersage der Pacman-Bewegung (basierend auf der Geschwindigkeit)
    predicted_pacman_pos = (pacman_pos[0] + pacman_velocity[0], pacman_pos[1] + pacman_velocity[1])
    dx = predicted_pacman_pos[0] - enemy_pos[0]
    dy = predicted_pacman_pos[1] - enemy_pos[1]

    # Priorisieren der horizontalen Bewegung (x) oder vertikalen Bewegung (y)
    if abs(dx) > abs(dy):
        if dx > 0:
            return (1, 0)  # Rechts
        elif dx < 0:
            return (-1, 0)  # Links
    else:
        if dy > 0:
            return (0, 1)  # Unten
        elif dy < 0:
            return (0, -1)  # Oben

    # Wenn beide Achsen eine ähnliche Differenz aufweisen, beide Achsen gleichzeitig bewegen (diagonal)
    if dx > 0 and dy > 0:
        return (1, 1)  # Rechts unten
    elif dx > 0 and dy < 0:
        return (1, -1)  # Rechts oben
    elif dx < 0 and dy > 0:
        return (-1, 1)  # Links unten
    elif dx < 0 and dy < 0:
        return (-1, -1)  # Links oben

def enemy_AI(enemy, pacman_pos, pacman_velocity, mode='chase'):
    direction = None
    if mode == 'chase':
        direction = calculate_direction_to_pacman(enemy["pos"], pacman_pos, pacman_velocity)
    elif mode == 'scatter':
        direction = get_random_direction()
    elif mode == 'ambush':
        direction = get_random_direction() if random.random() > 0.5 else calculate_direction_to_pacman(enemy["pos"], pacman_pos, pacman_velocity)

    if direction is None:
        direction = get_random_direction()

    return direction

enemy_positions = [
    (center_x, center_y),  
    (center_x - 1, center_y),  
    (center_x + 1, center_y),  
    (center_x, center_y - 1)  
]

enemies = [
    {"pos": list(enemy_positions[0]), "initial_pos": list(enemy_positions[0]), "mode": 'chase', "color": RED},  
    {"pos": list(enemy_positions[1]), "initial_pos": list(enemy_positions[1]), "mode": 'scatter', "color": GREEN},  
    {"pos": list(enemy_positions[2]), "initial_pos": list(enemy_positions[2]), "mode": 'ambush', "color": PINK},  
    {"pos": list(enemy_positions[3]), "initial_pos": list(enemy_positions[3]), "mode": 'scatter', "color": BLUE},  
]

# Pacman-Animation
def scale_sprite(image, size):
    return pygame.transform.scale(image, (size, size))

pacman_sprites = {
    "up": [
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthOpenUP.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthHalfOpenUP.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanFull.png")), CHAR_SIZE),  
    ],
    "down": [
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthOpendown.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthHalfOpenDOWN.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanFull.png")), CHAR_SIZE),  
    ],
    "left": [
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthOpenLEFT.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthHalfOpenLEFT.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanFull.png")), CHAR_SIZE),  
    ],
    "right": [
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthOpen.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanMouthHalfOpen.png")), CHAR_SIZE),
        scale_sprite(pygame.image.load(os.path.join(sprites_path, "PacmanFull.png")), CHAR_SIZE), 
    ],
}

enemy_sprites = {
    "up": pygame.transform.scale(pygame.image.load(os.path.join(sprites_path, "GhostUp.png")), (CHAR_SIZE, CHAR_SIZE)),
    "down": pygame.transform.scale(pygame.image.load(os.path.join(sprites_path, "GhostDown.png")), (CHAR_SIZE, CHAR_SIZE)),
    "left": pygame.transform.scale(pygame.image.load(os.path.join(sprites_path, "GhostLeft.png")), (CHAR_SIZE, CHAR_SIZE)),
    "right": pygame.transform.scale(pygame.image.load(os.path.join(sprites_path, "GhostRight.png")), (CHAR_SIZE, CHAR_SIZE))
}

# Richtung des Gegners für die Animation setzen
def get_enemy_facing(enemy_direction):
    if enemy_direction == (0, -1):
        return "up"
    elif enemy_direction == (0, 1):
        return "down"
    elif enemy_direction == (-1, 0):
        return "left"
    elif enemy_direction == (1, 0):
        return "right"

# Funktion für das Hauptmenü
def main_menu():
    pygame.mixer.quit()  # Mixer stoppen und zurücksetzen
    pygame.mixer.init()  # Mixer neu initialisieren
    pygame.mixer.music.load(os.path.join(music_path, "lobbymusic.mp3"))
    pygame.mixer.music.play(-1, 0.0)  # Starte die Musik

    # Prozentsatz für die Skalierung der Schrift und Buttons
    scale_percent_title = 0.2  
    scale_percent_button = 0.05  
    scale_percent_button_text = 0.05  
    scale_percent_checkbox = 0.02

    # Berechne die neue Schriftgröße basierend auf dem Prozentsatz der Bildschirmhöhe für den Titel
    font_size_title = int(screen_height * scale_percent_title)

    # Berechne die Button-Größen basierend auf dem Prozentsatz der Bildschirmgröße
    button_width = int(screen_width * 0.17)  
    button_height = int(screen_height * scale_percent_button)  

    # Berechne die Schriftgröße auf den Buttons basierend auf der Bildschirmhöhe
    font_size_button_text = int(screen_height * scale_percent_button_text)

    # Positionen der Buttons (Prozentual zur Bildschirmgröße)
    title_pos = (screen_width // 2, screen_height // 12)  
    play_button_pos = (screen_width // 2, screen_height * 0.548)  
    quit_button_pos = (screen_width // 2, screen_height * 0.609)  
    gamba_button_pos = (screen_width // 2, screen_height * 0.86) 

    # Position der Checkbox und des Textes
    checkbox_pos = (screen_width * 0.02, screen_height * 0.95)
    checkbox_width = int(screen_width * scale_percent_checkbox)
    checkbox_height = int(screen_height * scale_percent_checkbox)
    pacman_text_pos = (checkbox_pos[0] + checkbox_width + 5, checkbox_pos[1])

    # Initialer Zustand der Checkbox (False = aus)
    pacman_checkbox = False

    menu_running = True
    while menu_running:
        screen.fill(BLACK)
        background = pygame.image.load(os.path.join(directory, "ghggh.png"))
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(background, (x_pos, y_pos))

        # Schriftart für den Titel
        font_title = pygame.font.Font(None, font_size_title)
        title_text = font_title.render("Skibidi Fortnite 2", True, WHITE)
        screen.blit(title_text, (title_pos[0] - title_text.get_width() // 2, title_pos[1] - title_text.get_height() // 2))

        # Berechnung der Button-Positionen und -Größen
        play_button = pygame.Rect(play_button_pos[0] - button_width // 2, play_button_pos[1], button_width, button_height)
        quit_button = pygame.Rect(quit_button_pos[0] - button_width // 2, quit_button_pos[1], button_width, button_height)
        gamba_button = pygame.Rect(gamba_button_pos[0] - button_width // 2, gamba_button_pos[1], button_width, button_height)

        # Buttons zeichnen
        pygame.draw.rect(screen, GREEN, play_button)
        pygame.draw.rect(screen, RED, quit_button)
        pygame.draw.rect(screen, YELLOW, gamba_button)

        # Schriftart für die Buttons
        font_button_text = pygame.font.Font(None, font_size_button_text)  # Kleinere Schrift für Buttons
        play_text = font_button_text.render("Play", True, BLACK)
        quit_text = font_button_text.render("End", True, BLACK)
        gamba_text = font_button_text.render("Gamba", True, BLACK)

        # Texte auf die Buttons setzen (zentriert)
        screen.blit(play_text, (play_button.centerx - play_text.get_width() // 2, play_button.centery - play_text.get_height() // 2))
        screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))
        screen.blit(gamba_text, (gamba_button.centerx - gamba_text.get_width() // 2, gamba_button.centery - gamba_text.get_height() // 2))

        # Zeichnen der Checkbox (ein Rechteck)
        pygame.draw.rect(screen, WHITE, (checkbox_pos[0], checkbox_pos[1], checkbox_width, checkbox_height), 2)  # Rahmen der Checkbox
        if pacman_checkbox:  # Checkbox angekreuzt
            pygame.draw.rect(screen, GREEN, (checkbox_pos[0] + 3, checkbox_pos[1] + 3, checkbox_width - 6, checkbox_height - 6))

        # Text neben der Checkbox
        font_checkbox_text = pygame.font.Font(None, int(screen_height * 0.03))  # Kleinere Schrift für den Text
        pacman_text = font_checkbox_text.render("Pacman Must Die", True, WHITE)
        screen.blit(pacman_text, pacman_text_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Überprüfen, ob auf die Checkbox geklickt wurde
                if pygame.Rect(checkbox_pos[0], checkbox_pos[1], checkbox_width, checkbox_height).collidepoint(event.pos):
                    pacman_checkbox = not pacman_checkbox  # Zustand der Checkbox umschalten
                
                if play_button.collidepoint(event.pos):
                    pygame.mixer.music.stop()  
                    # Überprüfen, ob der schwere Modus aktiviert ist
                    if pacman_checkbox:
                        return "play_hard"  # Schwierigkeitsgrad schwer
                    else:
                        return "play"  # Normaler Schwierigkeitsgrad
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if gamba_button.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    return "gamba"

def reset_ghosts():
    """Setze die Geister auf ihre ursprüngliche Position und Modus zurück."""
    for enemy in enemies:
        enemy["pos"] = enemy["initial_pos"]  
        enemy["mode"] = "normal"  

def reset_game():
    """Setzt alle Spielfunktionen und Variablen zurück."""
    global pacman_pos, pacman_speed, current_score, game_over, game_won, enemies

    # Pacman zurücksetzen
    pacman_pos = [9, 1]
    pacman_speed = [0, 0]
    game_over = False
    game_won = False
    current_score = 0

    # Level zurücksetzen 
    level = [
        [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
        for row in MAP
    ]
    
    # Geister zurücksetzen
    reset_ghosts()

    # Musik und andere Spielzustände zurücksetzen
    pygame.mixer.music.load(os.path.join(music_path, "gamemusic.mp3"))
    pygame.mixer.music.play(-1, 0.0)  

def reset_game_hard():
    global pacman_pos, pacman_speed, enemies, level, current_score, total_score, camera

    # Reset Pacman's position and speed
    pacman_pos = [18, 18]
    pacman_speed = [0, 0]
    current_score = 0

    # Reset enemies positions and modes
    enemies = [
        {"pos": [1, 1], "initial_pos": [1, 1], "mode": 'chase', "color": RED},
        {"pos": [35, 1], "initial_pos": [35, 1], "mode": 'chase', "color": RED},
        {"pos": [1, 38], "initial_pos": [1, 38], "mode": 'chase', "color": RED},
        {"pos": [35, 38], "initial_pos": [35, 38], "mode": 'chase', "color": RED},
        {"pos": [5, 18], "initial_pos": [5, 18], "mode": 'ambush', "color": RED},
        {"pos": [31, 18], "initial_pos": [31, 18], "mode": 'ambush', "color": RED},
        {"pos": [18, 5], "initial_pos": [18, 5], "mode": 'scatter', "color": RED},
        {"pos": [18, 34], "initial_pos": [18, 34], "mode": 'scatter', "color": RED},
    ]

    # Reset the level based on the original MAP_HARD and ensure the dots are back
    level = [
        [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
        for row in MAP_HARD
    ]

    # Recalculate the total score based on the number of dots (1s) in the level
    total_score = sum([row.count(1) for row in level])

    # Reset the camera
    map_width = len(level[0]) * CHAR_SIZE
    map_height = len(level) * CHAR_SIZE
    camera = Camera(screen_width, screen_height, map_width, map_height)

    # Reset game music
    pygame.mixer.music.load(os.path.join(music_path, "gamemusic_hard.mp3"))
    pygame.mixer.music.play(-1, 0.0)

def win_screen():
    global game_state
    game_state = GAME_STOP

    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, "win.mp3"))
    pygame.mixer.music.play(0, 0.0)

    # Prozentsätze für Skalierung
    scale_percent_text = 0.19
    scale_percent_button = 0.05
    scale_percent_button_text = 0.05

    # Hintergrundbilder laden und skalieren
    ow_image = pygame.image.load(os.path.join(directory, "ow.png"))
    ow_image = pygame.transform.scale(ow_image, (screen_width, screen_height))
    
    win_image = os.path.join(directory, "win.png")
    win_image = pygame.image.load(win_image)
    win_image = pygame.transform.scale(win_image, (WIDTH, HEIGHT))

    screen.blit(ow_image, (0, 0))  # Blit the ow.png image to cover the screen
    screen.blit(win_image, (x_pos, y_pos))  

    # Schriftgröße für den Siegestext berechnen
    font_size_text = int(screen_height * scale_percent_text)
    font = pygame.font.Font(None, font_size_text)
    text = font.render("VICTORY!", True, YELLOW)
    
    text_x = screen_width // 2 - text.get_width() // 2
    text_y = screen_height * 0.42
    screen.blit(text, (text_x, text_y))

    # Button-Größen berechnen
    button_width = int(screen_width * 0.17)
    button_height = int(screen_height * scale_percent_button)

    # Button-Positionen berechnen
    restart_button_pos = (screen_width // 2, screen_height * 0.579)
    quit_button_pos = (screen_width // 2, screen_height * 0.64)

    # Buttons erstellen
    restart_button = pygame.Rect(restart_button_pos[0] - button_width // 2, restart_button_pos[1], button_width, button_height)
    quit_button = pygame.Rect(quit_button_pos[0] - button_width // 2, quit_button_pos[1], button_width, button_height)

    pygame.draw.rect(screen, GREEN, restart_button)
    pygame.draw.rect(screen, RED, quit_button)

    # Schriftgröße für die Buttons berechnen
    font_size_button_text = int(screen_height * scale_percent_button_text)
    font_small = pygame.font.Font(None, font_size_button_text)
    restart_text = font_small.render("Restart", True, BLACK)
    quit_text = font_small.render("Quit", True, BLACK)

    # Texte auf die Buttons setzen (zentriert)
    screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_state = GAME_RUNNING
                    reset_game()
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    return "menu"

def end_screen():
    global game_state
    game_state = GAME_STOP

    # Stoppe die aktuelle Musik und lade die neue Musik
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, "end.mp3"))
    pygame.mixer.music.play(0, 0.0)

    # Lade das Video
    video_path = os.path.join(directory, "end.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Fehler: Video konnte nicht geladen werden.")
        return

    # Prozentsätze für Skalierung
    scale_percent_text = 0.14
    scale_percent_button = 0.05
    scale_percent_button_text = 0.05

    # Schriftgröße für den Siegestext berechnen
    font_size_text = int(screen_height * scale_percent_text)
    font = pygame.font.Font(None, font_size_text)
    text = font.render("end", True, WHITE)
    
    text_x = screen_width // 2 - text.get_width() // 2
    text_y = screen_height * 0.42

    # Button-Größen berechnen
    button_width = int(screen_width * 0.17)
    button_height = int(screen_height * scale_percent_button)

    # Button-Positionen berechnen
    restart_button_pos = (screen_width // 2, screen_height * 0.868)
    quit_button_pos = (screen_width // 2, screen_height * 0.929)

    # Buttons erstellen
    restart_button = pygame.Rect(restart_button_pos[0] - button_width // 2, restart_button_pos[1], button_width, button_height)
    quit_button = pygame.Rect(quit_button_pos[0] - button_width // 2, quit_button_pos[1], button_width, button_height)

    # Hauptloop für das Abspielen des Videos
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Konvertiere das OpenCV-Bild in ein Pygame-Bild
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
        frame = pygame.transform.scale(frame, (screen_width, screen_height))

        # Zeichne das Video auf den Bildschirm
        screen.blit(frame, (0, 0))

        # Zeichne den Text und die Buttons
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, GREEN, restart_button)
        pygame.draw.rect(screen, RED, quit_button)

        # Schriftgröße für die Buttons berechnen
        font_size_button_text = int(screen_height * scale_percent_button_text)
        font_small = pygame.font.Font(None, font_size_button_text)
        restart_text = font_small.render("Restart", True, BLACK)
        quit_text = font_small.render("Quit", True, BLACK)

        # Texte auf die Buttons setzen (zentriert)
        screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
        screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_state = GAME_RUNNING
                    cap.release()
                    reset_game_hard()
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    cap.release()
                    return "menu"

        pygame.time.delay(30)  # Kontrolliere die Abspielgeschwindigkeit des Videos

    cap.release()
    return "menu"

def load_gif_frames(gif_path):
    """Lädt GIF-Frames als Pygame-Surfaces."""
    gif = imageio.mimread(gif_path)  # Alle Frames laden
    frames = []
    
    for frame in gif:
        # Wandle numpy array in Pygame Surface um
        frame = np.array(frame)
        
        # Überprüfe die Anzahl der Kanäle und konvertiere in RGB falls notwendig
        if len(frame.shape) == 2:  # Grayscale (2D array)
            frame = np.stack([frame] * 3, axis=-1)  # Erstelle 3 Kanäle aus dem Graustufenbild
        elif frame.shape[2] == 4:  # Wenn es sich um ein RGBA-Bild handelt, entferne den Alpha-Kanal
            frame = frame[:, :, :3]
        
        # Um die Achsen für Pygame auszurichten
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))  # Swap the axes to match Pygame's orientation
        frames.append(surface)
    
    return frames

miku_playing = False  # Variable, um zu überprüfen, ob Miku-Musik schon läuft

def game_over_screen():
    global game_state
    game_state = GAME_STOP
    global miku_playing

    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, "miku.mp3"))
    pygame.mixer.music.play(0, 0.0)

    miku_playing = True

    gif_path = os.path.join(directory, "miku.gif")
    gif_frames = load_gif_frames(gif_path)
    frame_index = 0

    # Prozentsätze für Skalierung
    scale_percent_text = 0.19
    scale_percent_button = 0.05
    scale_percent_button_text = 0.05

    # Schriftgröße für den "Game Over"-Text berechnen
    font_size_text = int(screen_height * scale_percent_text)
    font = pygame.font.Font(None, font_size_text)
    text = font.render("Game Over! :(", True, RED)
    text_x = screen_width // 2 - text.get_width() // 2
    text_y = screen_height * 0.48

    # Button-Größen berechnen
    button_width = int(screen_width * 0.17)
    button_height = int(screen_height * scale_percent_button)

    # Button-Positionen berechnen
    restart_button_pos = (screen_width // 2, screen_height * 0.868)
    quit_button_pos = (screen_width // 2, screen_height * 0.929)

    # Buttons erstellen
    restart_button = pygame.Rect(restart_button_pos[0] - button_width // 2, restart_button_pos[1], button_width, button_height)
    quit_button = pygame.Rect(quit_button_pos[0] - button_width // 2, quit_button_pos[1], button_width, button_height)

    font_size_button_text = int(screen_height * scale_percent_button_text)
    font_small = pygame.font.Font(None, font_size_button_text)
    restart_text = font_small.render("Restart", True, BLACK)
    quit_text = font_small.render("Quit", True, BLACK)

    clock = pygame.time.Clock()

    while True:
        screen.blit(pygame.transform.scale(gif_frames[frame_index], (screen_width, screen_height)), (0, 0))
        screen.blit(text, (text_x, text_y))

        pygame.draw.rect(screen, GREEN, restart_button)
        pygame.draw.rect(screen, RED, quit_button)

        screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
        screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

        pygame.display.flip()
        frame_index = (frame_index + 1) % len(gif_frames)
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_state = GAME_RUNNING
                    reset_game()
                    return "restart"
                if quit_button.collidepoint(event.pos):
                    return "menu"

def game_over_screen_hard():
    global game_state
    game_state = GAME_STOP
    global miku_playing

    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, "miku.mp3"))
    pygame.mixer.music.play(0, 0.0)

    miku_playing = True

    gif_path = os.path.join(directory, "miku.gif")
    gif_frames = load_gif_frames(gif_path)
    frame_index = 0

    # Prozentsätze für Skalierung
    scale_percent_text = 0.19
    scale_percent_button = 0.05
    scale_percent_button_text = 0.05

    # Schriftgröße für den "Game Over"-Text berechnen
    font_size_text = int(screen_height * scale_percent_text)
    font = pygame.font.Font(None, font_size_text)
    text = font.render("Game Over! :(", True, RED)
    text_x = screen_width // 2 - text.get_width() // 2
    text_y = screen_height * 0.48

    # Button-Größen berechnen
    button_width = int(screen_width * 0.17)
    button_height = int(screen_height * scale_percent_button)

    # Button-Positionen berechnen
    restart_button_pos = (screen_width // 2, screen_height * 0.868)
    quit_button_pos = (screen_width // 2, screen_height * 0.929)

    # Buttons erstellen
    restart_button = pygame.Rect(restart_button_pos[0] - button_width // 2, restart_button_pos[1], button_width, button_height)
    quit_button = pygame.Rect(quit_button_pos[0] - button_width // 2, quit_button_pos[1], button_width, button_height)

    font_size_button_text = int(screen_height * scale_percent_button_text)
    font_small = pygame.font.Font(None, font_size_button_text)
    restart_text = font_small.render("Restart", True, BLACK)
    quit_text = font_small.render("Quit", True, BLACK)

    clock = pygame.time.Clock()

    while True:
        screen.blit(pygame.transform.scale(gif_frames[frame_index], (screen_width, screen_height)), (0, 0))
        screen.blit(text, (text_x, text_y))

        pygame.draw.rect(screen, GREEN, restart_button)
        pygame.draw.rect(screen, RED, quit_button)

        screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
        screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

        pygame.display.flip()
        frame_index = (frame_index + 1) % len(gif_frames)
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_state = GAME_RUNNING
                    reset_game_hard()
                    return "restart"
                if quit_button.collidepoint(event.pos):
                    return "menu"

def game_loop():
    global game_state
    global pacman_pos
    global enemies
    clock = pygame.time.Clock()
    running = True
    game_over = False
    game_won = False
    pacman_pos = [9, 1]  
    pacman_speed = [0, 0]
    pacman_direction = "right"

    enemies = [
    {"pos": list(enemy_positions[0]), "initial_pos": list(enemy_positions[0]), "mode": 'chase', "color": RED},  
    {"pos": list(enemy_positions[1]), "initial_pos": list(enemy_positions[1]), "mode": 'scatter', "color": GREEN},  
    {"pos": list(enemy_positions[2]), "initial_pos": list(enemy_positions[2]), "mode": 'ambush', "color": PINK},  
    {"pos": list(enemy_positions[3]), "initial_pos": list(enemy_positions[3]), "mode": 'scatter', "color": BLUE},  
    ]

    level = [
        [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
        for row in MAP]

    pygame.mixer.music.load(os.path.join(music_path, "gamemusic.mp3"))
    pygame.mixer.music.play(-1, 0.0)

    pacman_animation_index = 0
    animation_timer = 0
    animation_delay = 1

    x_pos = (screen_width - WIDTH) // 2
    y_pos = (screen_height - HEIGHT) // 2

    total_score = sum([row.count(1) for row in level])  
    current_score = 0  

    while running:
        if game_state == GAME_RUNNING:  # Nur wenn das Spiel aktiv ist, Gegner bewegen und spielen
            while not game_over and not game_won:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False  
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  
                            pygame.quit()
                            sys.exit() 
                        if event.key in (pygame.K_UP, pygame.K_w):
                            pacman_speed = [0, -1]
                            pacman_direction = "up"
                        if event.key in (pygame.K_DOWN, pygame.K_s):
                            pacman_speed = [0, 1]
                            pacman_direction = "down"
                        if event.key in (pygame.K_LEFT, pygame.K_a):
                            pacman_speed = [-1, 0]
                            pacman_direction = "left"
                        if event.key in (pygame.K_RIGHT, pygame.K_d):
                            pacman_speed = [1, 0]
                            pacman_direction = "right"
                        if event.key == pygame.K_RETURN:  
                            game_won = True  

                # Pacman bewegen
                new_pos = [pacman_pos[0] + pacman_speed[0], pacman_pos[1] + pacman_speed[1]]
                if level[new_pos[1]][new_pos[0]] != 2:
                    pacman_pos = new_pos

                if level[pacman_pos[1]][pacman_pos[0]] == 1:
                    level[pacman_pos[1]][pacman_pos[0]] = 0
                    current_score += 1  

                # Geister bewegen, wenn das Spiel aktiv ist
                if game_state == GAME_RUNNING:  # Verhindert Gegnerbewegungen, wenn das Spiel pausiert
                    pacman_velocity = pacman_speed  # Pacman-Geschwindigkeit wird hier definiert
                    for enemy in enemies:
                        # Übergebe pacman_pos und pacman_velocity an enemy_AI
                        direction = enemy_AI(enemy, pacman_pos, pacman_velocity, mode=enemy["mode"])
                        enemy_new_pos = [enemy["pos"][0] + direction[0], enemy["pos"][1] + direction[1]]
                        if level[enemy_new_pos[1]][enemy_new_pos[0]] != 2:
                            enemy["pos"] = enemy_new_pos

                        if pacman_pos == enemy["pos"]:
                            game_over = True

                # Prüfen, ob alle Punkte gesammelt wurden
                if all(cell != 1 for row in level for cell in row):
                    game_won = True

                # Bildschirm zeichnen
                screen.fill(BLACK)

                for y in range(len(level)):
                    for x in range(len(level[y])):
                        if level[y][x] == 2:
                            pygame.draw.rect(screen, BLUE, (x * CHAR_SIZE + x_pos, y * CHAR_SIZE + y_pos, CHAR_SIZE, CHAR_SIZE))
                        elif level[y][x] == 1:
                            pygame.draw.circle(screen, WHITE, (x * CHAR_SIZE + CHAR_SIZE // 2 + x_pos, y * CHAR_SIZE + CHAR_SIZE // 2 + y_pos), 5)

                # Pacman zeichnen
                animation_timer += 1
                if animation_timer >= animation_delay:
                    pacman_animation_index = (pacman_animation_index + 1) % len(pacman_sprites[pacman_direction])
                    animation_timer = 0

                pacman_sprite = pacman_sprites[pacman_direction][pacman_animation_index]
                screen.blit(pacman_sprite, (pacman_pos[0] * CHAR_SIZE + x_pos, pacman_pos[1] * CHAR_SIZE + y_pos))

                # Gegner zeichnen, nur wenn das Spiel nicht beendet ist
                if not game_over and not game_won:
                    for enemy in enemies:
                        direction = enemy_AI(enemy, pacman_pos, pacman_velocity, mode=enemy["mode"])
                        enemy_facing = get_enemy_facing(direction)
                        screen.blit(enemy_sprites[enemy_facing], (enemy["pos"][0] * CHAR_SIZE + x_pos, enemy["pos"][1] * CHAR_SIZE + y_pos))

                # Punktestand anzeigen
                # Dynamische Schriftgröße basierend auf Bildschirmhöhe
                font_size = int(screen_height * 0.07)  
                font = pygame.font.Font(None, font_size)

                # Punktestand-Text
                score_text = f"{current_score} / {total_score}"
                score_surface = font.render(score_text, True, WHITE)

                # Position relativ zum Bildschirm
                score_x = screen_width * 0.5  
                score_y = screen_height * 0.9

                # Rechteck mit neuer Position
                score_rect = score_surface.get_rect(center=(score_x, score_y))

                # Auf den Bildschirm zeichnen
                screen.blit(score_surface, score_rect)


                # Game Over oder Win Screen einblenden
                if game_over:
                    result = game_over_screen()
                    if result == "restart":
                        game_over = False
                        game_won = False
                        pacman_pos = [9, 1]
                        pacman_speed = [0, 0]
                        level = [
                            [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
                            for row in MAP]
                        current_score = 0  
                        pygame.mixer.music.load(os.path.join(music_path, "gamemusic.mp3"))
                        pygame.mixer.music.play(-1, 0.0)  
                        break
                    elif result == "menu":
                        running = False
                        return "menu"

                elif game_won:
                    result = win_screen()
                    if result == "restart":
                        game_over = False
                        game_won = False
                        pacman_pos = [9, 1]
                        pacman_speed = [0, 0]
                        level = [
                            [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
                            for row in MAP]
                        current_score = 0  
                        pygame.mixer.music.load(os.path.join(music_path, "gamemusic.mp3"))
                        pygame.mixer.music.play(-1, 0.0)  
                        break
                    elif result == "menu":
                        running = False
                        return "menu"

                pygame.display.flip()
                clock.tick(6)

class Camera:
    def __init__(self, screen_width, screen_height, map_width, map_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target_rect):
        # Berechne die Kamera-Position, um das Ziel (Pacman) zu zentrieren
        self.offset_x = target_rect.x - self.screen_width // 2
        self.offset_y = target_rect.y - self.screen_height // 2

        # Begrenze die Kamera-Position, um nicht über den Rand der Map hinaus zu gehen
        self.offset_x = max(0, min(self.offset_x, self.map_width - self.screen_width))
        self.offset_x = self.offset_x + (self.map_width - self.screen_width) // 2
        self.offset_y = max(0, min(self.offset_y, self.map_height - self.screen_height))

    def apply(self, rect):
        # Verschiebe das Rechteck um die Kamera-Position
        return rect.move(-self.offset_x, -self.offset_y)

    def apply_point(self, point):
        # Verschiebe den Punkt um die Kamera-Position
        return (point[0] - self.offset_x, point[1] - self.offset_y)

def game_loop_hard():
    global game_state
    global pacman_pos
    global enemies

    while True:  # Hauptschleife für den Neustart
        clock = pygame.time.Clock()
        running = True
        game_over = False
        game_won = False
        pacman_pos = [18, 18]  
        pacman_speed = [0, 0]
        pacman_direction = "down"  
        current_score = 0

        enemies = [
            {"pos": [1, 1], "initial_pos": [1, 1], "mode": 'chase', "color": RED},
            {"pos": [35, 1], "initial_pos": [35, 1], "mode": 'chase', "color": RED},
            {"pos": [1, 38], "initial_pos": [1, 38], "mode": 'chase', "color": RED},
            {"pos": [35, 38], "initial_pos": [35, 38], "mode": 'chase', "color": RED},
            {"pos": [5, 18], "initial_pos": [5, 18], "mode": 'ambush', "color": RED},
            {"pos": [31, 18], "initial_pos": [31, 18], "mode": 'ambush', "color": RED},
            {"pos": [18, 5], "initial_pos": [18, 5], "mode": 'scatter', "color": RED},
            {"pos": [18, 34], "initial_pos": [18, 34], "mode": 'scatter', "color": RED},
        ]

        level = [
            [2 if cell == '1' else 1 if cell == ' ' else 0 for cell in row]
            for row in MAP_HARD
        ]

        map_width = len(level[0]) * CHAR_SIZE
        map_height = len(level) * CHAR_SIZE

        # Kamera erstellen
        camera = Camera(screen_width, screen_height, map_width, map_height)
        
        # Musikdateien
        music_tracks = ["gamemusic_hard.mp3", "gamemusic_hard2.mp3", "gamemusic_hard3.mp3", "gamemusic_hard4.mp3", "gamemusic_hard5.mp3", "gamemusic_hard6.mp3", "gamemusic_hard7.mp3", "gamemusic_hard8.mp3", "gamemusic_hard9.mp3", "gamemusic_hard10.mp3"]
        current_track = 0  # Start mit case1.mp3

        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join(music_path, music_tracks[current_track]))
        pygame.mixer.music.play(-1, 0.0)

        #pygame.mixer.music.load(os.path.join(music_path, "gamemusic_hard.mp3"))
        #pygame.mixer.music.play(-1, 0.0)

        pacman_animation_index = 0
        animation_timer = 0
        animation_delay = 1

        total_score = sum([row.count(1) for row in level])  

        while running:
            if game_state == GAME_RUNNING:  
                while not game_over and not game_won:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit() 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:  
                                pygame.quit()
                                sys.exit() 
                            if event.key in (pygame.K_UP, pygame.K_w):
                                pacman_speed = [0, -1]
                                pacman_direction = "up"
                            if event.key in (pygame.K_DOWN, pygame.K_s):
                                pacman_speed = [0, 1]
                                pacman_direction = "down"
                            if event.key in (pygame.K_LEFT, pygame.K_a):
                                pacman_speed = [-1, 0]
                                pacman_direction = "left"
                            if event.key in (pygame.K_RIGHT, pygame.K_d):
                                pacman_speed = [1, 0]
                                pacman_direction = "right"
                            if event.key == pygame.K_RETURN:  
                                game_won = True
                            if event.key == pygame.K_1:  # Musik mit Taste 1 wechseln
                                current_track = (current_track + 1) % len(music_tracks)  # Nächstes Lied wählen
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load(os.path.join(music_path, music_tracks[current_track]))
                                pygame.mixer.music.play(-1, 0.0)  # Endlos abspielen  

                    # Pacman bewegen
                    new_pos = [pacman_pos[0] + pacman_speed[0], pacman_pos[1] + pacman_speed[1]]
                    if level[new_pos[1]][new_pos[0]] != 2:
                        pacman_pos = new_pos

                    if level[pacman_pos[1]][pacman_pos[0]] == 1:
                        level[pacman_pos[1]][pacman_pos[0]] = 0
                        current_score += 1  

                    pacman_rect = pygame.Rect(
                        pacman_pos[0] * CHAR_SIZE, 
                        pacman_pos[1] * CHAR_SIZE, 
                        CHAR_SIZE, CHAR_SIZE
                    )
                    camera.update(pacman_rect)  

                    # Geister bewegen
                    if game_state == GAME_RUNNING:
                        pacman_velocity = pacman_speed  
                        for enemy in enemies:
                            direction = enemy_AI(enemy, pacman_pos, pacman_velocity, mode=enemy["mode"])
                            enemy_new_pos = [enemy["pos"][0] + direction[0], enemy["pos"][1] + direction[1]]
                            if level[enemy_new_pos[1]][enemy_new_pos[0]] != 2:
                                enemy["pos"] = enemy_new_pos

                            if pacman_pos == enemy["pos"]:
                                game_over = True

                    # Prüfen, ob alle Punkte gesammelt wurden
                    if all(cell != 1 for row in level for cell in row):
                        game_won = True

                    # Bildschirm zeichnen
                    screen.fill(BLACK)

                    # Map zeichnen
                    for y in range(len(level)):
                        for x in range(len(level[y])):
                            tile_rect = pygame.Rect(
                                x * CHAR_SIZE, 
                                y * CHAR_SIZE, 
                                CHAR_SIZE, CHAR_SIZE
                            )
                            if level[y][x] == 2:
                                pygame.draw.rect(screen, RED, camera.apply(tile_rect))
                            elif level[y][x] == 1:
                                dot_pos = (
                                    x * CHAR_SIZE + CHAR_SIZE // 2, 
                                    y * CHAR_SIZE + CHAR_SIZE // 2
                                )
                                pygame.draw.circle(screen, WHITE, camera.apply_point(dot_pos), 5)

                    # Pacman zeichnen
                    animation_timer += 1
                    if animation_timer >= animation_delay:
                        pacman_animation_index = (pacman_animation_index + 1) % len(pacman_sprites[pacman_direction])
                        animation_timer = 0

                    pacman_sprite = pacman_sprites[pacman_direction][pacman_animation_index]
                    screen.blit(pacman_sprite, camera.apply(pacman_rect))

                    # Gegner zeichnen
                    if not game_over and not game_won:
                        for enemy in enemies:
                            direction = enemy_AI(enemy, pacman_pos, pacman_speed, mode=enemy["mode"])
                            enemy_facing = get_enemy_facing(direction)
                            enemy_rect = pygame.Rect(
                                enemy["pos"][0] * CHAR_SIZE, 
                                enemy["pos"][1] * CHAR_SIZE, 
                                CHAR_SIZE, CHAR_SIZE
                            )
                            screen.blit(enemy_sprites[enemy_facing], camera.apply(enemy_rect))

                    # Punktestand anzeigen
                    font_size = int(screen_height * 0.07)  
                    font = pygame.font.Font(None, font_size)

                    score_text = f"{current_score} / {total_score}"
                    score_surface = font.render(score_text, True, WHITE)

                    score_x = screen_width * 0.5  
                    score_y = screen_height * 0.9

                    score_rect = score_surface.get_rect(center=(score_x, score_y))
                    screen.blit(score_surface, score_rect)

                    # Game Over oder Win Screen einblenden
                    if game_over:
                        result = game_over_screen_hard()
                        if result == "restart":
                            break  # Verlasse die innere Schleife, um die äußere Schleife neu zu starten
                        elif result == "menu":
                            return "menu"  # Zurück zum Hauptmenü

                    elif game_won:
                        result = end_screen()
                        if result == "restart":
                            break  # Verlasse die innere Schleife, um die äußere Schleife neu zu starten
                        elif result == "menu":
                            return "menu"  # Zurück zum Hauptmenü

                    pygame.display.flip()
                    clock.tick(7)

                if game_over or game_won:
                    break  # Verlasse die innere Schleife, um die äußere Schleife neu zu starten      


#--------------------------------------------------------------------------------------------------------------------------


# Neue Seltenheiten und Wahrscheinlichkeiten
ITEMS = [
    ("Blue", (0, 0, 255), 0.7992),
    ("Purple", (128, 0, 128), 0.1598),
    ("Pink", (255, 105, 180), 0.032),
    ("Red", (255, 0, 0), 0.0064),
    ("Gold", (255, 215, 0), 0.0026),
]

SPIN_SPEED = 15
SPIN_DURATION = 3

def get_random_item():
    rand = random.random()
    cumulative = 0
    for item, color, chance in ITEMS:
        cumulative += chance
        if rand <= cumulative:
            return (item, color)  # Nur Name und Farbe zurückgeben
    return ITEMS[0][:2]  # Falls kein Treffer, den ersten Eintrag ohne Wahrscheinlichkeit zurückgeben

def cscase():
    global game_state
    running = True
    won_item = None
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, int(screen_height * 0.05))
    item_size = int(screen_height * 0.11)

    # Hintergrundbild laden
    background_image = pygame.image.load(os.path.join(directory, "case.png"))
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Musikdateien
    music_tracks = ["case1.mp3", "case2.mp3", "case3.mp3"]
    current_track = 0  # Start mit case1.mp3

    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_path, music_tracks[current_track]))
    pygame.mixer.music.play(-1, 0.0)

    spin_music = pygame.mixer.Sound(os.path.join(music_path, "spin.mp3"))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Spiel wirklich beenden

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # SPACE -> NEUE CASE
                    spin_music.play()
                    won_item = spin_animation()

                if event.key == pygame.K_q:  # "Q" -> Zurück zum Hauptmenü
                    pygame.mixer.music.stop()
                    running = False  # Beende die Schleife
                    return  # Verlasse die Funktion sauber, ohne pygame zu beenden

                if event.key == pygame.K_1:  # Musik mit Taste 1 wechseln
                    current_track = (current_track + 1) % len(music_tracks)  # Nächstes Lied wählen
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(music_path, music_tracks[current_track]))
                    pygame.mixer.music.play(-1, 0.0)  # Endlos abspielen

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))
        text = font.render("SPACE - open Case", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 105))
        text = font.render("Q - back", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 70))
        text = font.render("ESC - quit", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 35))
        text = font.render("1 - music", True, (255, 255, 255))
        screen.blit(text, (screen_width // 14 - text.get_width() // 2, screen_height - 35))

        if won_item:
            name, color = won_item
            rect_size = int(screen_height * 0.1)
            pygame.draw.rect(screen, color, (screen_width // 2 - item_size // 2, screen_height // 2 - item_size // 2, item_size, item_size))
            text = font.render(f"Won: {name}", True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 14 + rect_size))

        pygame.display.flip()
        clock.tick(30)

def spin_animation():
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    line_length = screen_height * 0.077

    spinning = True
    start_time = time.time()
    items = [get_random_item() for _ in range(7)]
    clock = pygame.time.Clock()

    initial_spin_speed = 50
    max_spin_duration = 5

    background_image = pygame.image.load(os.path.join(directory, "case.png"))
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    center_x = screen_width // 2
    center_y = screen_height // 2
    item_size = int(screen_height * 0.11)
    item_spacing = int(screen_width * 0.066)
    total_items = len(items)

    while spinning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Nur hier das Spiel beenden, falls gewünscht

        screen.blit(background_image, (0, 0))

        for i, (name, color) in enumerate(items):
            x_pos = center_x - (len(items) // 2) * item_spacing + i * item_spacing - item_size // 2
            pygame.draw.rect(screen, color, (x_pos, center_y - item_size // 2, item_size, item_size))

        pygame.draw.line(screen, (255, 203, 83), (center_x, center_y - line_length), (center_x, center_y + line_length), 3)
        pygame.display.flip()

        elapsed_time = time.time() - start_time
        if elapsed_time < max_spin_duration:
            speed_decrease_factor = elapsed_time / max_spin_duration
            current_spin_speed = initial_spin_speed * (1 - speed_decrease_factor)
        else:
            current_spin_speed = 0

        clock.tick(max(current_spin_speed, 10))
        items.append(get_random_item())
        items.pop(0)

        if elapsed_time >= max_spin_duration:
            spinning = False

    time.sleep(1)
    winner_index = (total_items // 2) - 1
    winner = items[winner_index]
    return winner

# Hauptmenü starten
while True:  # Endlosschleife für das Hauptmenü
    menu_choice = main_menu()  # Starte das Menü
    if menu_choice == "play":
        game_state = GAME_RUNNING
        result = game_loop()  # Starte das Spiel
        if result == "menu":
            continue  # Zurück ins Menü
    elif menu_choice == "gamba":
        cscase()  # GAMBA
    elif menu_choice == "play_hard":
        game_state = GAME_RUNNING
        result = game_loop_hard()  # Starte das Spiel
        if result == "menu":
            continue  # Zurück ins Menü

pygame.quit()
sys.exit()
