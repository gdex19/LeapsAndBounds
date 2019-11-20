import arcade


# Define constants
WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 750
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
RIGHT = 0
LEFT = 1
PLAYER_SCALE = 0.25
TILE_SCALING = 0.32
PLAYER_MOVEMENT_SPEED = 5


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Character.png", PLAYER_SCALE)
        self.center_x = WINDOW_WIDTH / 6
        self.center_y = WINDOW_HEIGHT / 5

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


"""class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__("images/tiles/grassMid.png", TILE_SCALING)"""


class LeapsAndBoundsGame(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.physics_engine = None
        self.score = 0
        self.player_list = None
        self.wall_list = None
        LeapsAndBoundsGame.input = []

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.player_list = arcade.SpriteList()
        self.player_list.append(Player())
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

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.player_list.update()


def main():
    window = LeapsAndBoundsGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
