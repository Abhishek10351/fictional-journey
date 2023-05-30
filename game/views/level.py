from datetime import timedelta
import random
import pathlib
from constants import *
import arcade
import sprites


class Level(arcade.View):
    """ Base class for all levels """

    score = arcade.gui.Property(0)

    def __init__(self):
        super().__init__()

        self.total_time = timedelta(minutes=0, seconds=0, microseconds=0)
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"))

        self.score = 0
        arcade.gui.bind(self, "score", self.update_score)
        self.player = None
        self.bullets = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_bullets = arcade.SpriteList()
        self.powerups = arcade.SpriteList()
        self.manager = arcade.gui.UIManager()

    def setup(self):
        self.clear()
        self.total_time = timedelta(seconds=0)
        self.manager.clear()
        self.score = 0
        self.score_label = arcade.gui.UILabel(
            text=f"{self.score:0>5}", x=SCREEN_WIDTH-120, y=SCREEN_HEIGHT-80, font_name="Kenney Future", font_size=20)

        self.manager.add(self.score_label)
        self.bullets.clear()
        self.enemy_bullets.clear()
        self.powerups.clear()

    def on_update(self, delta_time):
        self.total_time += timedelta(seconds=delta_time)
        self.player.update()
        self.bullets.update()
        self.enemy_list.update()
        self.enemy_bullets.update()

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed. """
        if symbol == arcade.key.P:
            self.window.show_view(self.window.views["Pause"])
        if symbol == arcade.key.R:
            self.setup()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player.draw()
        self.bullets.draw()
        self.enemy_list.draw()
        self.enemy_bullets.draw()
        self.powerups.draw()
        self.manager.draw()

    def game_over(self):
        self.window.views["GameOver"].setup()
        self.window.show_view(self.window.views["GameOver"])

    def level_complete(self):
        if (self.window.current_level > self.window.levels_completed):
            self.window.levels_completed += 1

        # self.set_high_score()

        self.window.views["LevelUp"].setup()
        self.window.show_view(self.window.views["LevelUp"])

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def update_score(self):
        if self.score < 0:
            self.score = 0
            self.game_over()
        self.manager.remove(child=self.score_label)
        self.score_label.text = f"{self.score:0>5}"
        self.score_label.fit_content()
        self.manager.add(self.score_label)

    def add_powerup(self, powerup, x, y):
        self.powerups.append(sprites.Powerup(powerup, center_x=x, center_y=y))

    def create_enemies(self, enemy_instance, enemy_path, no_of_enemies=self.no_of_enemies):
        total = 0
        while total < no_of_enemies:
            enemy = enemy_instance(enemy_path, center_x=random.randint(
                0, 525), center_y=random.randint(350, 525))
            enemy_x_change = list(range(-5, 5))
            enemy_x_change.remove(0)
            enemy.change_x = random.choice(enemy_x_change)
            if not enemy.collides_with_list(self.enemy_list) or enemy.left > 0:
                total += 1
                self.enemy_list.append(enemy)
