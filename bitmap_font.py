import pygame
import sys
from game_objects.letters import Letter
from utils.constants import *
from utils.sprites import load_sprite_sheet
from tkinter import simpledialog


def letter_to_index(character):
    if letter == " ":
        return 0
    if character.isalpha() and len(character) == 1:
        return ord(character.lower()) - 96
    else:
        return None


# Ask the user for the text to display
user_input = simpledialog.askstring(title="Bitmap Text", prompt="Enter the text to display:")
if user_input is None or user_input == "":
    user_input = "Por favor ponme buena nota"

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bitmap Text")

# Create an empty list to store the letters objects
text = []

# Save the letters images dictionary
LETTERS = load_sprite_sheet(BITMAP_FONT, 10, 6)[32:]

# Create the letters objects
for letter in user_input:
    index = letter_to_index(letter)
    if index is not None:
        text.append(Letter((WIDTH, HEIGHT // 2), LETTERS[index]))

# Set up the clock
clock = pygame.time.Clock()

displaying_text = []
counter = 0
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
    if text and counter % 10 == 0:
        displaying_text.append(text.pop(0))
        counter = 0
    counter += 1
    # Draw
    SCREEN.fill((0, 0, 0))
    for letter in displaying_text:
        if letter.rect.x < -100:
            displaying_text.remove(letter)
        letter.update()
        letter.draw(SCREEN)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
