from utils.sprites import load_sprite_sheet
from utils.constants import WIDTH, WALKING_ANIMATION_PATH


class Character:
    def __init__(self, position):
        self.sprites = load_sprite_sheet(WALKING_ANIMATION_PATH, 10, 2)
        self.right_sprites = self.sprites[1:10]
        self.left_sprites = self.sprites[11:]
        self.current_sprite_index = 0
        self.image = self.sprites[self.current_sprite_index]
        self.rect = self.image.get_rect(center=position)
        self.speed = 4
        self.moving_right = True
        self.moving_left = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.x <= 0:
            self.moving_right = True
            self.moving_left = False
        elif self.rect.x >= WIDTH - 50:
            self.moving_left = True
            self.moving_right = False

        if self.moving_right:
            self.rect.x += self.speed
        elif self.moving_left:
            self.rect.x -= self.speed
        else:
            self.current_sprite_index = 0
        self.update_sprite()

    def update_sprite(self):
        self.current_sprite_index += 1
        if self.moving_right:
            if self.current_sprite_index >= len(self.right_sprites):
                self.current_sprite_index = 0
            self.image = self.right_sprites[self.current_sprite_index]
        elif self.moving_left:
            if self.current_sprite_index >= len(self.left_sprites):
                self.current_sprite_index = 0
            self.image = self.left_sprites[self.current_sprite_index]



