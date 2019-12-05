import arcade
import random

from constants import FISH_SCALE, WINDOW_HEIGHT, GRASS_TOP, SCROLL_SPEED, \
    FISH_SPEED, DIAMOND_SCALE, DIAMOND_SPEED, HEART_SCALE, HEART_SPEED


class Fish(arcade.Sprite):
    """A sprite for a target, represented by a fish"""
    def __init__(self):
        """Initialized the sprite's location, speed, and texture"""
        super().__init__("images/Fish.png", FISH_SCALE)
        self.center_x = WINDOW_HEIGHT * 13 / 4
        self.center_y = random.randint(WINDOW_HEIGHT * 5 / 4, WINDOW_HEIGHT * 13 / 4 + 400)
        self.change_y = -FISH_SPEED * TargetTimer.speed
        self.change_x = -SCROLL_SPEED * TargetTimer.speed

    def update(self):
        """Updates the sprite's location, speed, and texture"""
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = WINDOW_HEIGHT * 13 / 4
            self.center_y = random.randint(WINDOW_HEIGHT * 5 / 4, WINDOW_HEIGHT * 13 / 4 + 400)
            self.change_y = -FISH_SPEED * TargetTimer.speed
            self.change_x = -SCROLL_SPEED * TargetTimer.speed


class Diamond(arcade.Sprite):
    """A sprite for a more valuable target, the diamond"""
    def __init__(self):
        """Initialized the sprite's location, speed, and texture"""
        super().__init__("images/Diamond.png", DIAMOND_SCALE)
        self.center_x = WINDOW_HEIGHT * 16 / 3
        self.center_y = random.randint(WINDOW_HEIGHT * 5, WINDOW_HEIGHT * 8 + 400)
        self.change_y = -DIAMOND_SPEED * TargetTimer.speed
        self.change_x = -SCROLL_SPEED * TargetTimer.speed

    def update(self):
        """Updates the sprite's location, speed, and texture"""
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = WINDOW_HEIGHT * 16 / 3
            self.center_y = random.randint(WINDOW_HEIGHT * 5, WINDOW_HEIGHT * 8 + 400)
            self.change_y = -DIAMOND_SPEED * TargetTimer.speed
            self.change_x = -SCROLL_SPEED * TargetTimer.speed


class Heart(arcade.Sprite):
    """A sprite to regain lives, represented by a heart, only when they have one life"""
    def __init__(self):
        """Initialized the sprite's location, speed, and texture"""
        super().__init__("images/heart.png", HEART_SCALE)
        self.center_x = WINDOW_HEIGHT * 6
        self.center_y = random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 12)
        self.change_y = -HEART_SPEED * TargetTimer.speed
        self.change_x = -SCROLL_SPEED * TargetTimer.speed

    def update(self):
        """Updates the sprite's location, speed, and texture"""
        super().update()
        if self.bottom <= GRASS_TOP:
            self.center_x = WINDOW_HEIGHT * 6
            self.center_y = random.randint(WINDOW_HEIGHT * 3, WINDOW_HEIGHT * 12)
            self.change_y = -HEART_SPEED * TargetTimer.speed
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








