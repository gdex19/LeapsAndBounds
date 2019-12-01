import arcade
import menu_views
# Define constants
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SCALE, GRASS_TOP, JACK_MOVEMENT_SPEED, \
    JACK_JUMP_SPEED, SHRINK_SPEED, BACKGROUND_COLOR, TIMER_MAX, MULTIPLIER, GRAVITY, GAME_TITLE, JILL_MOVEMENT_SPEED, \
    JILL_JUMP_SPEED, JILL_HEIGHT, JACK_HEIGHT, BACKGROUND_COLOR_HARD
from ground_grass import Ground, Grass, Grass2, GroundTimer
from obstacles import Rocks, Rockets, ObstacleTimer, Meteor
from targets import Fish, Diamond, TargetTimer


class MainTimer(arcade.Sprite):
    def __init__(self):
        super().__init__()
        MainTimer.timer = 0
        MainTimer.speed = 1

    def update(self):
        super().update()
        MainTimer.timer += 1
        if MainTimer.timer >= 100:
            MainTimer.timer = 0
            MainTimer.speed += 0.01


class JillPlayer(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Jill.png", PLAYER_SCALE)
        self.center_x = WINDOW_WIDTH / 6
        self.center_y = GRASS_TOP + JILL_HEIGHT * PLAYER_SCALE / 2
        self.left_facing = arcade.load_texture("images/Jill.png", mirrored=True, scale=self.scale)
        self.right_facing = arcade.load_texture("images/Jill.png", scale=self.scale)

    def lateral_movement(self):
        if LeapsAndBoundsGame.left_right[0] and self.left >= 0:
            self.texture = self.left_facing
            self.change_x = -JILL_MOVEMENT_SPEED
        elif LeapsAndBoundsGame.left_right[1] and self.right <= WINDOW_WIDTH:
            self.texture = self.right_facing
            self.change_x = JILL_MOVEMENT_SPEED
        elif not LeapsAndBoundsGame.left_right[0]:
            self.texture = self.right_facing
            self.change_x = 0
        elif not LeapsAndBoundsGame.left_right[1]:
            self.change_x = 0

    def jump_duck(self):
        if LeapsAndBoundsGame.jumping and self.bottom < GRASS_TOP + 1:
            self.change_y = JILL_JUMP_SPEED

    def shrink(self):
        if LeapsAndBoundsGame.shrinking is True and self.scale >= PLAYER_SCALE / 2:
            self.scale -= SHRINK_SPEED
        elif LeapsAndBoundsGame.shrinking is False and self.scale <= PLAYER_SCALE:
            self.scale += SHRINK_SPEED

    def set_texture_scales(self):
        if self.scale != PLAYER_SCALE:
            self.left_facing = arcade.load_texture("images/Jill.png", mirrored=True, scale=self.scale)
            self.right_facing = arcade.load_texture("images/Jill.png", scale=self.scale)

    def update(self):
        super().update()
        self.lateral_movement()
        self.jump_duck()
        self.shrink()
        self.set_texture_scales()


class JackPlayer(arcade.Sprite):
    def __init__(self):
        super().__init__("images/Jack.png", PLAYER_SCALE)
        self.center_x = WINDOW_WIDTH / 6
        self.center_y = GRASS_TOP + JACK_HEIGHT * PLAYER_SCALE / 2
        self.left_facing = arcade.load_texture("images/Jack.png", mirrored=True, scale=self.scale)
        self.right_facing = arcade.load_texture("images/Jack.png", scale=self.scale)

    def lateral_movement(self):
        if LeapsAndBoundsGame.left_right[0] and self.left >= 0:
            self.texture = self.left_facing
            self.change_x = -JACK_MOVEMENT_SPEED
        elif LeapsAndBoundsGame.left_right[1] and self.right <= WINDOW_WIDTH:
            self.texture = self.right_facing
            self.change_x = JACK_MOVEMENT_SPEED
        elif not LeapsAndBoundsGame.left_right[0]:
            self.texture = self.right_facing
            self.change_x = 0
        elif not LeapsAndBoundsGame.left_right[1]:
            self.change_x = 0

    def jump_duck(self):
        if LeapsAndBoundsGame.jumping and self.bottom < GRASS_TOP + 1:
            self.change_y = JACK_JUMP_SPEED

    def shrink(self):
        if LeapsAndBoundsGame.shrinking is True and self.scale >= PLAYER_SCALE / 2:
            self.scale -= SHRINK_SPEED
        elif LeapsAndBoundsGame.shrinking is False and self.scale <= PLAYER_SCALE:
            self.scale += SHRINK_SPEED

    def set_texture_scales(self):
        if self.scale != PLAYER_SCALE:
            self.left_facing = arcade.load_texture("images/Jack.png", mirrored=True, scale=self.scale)
            self.right_facing = arcade.load_texture("images/Jack.png", scale=self.scale)

    def update(self):
        super().update()
        self.lateral_movement()
        self.jump_duck()
        self.shrink()
        self.set_texture_scales()


class LeapsAndBoundsGame(arcade.View):
    shrinking = bool
    jumping = bool
    left_right = list

    def __init__(self, previous_view):
        """ Setup the game (or reset the game) """
        super().__init__()
        self.previous_view = previous_view
        self.timer_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.rocket_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.kill_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        if self.previous_view.character == 0:
            self.player_list.append(JackPlayer())
            self.name = "Jack"
        elif self.previous_view.character == 1:
            self.player_list.append(JillPlayer())
            self.name = "Jill"

        self.timer_list.append(GroundTimer())
        self.timer_list.append(TargetTimer())
        self.timer_list.append(ObstacleTimer())
        self.timer_list.append(MainTimer())
        self.background_list.append(Grass())
        self.background_list.append(Grass2())
        self.floor_list.append(Ground())
        self.rock_list.append(Rocks())
        self.rocket_list.append(Rockets())
        self.fish_list.append(Fish())
        self.diamond_list.append(Diamond())
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_list[0], self.floor_list, GRAVITY)
        self.score = 0
        self.timer = 0
        self.lives = 3
        self.fish_count = 0

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
            if self.physics_engine.can_jump():
                LeapsAndBoundsGame.jumping = True
        elif symbol == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = menu_views.PauseView(self)
            self.window.show_view(pause)
            LeapsAndBoundsGame.left_right = [False, False]
            LeapsAndBoundsGame.shrinking = False
            LeapsAndBoundsGame.shrinking = False

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
        self.diamond_list.draw()
        self.meteor_list.draw()
        score_output = f"Score: {self.score}"
        arcade.draw_text(score_output, 20, 20, arcade.color.WHITE, 14)
        lives_output = f"Lives: {self.lives}"
        arcade.draw_text(lives_output, WINDOW_WIDTH - 100, 20, arcade.color.WHITE, 14)

    def increase_time_score(self):
        self.timer += MULTIPLIER
        if self.timer >= TIMER_MAX:
            self.timer = 0
            self.score += int(1 * MainTimer.speed)

    def spawn_obstacles(self):
        if len(self.rock_list) < 1:
            self.rock_list.append(Rocks())
        if len(self.rocket_list) < 1:
            self.rocket_list.append(Rockets())
        if self.score >= 250 and len(self.meteor_list) < 1:
            self.meteor_list.append(Meteor())

    def background_change(self):
        if self.score >= 250:
            arcade.draw_lrtb_rectangle_filled(left=0,
                                              right=WINDOW_WIDTH,
                                              top=GRASS_TOP,
                                              bottom=0,
                                              color=arcade.color.LAVA + (150,))
            arcade.set_background_color(BACKGROUND_COLOR_HARD)

    def spawn_targets(self):
        if len(self.fish_list) < 2:
            self.fish_list.append(Fish())
        elif len(self.fish_list) > 2:
            self.fish_list[2].remove_from_sprite_lists()
        elif len(self.diamond_list) < 1:
            self.diamond_list.append(Diamond())

    def fish_count_lives(self):
        if self.fish_count >= 20:
            self.lives += 1
            self.fish_count = 0

    def obstacle_collision(self):
        obstacle_hit_list1 = []
        obstacle_hit_list_rock = arcade.check_for_collision_with_list(self.player_list[0], self.rock_list)
        obstacle_hit_list_rocket = arcade.check_for_collision_with_list(self.player_list[0], self.rocket_list)
        obstacle_hit_list_meteor = arcade.check_for_collision_with_list(self.player_list[0], self.meteor_list)
        if obstacle_hit_list1 != obstacle_hit_list_rock:
            for obstacle in obstacle_hit_list_rock:
                self.kill_list.append(obstacle)
            end = menu_views.EndView(self)
            self.previous_view.high_scores.append(self.score)
            self.window.show_view(end)
        if obstacle_hit_list1 != obstacle_hit_list_rocket:
            for obstacle in obstacle_hit_list_rocket:
                if self.lives == 1:
                    self.kill_list.append(obstacle)
                    end = menu_views.EndView(self)
                    self.previous_view.high_scores.append(self.score)
                    self.window.show_view(end)
                else:
                    obstacle.remove_from_sprite_lists()
                    self.lives -= 1
                    self.score -= 10
        if obstacle_hit_list1 != obstacle_hit_list_meteor:
            for obstacle in obstacle_hit_list_meteor:
                if self.lives == 1:
                    self.kill_list.append(obstacle)
                    end = menu_views.EndView(self)
                    self.previous_view.high_scores.append(self.score)
                    self.window.show_view(end)
                else:
                    obstacle.remove_from_sprite_lists()
                    self.lives -= 1
                    self.score -= 50

    def target_collision(self):
        target_hit_list1 = []
        target_hit_list_fish = arcade.check_for_collision_with_list(self.player_list[0], self.fish_list)
        target_hit_list_diamond = arcade.check_for_collision_with_list(self.player_list[0], self.diamond_list)
        if target_hit_list1 != target_hit_list_fish:
            for target in target_hit_list_fish:
                target.remove_from_sprite_lists()
                self.score += 5
                self.fish_count += 1
        elif target_hit_list1 != target_hit_list_diamond:
            for target in target_hit_list_diamond:
                target.remove_from_sprite_lists()
                self.score += 20

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.player_list.update()
        self.timer_list.update()
        self.background_list.update()
        self.floor_list.update()
        self.rock_list.update()
        self.rocket_list.update()
        self.diamond_list.update()
        self.meteor_list.update()
        self.fish_list.update()
        self.kill_list.update()
        self.physics_engine.update()
        self.background_change()
        self.fish_count_lives()
        self.increase_time_score()
        self.obstacle_collision()
        self.target_collision()
        self.spawn_obstacles()
        self.spawn_targets()


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    menu = menu_views.MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
