from utils.sprites import load_sprite_sheet
from utils.constants import WIDTH, WALKING_ANIMATION_PATH


class Letter:
    def __init__(self, position, image):
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.speed = 4

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed
