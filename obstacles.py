import arcade
import random

from constants import ROCKET_SCALE, ROCKET_HEIGHT, WINDOW_WIDTH, PLAYER_SCALE, GRASS_TOP, ROCKET_WIDTH, PLAYER_HEIGHT, \
    ROCKET_SPEED, ROCK_WIDTH, STATIONARY_SPEED, ROCK_HEIGHT, ROCK_SCALE


class Rocks(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Rock Pile.png", ROCK_SCALE)
        self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)
        self.center_y = GRASS_TOP + ROCK_HEIGHT * ROCK_SCALE / 2
        self.change_x = -STATIONARY_SPEED

    def update(self):
        super().update()
        if self.left <= -ROCK_WIDTH:
            self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)


class Rockets(arcade.Sprite):
    def __init__(self):
        super().__init__("images/rocket.png", ROCKET_SCALE)
        self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
        self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                   int(PLAYER_HEIGHT * PLAYER_SCALE + ROCKET_HEIGHT * ROCKET_SCALE / 2))
        self.change_x = -ROCKET_SPEED

    def update(self):
        super().update()
        if self.left <= -ROCKET_WIDTH * ROCKET_SCALE:
            self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
            self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                       int(PLAYER_HEIGHT * PLAYER_SCALE +
                                                           ROCKET_HEIGHT * ROCKET_SCALE / 2))
