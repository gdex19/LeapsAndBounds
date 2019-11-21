import arcade

# Define constants
from ground_grass import Ground, Grass, Grass2
from obstacles import Rocks, Rockets
from targets import Fish

GAME_TITLE = "Introduction"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.AIR_SUPERIORITY_BLUE
GAME_SPEED = 1 / 60
PLAYER_SCALE = 0.28
TILE_SCALING = 0.32
PLAYER_MOVEMENT_SPEED = 5
PLAYER_HEIGHT = 383
PLAYER_WIDTH = 300
PLAYER_JUMP_SPEED = 10
GRASS_TOP = 94
MULTIPLIER = 2
TIMER_MAX = 100
SHRINK_SPEED = 0.01
GRAVITY = 0.5


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Character.png", PLAYER_SCALE)
        self.center_x = WINDOW_WIDTH / 6
        self.center_y = GRASS_TOP + PLAYER_HEIGHT * PLAYER_SCALE / 2

    def lateral_movement(self):
        if LeapsAndBoundsGame.left_right[0] and self.left >= 0:
            self.change_x = -PLAYER_MOVEMENT_SPEED
        elif LeapsAndBoundsGame.left_right[1] and self.right <= WINDOW_WIDTH:
            self.change_x = PLAYER_MOVEMENT_SPEED
        elif not LeapsAndBoundsGame.left_right[0]:
            self.change_x = 0
        elif not LeapsAndBoundsGame.left_right[1]:
            self.change_x = 0

    def jump_duck(self):
        if LeapsAndBoundsGame.jumping and GRASS_TOP + 0.1 > self.bottom > GRASS_TOP - 0.1 and self.change_y >= 0:
            self.change_y = PLAYER_JUMP_SPEED

    def shrink(self):
        if LeapsAndBoundsGame.shrinking is True and self.scale >= PLAYER_SCALE / 2:
            self.scale -= SHRINK_SPEED
        elif LeapsAndBoundsGame.shrinking is False and self.scale <= PLAYER_SCALE:
            self.scale += SHRINK_SPEED

    def update(self):
        super().update()
        self.lateral_movement()
        self.jump_duck()
        self.shrink()


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

        arcade.draw_text("PAUSED", WINDOW_WIDTH/2, WINDOW_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         WINDOW_WIDTH/2,
                         WINDOW_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         WINDOW_WIDTH/2,
                         WINDOW_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = LeapsAndBoundsGame()
            self.window.show_view(game)


class MenuView(arcade.View):
    """Taken from example on arcade.academy"""
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", WINDOW_WIDTH/2, WINDOW_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = LeapsAndBoundsGame()
        self.window.show_view(game)


class LeapsAndBoundsGame(arcade.View):
    shrinking = bool
    jumping = bool
    left_right = list

    def __init__(self):
        """ Setup the game (or reset the game) """
        super().__init__()
        self.player_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.rocket_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()

        self.player_list.append(Player())
        self.background_list.append(Grass())
        self.background_list.append(Grass2())
        self.floor_list.append(Ground())
        self.rock_list.append(Rocks())
        self.rocket_list.append(Rockets())
        self.fish_list.append(Fish())
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list[0], self.floor_list, GRAVITY)
        self.score = 0
        self.timer = 0

        LeapsAndBoundsGame.left_right = [False, False]
        LeapsAndBoundsGame.jumping = False
        LeapsAndBoundsGame.shrinking = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            LeapsAndBoundsGame.left_right[0] = True
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            LeapsAndBoundsGame.left_right[1] = True
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S or symbol == arcade.key.LCTRL:
            LeapsAndBoundsGame.shrinking = True
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list[0], self.floor_list, GRAVITY * 2)
        elif symbol == arcade.key.UP or symbol == arcade.key.W or symbol == arcade.key.SPACE:
            LeapsAndBoundsGame.jumping = True
        elif symbol == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)
            LeapsAndBoundsGame.left_right = [False, False]
            LeapsAndBoundsGame.shrinking = False
            LeapsAndBoundsGame.jumping = False

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            LeapsAndBoundsGame.left_right[0] = False
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            LeapsAndBoundsGame.left_right[1] = False
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S or symbol == arcade.key.LCTRL:
            LeapsAndBoundsGame.shrinking = False
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list[0], self.floor_list, GRAVITY)
        elif symbol == arcade.key.UP or symbol == arcade.key.W or symbol == arcade.key.SPACE:
            LeapsAndBoundsGame.jumping = False

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.set_background_color(BACKGROUND_COLOR)
        self.player_list.draw()
        self.background_list.draw()
        self.rock_list.draw()
        self.rocket_list.draw()
        self.fish_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 20, arcade.color.WHITE, 14)

    def increase_time_score(self):
        self.timer += 1 * MULTIPLIER
        if self.timer >= TIMER_MAX:
            self.timer = 0
            self.score += 1

    def spawn_obstacles(self):
        if len(self.rock_list) < 1:
            self.rock_list.append(Rocks())
        if len(self.rocket_list) < 1:
            self.rocket_list.append(Rockets())

    def spawn_targets(self):
        if len(self.fish_list) < 2:
            self.fish_list.append(Fish())
        if len(self.fish_list) > 2:
            self.fish_list[2].remove_from_sprite_lists()

    def obstacle_collision(self):
        obstacle_hit_list1 = []
        obstacle_hit_list_rock = arcade.check_for_collision_with_list(self.player_list[0], self.rock_list)
        obstacle_hit_list_rocket = arcade.check_for_collision_with_list(self.player_list[0], self.rocket_list)
        if obstacle_hit_list1 != obstacle_hit_list_rock:
            for obstacle in obstacle_hit_list_rock:
                obstacle.remove_from_sprite_lists()
                self.score -= 10
        if obstacle_hit_list1 != obstacle_hit_list_rocket:
            for obstacle in obstacle_hit_list_rocket:
                obstacle.remove_from_sprite_lists()
                self.score -= 5

    def target_collision(self):
        target_hit_list1 = []
        target_hit_list_fish = arcade.check_for_collision_with_list(self.player_list[0], self.fish_list)
        if target_hit_list1 != target_hit_list_fish:
            for target in target_hit_list_fish:
                target.remove_from_sprite_lists()
                self.score += 5

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.player_list.update()
        self.background_list.update()
        self.floor_list.update()
        self.rock_list.update()
        self.rocket_list.update()
        self.fish_list.update()
        self.physics_engine.update()
        self.increase_time_score()
        self.obstacle_collision()
        self.target_collision()
        self.spawn_obstacles()
        self.spawn_targets()


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, 'The Game')
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
