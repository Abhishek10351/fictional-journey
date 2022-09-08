import arcade
import arcade.gui
from constants import *
import styles


class HowToPlay(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    @property
    def level(self):
        return self.window.level

    @property
    def message(self):
        return """Hello, Player! Welcome to the game.
    It is quite a simple Game, all you have to do is to kill all the enemies using your SpaceShip
    and collect items and powerups falling from them.
    Use the arrow keys to move up and down or change the direction as needed in the level.
    Gamepad support will be added later on the game.
    """

    @property
    def text(self):
        return arcade.Text(self.message, 100, 400, bold=True, width=400,  multiline=True, color=arcade.color.RED, font_size=16, align="center", font_name= "Kenney Future Narrow")

    def on_draw(self):
        self.clear()
        self.text.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """

        game_view = self.window.views["StartScreen"]
        self.window.show_view(game_view)
