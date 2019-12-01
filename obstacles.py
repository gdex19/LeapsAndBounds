import arcade
import random

from constants import ROCKET_SCALE, ROCKET_HEIGHT, WINDOW_WIDTH, PLAYER_SCALE, GRASS_TOP, ROCKET_WIDTH, \
    ROCKET_SPEED, ROCK_WIDTH, ROCK_HEIGHT, ROCK_SCALE, BACKGROUND_SPEED, METEOR_SCALE, SCROLL_SPEED, \
    WINDOW_HEIGHT, METEOR_SPEED, PLAYER_HEAD


class Rocks(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Rock Pile.png", ROCK_SCALE)
        self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)
        self.center_y = GRASS_TOP + ROCK_HEIGHT * ROCK_SCALE / 2
        self.change_x = -BACKGROUND_SPEED * ObstacleTimer.speed

    def update(self):
        super().update()
        if self.left <= -ROCK_WIDTH:
            self.center_x = WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)
        self.change_x = -BACKGROUND_SPEED * ObstacleTimer.speed


class Rockets(arcade.Sprite):
    def __init__(self):
        super().__init__("images/rocket.png", ROCKET_SCALE)
        self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
        self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                   int(PLAYER_HEAD * PLAYER_SCALE * 2 + ROCKET_HEIGHT * ROCKET_SCALE / 2))
        self.change_x = -ROCKET_SPEED * ObstacleTimer.speed

    def update(self):
        super().update()
        if self.left <= -ROCKET_WIDTH * ROCKET_SCALE:
            self.center_x = (WINDOW_WIDTH + random.randint(WINDOW_WIDTH / 12, WINDOW_WIDTH)) * 2
            self.center_y = GRASS_TOP + random.randint(int(ROCKET_HEIGHT * ROCKET_SCALE / 2),
                                                       int(PLAYER_HEAD * PLAYER_SCALE +
                                                           ROCKET_HEIGHT * ROCKET_SCALE / 2))
        self.change_x = -ROCKET_SPEED * ObstacleTimer.speed


class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Meteor.png", METEOR_SCALE)
        self.center_x = random.randint(WINDOW_WIDTH * 1.5, WINDOW_WIDTH * 2.5)
        self.center_y = WINDOW_HEIGHT + random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 4)
        self.change_y = -METEOR_SPEED * ObstacleTimer.speed
        self.change_x = -SCROLL_SPEED * ObstacleTimer.speed

    def update(self):
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = random.randint(WINDOW_WIDTH * 1.5, WINDOW_WIDTH * 2.5)
            self.center_y = WINDOW_HEIGHT + random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 4)
            self.change_y = -METEOR_SPEED * ObstacleTimer.speed
            self.change_x = -SCROLL_SPEED * ObstacleTimer.speed


class ObstacleTimer(arcade.Sprite):
    def __init__(self):
        super().__init__()
        ObstacleTimer.timer = 0
        ObstacleTimer.speed = 1

    def update(self):
        super().update()
        ObstacleTimer.timer += 1
        if ObstacleTimer.timer >= 100:
            ObstacleTimer.timer = 0
            ObstacleTimer.speed += 0.01
