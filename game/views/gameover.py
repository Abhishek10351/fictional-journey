import arcade
import arcade.gui
from constants import *
import pathlib


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            pathlib.Path("assets/images/background.jpg"))
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.manager = arcade.gui.UIManager()

    def setup(self):
        self.manager.clear()
        self.manager.add(arcade.gui.UIAnchorLayout(
            children=[self.text], anchor_x="center", anchor_y="center"))
        if self.window.sound:
            arcade.Sound(
                "assets/sounds/game_over.ogg").play(
                volume=self.window.volume/100)

    @property
    def message(self):
        return (f"You have lost level {self.window.current_level}."
                "Click to continue.")

    @property
    def text(self):
        return arcade.gui.UILabel(
            text=self.message, font_name="Kenney Future", width=450, height=200, font_size=24, bold=True, text_color=arcade.color.WHITE, multiline=True)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """

        self.window.show_view(self.window.views["LevelSelect"])

    def on_show_view(self):
        self.manager.enable()
        if self.window.controller:
            self.window.controller.push_handlers(self)

    def on_hide_view(self):
        self.manager.disable()
        if self.window.controller:
            self.window.controller.remove_handlers(self)
    def on_button_press(self, controller, button):
        if button in ["b", "back"]:
            self.window.show_view(self.window.views["LevelSelect"])
        elif button in ["start", "a"]:
            self.window.levels[self.window.current_level-1].setup()
            self.window.show_view(self.window.levels[self.window.current_level-1])