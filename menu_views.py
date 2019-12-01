import arcade
import main_game
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SCALE


class PauseView(arcade.View):
    """Taken from example on arcade.academy"""

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_list[0]
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Select a Character to Reset",
                         WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = main_game.LeapsAndBoundsGame()
            self.window.show_view(game)


class MenuView(arcade.View):
    """Taken from example on arcade.academy"""

    def __init__(self):
        super().__init__()
        self.high_scores = []
        self.character = 0
        self.jack = arcade.Sprite("images/Jack.png", scale=PLAYER_SCALE, center_x=200, center_y=200)
        self.jill = arcade.Sprite("images/Jill.png", scale=PLAYER_SCALE, center_x=WINDOW_WIDTH - 200, center_y=200)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Leaps and Bounds: The Marathon", WINDOW_WIDTH / 2, WINDOW_HEIGHT * 2 / 3,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click on a Character to Play", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Jack", 200, 280, arcade.color.CRIMSON_GLORY, font_size=20, anchor_x="center")
        arcade.draw_text("Jill", WINDOW_WIDTH - 200, 280, arcade.color.BOTTLE_GREEN, font_size=20, anchor_x="center")
        self.jack.draw()
        self.jill.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.jack.collides_with_point([_x, _y]):
            self.character = 0
            game = main_game.LeapsAndBoundsGame(self)
            self.window.show_view(game)
        elif self.jill.collides_with_point([_x, _y]):
            self.character = 1
            game = main_game.LeapsAndBoundsGame(self)
            self.window.show_view(game)


class EndView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.high_scores = game_view.previous_view.high_scores
        if len(self.high_scores) > 0:
            self.high_scores.sort(reverse=True)
        if len(self.high_scores) > 3:
            del self.high_scores[-1]
        self.character = game_view.previous_view.character
        self.score_value = str(self.game_view.score) + ": " + self.game_view.name
        self.jack = arcade.Sprite("images/Jack.png", scale=PLAYER_SCALE, center_x=WINDOW_WIDTH - 150,
                                  center_y=WINDOW_HEIGHT - 150)
        self.jill = arcade.Sprite("images/Jill.png", scale=PLAYER_SCALE, center_x=WINDOW_WIDTH - 150,
                                  center_y=WINDOW_HEIGHT - 150)

    def on_show(self):
        arcade.set_background_color(arcade.color.CRIMSON_GLORY)

    def draw_highscore(self):
        if len(self.high_scores) == 1:
            # Show tip to return or reset
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("Select a Character to Reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
        elif len(self.high_scores) == 2:
            arcade.draw_text("High Scores:\n" + self.high_scores[0], WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.score_value > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Select a Character to Reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

        elif len(self.high_scores) == 3:
            arcade.draw_text("High Scores:\n" + self.high_scores[0] + "\n" + self.high_scores[1],
                             WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.score_value > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Select a Character to Reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

        elif len(self.high_scores) == 4:
            arcade.draw_text("High Scores:\n" + self.high_scores[0] + "\n" + self.high_scores[1] + "\n" +
                             self.high_scores[2], WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.score_value > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Select a Character, Press Enter to Reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

    def character_switch(self):
        if self.character == 0:
            self.jack.draw()
            self.jack.center_x = WINDOW_WIDTH - 150
            self.jill.center_x = -50
        elif self.character == 1:
            self.jill.draw()
            self.jill.center_x = WINDOW_WIDTH - 150
            self.jack.center_x = -50

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_list[0]
        death_sprite = self.game_view.kill_list[0]
        player_sprite.draw()
        death_sprite.draw()

        # draw a red filter over him
        arcade.draw_lrtb_rectangle_filled(left=0,
                                          right=WINDOW_WIDTH,
                                          top=WINDOW_HEIGHT,
                                          bottom=0,
                                          color=arcade.color.CRIMSON_GLORY + (100,))
        self.draw_highscore()
        self.character_switch()

        arcade.draw_text("GAME OVER", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.jack.collides_with_point([x, y]):
            self.character = 1
        elif self.jill.collides_with_point([x, y]):
            self.character = 0

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:  # reset game
            game = main_game.LeapsAndBoundsGame(self)
            self.window.show_view(game)
