import arcade
import random
import main_game

from constants import FISH_SCALE, FISH_HEIGHT, WINDOW_HEIGHT, FISH_WIDTH, WINDOW_WIDTH, GRASS_TOP, SCROLL_SPEED, \
    FISH_SPEED, SPEED_INCREMENT, SPEED_TIMER_MAX


class Fish(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Fish.png", FISH_SCALE)
        self.speed = main_game.LeapsAndBoundsGame().score + 1
        self.center_x = random.randint(WINDOW_WIDTH + FISH_SCALE * FISH_WIDTH / 2,
                                       1.5 * WINDOW_WIDTH - FISH_SCALE *
                                       FISH_WIDTH / 2)
        self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT /
                                                       2, WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)
        self.change_y = -FISH_SPEED
        self.change_x = -SCROLL_SPEED

    def update(self):
        super().update()
        self.update_speed()
        if self.bottom <= GRASS_TOP:
            self.center_x = random.randint(FISH_SCALE * FISH_WIDTH / 2, WINDOW_WIDTH - FISH_SCALE * FISH_WIDTH / 2)
            self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT / 2,
                                                           WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)
        self.change_x = -SCROLL_SPEED
        self.change_y = -FISH_SPEED







