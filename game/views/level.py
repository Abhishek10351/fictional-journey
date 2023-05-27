import arcade
from datetime import timedelta
import pathlib
from constants import *


class Level(arcade.View):
    """ Base class for all levels """

    def __init__(self):
        super().__init__()

        self.total_time = timedelta(minutes=0, seconds=0, microseconds=0)
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"))
        self.score = 0
        self.player = None
        self.bullets = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_bullets = arcade.SpriteList()
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
        self.manager.draw()

    def game_over(self):
        self.window.views["GameOver"].setup()
        self.window.show_view(self.window.views["GameOver"])

    def level_complete(self):
        if (self.window.current_level > self.window.levels_completed):
            self.window.levels_completed += 1

        self.window.views["LevelUp"].setup()
        self.window.show_view(self.window.views["LevelUp"])

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()
