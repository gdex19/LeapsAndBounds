import arcade
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
STATIONARY_SPEED = 5
ROCK_WIDTH = 160
ROCK_HEIGHT = 155
ROCK_SCALE = 0.6
GRASS_TOP = 94


class Rocks(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Rock Pile.png", ROCK_SCALE)
        self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)
        self.center_y = GRASS_TOP + ROCK_HEIGHT * ROCK_SCALE / 2
        self.change_x = -STATIONARY_SPEED

    def update(self):
        super().update()
        if self.left <= -ROCK_WIDTH:
            print("hello")
            self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)
