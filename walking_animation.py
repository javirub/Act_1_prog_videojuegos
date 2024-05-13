import pygame
import sys
from game_objects.character import Character
from utils.constants import *

# Initialize Pygame
pygame.init()

# Set up the display

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Walking Animation")
# Set up the clock
clock = pygame.time.Clock()
# Set up the character
character = Character((WIDTH // 2, HEIGHT - 100))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update
    character.update()

    # Draw
    SCREEN.fill((0, 0, 0))
    character.draw(SCREEN)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)


pygame.quit()
sys.exit()
