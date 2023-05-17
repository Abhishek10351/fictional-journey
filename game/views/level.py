import arcade
from datetime import timedelta


class Level(arcade.View):
    """ Base class for all levels """

    def __init__(self):
        super().__init__()

        self.total_seconds = timedelta(minutes=0, seconds=0, microseconds=0)
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"), width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.score = 0
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()

    def setup(self):
        self.clear()
        self.total_seconds = timedelta(minutes=0, seconds=0, microseconds=0)
        self.score = 0
        self.bullet_list.clear()
        self.enemy_bullet_list.clear()

    def on_update(self, delta_time):
        self.total_seconds += timedelta(seconds=delta_time)

        self.player.update()
        self.bullets.update()
        self.enemy_bullet_list.update()       

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if symbol == arcade.key.P:
            self.window.show_view(self.window.views["Pause"])
        if symbol == arcade.key.R:
            self.setup()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player.draw()
        self.bullets.draw()
        self.enemy_bullet_list.draw()