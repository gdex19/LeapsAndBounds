import arcade
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
STATIONARY_SPEED = 5
ROCK_WIDTH = 160
ROCK_HEIGHT = 155
ROCK_SCALE = 0.5
GRASS_TOP = 94
ROCKET_SPEED = 10
ROCKET_WIDTH = 1080
ROCKET_HEIGHT = 557
ROCKET_SCALE = 0.1
PLAYER_HEIGHT = 383
PLAYER_SCALE = 0.28


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
