import arcade
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
GRASS_TOP = 94
FISH_SCALE = 0.15
FISH_HEIGHT = 200
FISH_WIDTH = 240
FISH_SPEED = 5


class Fish(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Fish.png", FISH_SCALE)
        self.center_x = random.randint(FISH_SCALE * FISH_WIDTH / 2, WINDOW_WIDTH - FISH_SCALE * FISH_WIDTH / 2)
        self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT / 2, WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)
        self.change_y = -FISH_SPEED

    def update(self):
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = random.randint(FISH_SCALE * FISH_WIDTH / 2, WINDOW_WIDTH - FISH_SCALE * FISH_WIDTH / 2)
            self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT / 2,
                                                           WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)







