import arcade
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
ROCKET_SPEED = 10
ROCKET_WIDTH = 1080
ROCKET_HEIGHT = 557
ROCKET_SCALE = 0.1
GRASS_TOP = 94
PLAYER_HEIGHT = 383
PLAYER_SCALE = 0.28


class Rockets(arcade.Sprite):
    def __init__(self):
        super().__init__("images/rocket.png", ROCKET_SCALE)
        self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
        self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                   int(PLAYER_HEIGHT * PLAYER_SCALE + ROCKET_HEIGHT * ROCKET_SCALE))
        self.change_x = -ROCKET_SPEED

    def update(self):
        super().update()
        if self.left <= -ROCKET_WIDTH * ROCKET_SCALE:
            self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
            self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                       int(PLAYER_HEIGHT * PLAYER_SCALE + ROCKET_HEIGHT * ROCKET_SCALE))
