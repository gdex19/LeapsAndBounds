import arcade
import random

from constants import FISH_SCALE, FISH_HEIGHT, WINDOW_HEIGHT, FISH_WIDTH, WINDOW_WIDTH, GRASS_TOP, SCROLL_SPEED, \
    FISH_SPEED, DIAMOND_SCALE, DIAMOND_SPEED


class Fish(arcade.Sprite):
    """A sprite for a target, represented by a fish"""
    def __init__(self):
        """Initialized the sprite's location, speed, and texture"""
        super().__init__("images/Fish.png", FISH_SCALE)
        self.center_x = random.randint(WINDOW_WIDTH + FISH_SCALE * FISH_WIDTH / 2,
                                       1.5 * WINDOW_WIDTH - FISH_SCALE *
                                       FISH_WIDTH / 2)
        self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT /
                                                       2, WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)
        self.change_y = -FISH_SPEED * TargetTimer.speed
        self.change_x = -SCROLL_SPEED * TargetTimer.speed

    def update(self):
        """Updates the sprite's location, speed, and texture"""
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = random.randint(FISH_SCALE * FISH_WIDTH / 2, WINDOW_WIDTH - FISH_SCALE * FISH_WIDTH / 2)
            self.center_y = WINDOW_HEIGHT + random.randint(FISH_SCALE * FISH_HEIGHT / 2,
                                                           WINDOW_HEIGHT - FISH_SCALE * FISH_HEIGHT / 2)
            self.change_y = -FISH_SPEED * TargetTimer.speed
            self.change_x = -SCROLL_SPEED * TargetTimer.speed


class Diamond(arcade.Sprite):
    """A sprite for a more valuable target, the diamond"""
    def __init__(self):
        """Initialized the sprite's location, speed, and texture"""
        super().__init__("images/Diamond.png", DIAMOND_SCALE)
        self.center_x = random.randint(WINDOW_WIDTH * 1.5, WINDOW_WIDTH * 2.5)
        self.center_y = WINDOW_HEIGHT + random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 4)
        self.change_y = -DIAMOND_SPEED * TargetTimer.speed
        self.change_x = -SCROLL_SPEED * TargetTimer.speed

    def update(self):
        """Updates the sprite's location, speed, and texture"""
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = random.randint(WINDOW_WIDTH * 1.5, WINDOW_WIDTH * 2.5)
            self.center_y = WINDOW_HEIGHT + random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 4)
            self.change_y = -DIAMOND_SPEED * TargetTimer.speed
            self.change_x = -SCROLL_SPEED * TargetTimer.speed


class TargetTimer(arcade.Sprite):
    """Sets up timer for targets, in order to adjust their speed"""
    def __init__(self):
        """Initializes the timer and it's variables"""
        super().__init__()
        TargetTimer.timer = 0
        TargetTimer.speed = 1

    def update(self):
        """Updates the timer every 1/60th of a second"""
        super().update()
        TargetTimer.timer += 1
        if TargetTimer.timer >= 100:
            TargetTimer.timer = 0
            TargetTimer.speed += 0.01








