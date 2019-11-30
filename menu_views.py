import arcade
import main_game
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


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
        arcade.draw_text("Press Enter to reset",
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

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Running Man", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to Play", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
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
        print(self.high_scores)

    def on_show(self):
        arcade.set_background_color(arcade.color.CRIMSON_GLORY)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_list[0]
        death_sprite = self.game_view.kill_list[0]
        player_sprite.draw()
        death_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=0,
                                          right=WINDOW_WIDTH,
                                          top=WINDOW_HEIGHT,
                                          bottom=0,
                                          color=arcade.color.CRIMSON_GLORY + (100,))

        arcade.draw_text("GAME OVER", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        if len(self.high_scores) == 1:
            # Show tip to return or reset
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("Press Enter to reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
        elif len(self.high_scores) == 2:
            arcade.draw_text("High Scores:\n" + str(self.high_scores[0]), WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.game_view.score > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Press Enter to reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

        elif len(self.high_scores) == 3:
            arcade.draw_text("High Scores:\n" + str(self.high_scores[0]) + "\n" + str(self.high_scores[1]),
                             WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.game_view.score > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Press Enter to reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

        elif len(self.high_scores) == 4:
            arcade.draw_text("High Scores:\n" + str(self.high_scores[0]) + "\n" + str(self.high_scores[1]) + "\n" +
                             str(self.high_scores[2]), WINDOW_WIDTH / 7, 3 * WINDOW_HEIGHT / 4,
                             arcade.color.BLACK, font_size=25, anchor_x="center")
            if self.game_view.score > self.high_scores[0]:
                arcade.draw_text("New High Score!", WINDOW_WIDTH / 2, 3 * WINDOW_HEIGHT / 4, arcade.color.BLACK,
                                 font_size=25, anchor_x="center")
            arcade.draw_text("Score: " + str(self.game_view.score),
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, arcade.color.BLACK, font_size=20,
                             anchor_x="center")
            arcade.draw_text("Press Enter to reset",
                             WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20,
                             anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:  # reset game
            game = main_game.LeapsAndBoundsGame(self)
            self.window.show_view(game)