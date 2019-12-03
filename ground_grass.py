import arcade

from constants import GROUND_HEIGHT, WINDOW_WIDTH, GRASS_WIDTH, BACKGROUND_SPEED, GRASS_HEIGHT


class Grass(arcade.Sprite):
    """Sprite for the grass textures that scroll across screen"""
    def __init__(self):
        """Initializes grass with a defined speed, location, and texture"""
        super().__init__("images/Grass.png")
        self.center_x = GRASS_WIDTH // 2
        self.center_y = GRASS_HEIGHT // 2
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed

    def update(self):
        """Updates the grasses location in order to keep it scrolling infinitely"""
        super().update()
        if self.left <= -GRASS_WIDTH:
            self.center_x = WINDOW_WIDTH + GRASS_WIDTH // 2 + self.right
        self.change_x = -BACKGROUND_SPEED * GroundTimer.speed


class Grass2(arcade.Sprite):
    """The same thing as Grass, but starts one more block over"""
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
    """The ground that the character interacts with"""
    def __init__(self):
        """Sets the location of the ground"""
        super().__init__("images/Ground.png")
        self.center_x = WINDOW_WIDTH // 2
        self.center_y = GROUND_HEIGHT // 2


class GroundTimer(arcade.Sprite):
    """Creates timer for the Grass sprites in order to change its speed"""
    def __init__(self):
        """Initializes the timer's variables"""
        super().__init__()
        GroundTimer.timer = 0
        GroundTimer.speed = 1

    def update(self):
        """Updates the timer every 1/60th of a second"""
        super().update()
        GroundTimer.timer += 1
        if GroundTimer.timer >= 100:
            GroundTimer.timer = 0
            GroundTimer.speed += 0.01
