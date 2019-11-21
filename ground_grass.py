import arcade

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
BACKGROUND_SPEED = 5
GRASS_HEIGHT = 150
GRASS_WIDTH = 1200
GROUND_HEIGHT = 94
GROUND_WIDTH = 1200


class Grass(arcade.Sprite):
    """found on stackoverflow (https://stackoverflow.com/questions/55167496/infinite-scrolling-background-in-python),
    adapted to class format"""
    def __init__(self):
        super().__init__("images/Grass.png")
        self.center_x = GRASS_WIDTH // 2
        self.center_y = GRASS_HEIGHT // 2
        self.change_x = -BACKGROUND_SPEED

    def update(self):
        super().update()
        if self.left == -GRASS_WIDTH:
            self.center_x = WINDOW_WIDTH + GRASS_WIDTH // 2


class Grass2(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Grass.png")
        self.center_x = GRASS_WIDTH + WINDOW_WIDTH // 2
        self.center_y = GRASS_HEIGHT // 2
        self.change_x = -BACKGROUND_SPEED

    def update(self):
        super().update()
        if self.left == -GRASS_WIDTH:
            self.center_x = WINDOW_WIDTH + GRASS_WIDTH // 2


class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Ground.png")
        self.center_x = WINDOW_WIDTH // 2
        self.center_y = GROUND_HEIGHT // 2