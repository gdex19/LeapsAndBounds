import arcade


# Define constants
GAME_TITLE = "Introduction"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.BLACK
BACKGROUND_SPEED = 5
GAME_SPEED = 1/60
RIGHT = 0
LEFT = 1
PLAYER_SCALE = 0.28
TILE_SCALING = 0.32
PLAYER_MOVEMENT_SPEED = 5
GROUND_WIDTH = 1200
GROUND_HEIGHT = 94
PLAYER_HEIGHT = 383
PLAYER_WIDTH = 300
GRASS_HEIGHT = 150
GRASS_WIDTH = 1200


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Character.png", PLAYER_SCALE)
        self.center_x = WINDOW_WIDTH / 6
        self.center_y = 200

    def movement_start(self):
        if LeapsAndBoundsGame.input[0] == 1:
            self.change_x = -PLAYER_MOVEMENT_SPEED
        elif LeapsAndBoundsGame.input[1] == 1:
            self.change_x = PLAYER_MOVEMENT_SPEED
        elif LeapsAndBoundsGame.input[0] == 0:
            self.change_x = 0
        elif LeapsAndBoundsGame.input[1] == 0:
            self.change_x = 0

    def update(self):
        super().update()
        self.movement_start()


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


class Rocks(arcade.Sprite):
    def __init__(self):
        super().__init__("")


class LeapsAndBoundsGame(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.physics_engine = None
        self.score = 0
        self.player_list = None
        self.background_list = None
        self.floor_list = None
        LeapsAndBoundsGame.input = []

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.player_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()
        self.player_list.append(Player())
        self.background_list.append(Grass())
        self.background_list.append(Grass2())
        self.floor_list.append(Ground())
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list[0], self.floor_list)
        self.score = 0
        LeapsAndBoundsGame.input = [0, 0]

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            LeapsAndBoundsGame.input[0] = 1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            LeapsAndBoundsGame.input[1] = 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            LeapsAndBoundsGame.input[0] = 0
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            LeapsAndBoundsGame.input[1] = 0

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.player_list.draw()
        self.background_list.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.player_list.update()
        self.background_list.update()
        self.floor_list.update()
        self.physics_engine.update()


def main():
    window = LeapsAndBoundsGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
