import arcade

from constants import GROUND_HEIGHT, WINDOW_WIDTH, GRASS_WIDTH, BACKGROUND_SPEED, GRASS_HEIGHT


class Grass(arcade.Sprite):
    """found on stackoverflow (https://stackoverflow.com/questions/55167496/infinite-scrolling-background-in-python),
    adapted to class format"""
    def __init__(self):
        super().__init__("images/Grass.png")
        self.center_x = GRASS_WIDTH // 2
        self.center_y = GRASS_HEIGHT // 2
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed

    def update(self):
        super().update()
        if self.left <= -GRASS_WIDTH:
            self.center_x = WINDOW_WIDTH + GRASS_WIDTH // 2 + self.right
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed


class Grass2(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Grass.png")
        self.center_x = GRASS_WIDTH + WINDOW_WIDTH // 2
        self.center_y = GRASS_HEIGHT // 2
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed

    def update(self):
        super().update()
        if self.left <= -GRASS_WIDTH:
            self.center_x = WINDOW_WIDTH + GRASS_WIDTH // 2 + self.right
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed


class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Ground.png")
        self.center_x = WINDOW_WIDTH // 2
        self.center_y = GROUND_HEIGHT // 2


class GroundTimer(arcade.Sprite):
    def __init__(self):
        super().__init__()
        GroundTimer.timer = 0
        GroundTimer.speed = 1

    def update(self):
        super().update()
        GroundTimer.timer += 1
        if GroundTimer.timer >= 100:
            GroundTimer.timer = 0
            GroundTimer.speed += 0.01
