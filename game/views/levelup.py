import arcade
from constants import *


class LevelUpView(arcade.View):
    """ View to show when a level is completed """

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.manager = arcade.gui.UIManager()

    def setup(self):
        self.manager.clear()
        self.manager.add(self.text)

    @property
    def message(self):
        return f"You have completed level {self.window.current_level}."
        "Click to continue."""

    @property
    def text(self):
        return arcade.gui.UILabel(x=100, y=400, width=300, text=self.message, font_size=24, font_name="Kenney Future", multiline=True, align="center")

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        self.window.show_view(self.window.views["LevelSelect"])

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()
