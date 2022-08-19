import arcade
from constants import *


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "assets/images/background.jpg")
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    @property
    def level(self):
        return self.window.views["Game"].level

    @property
    def message(self):
        return f"You have lost level {self.level}.\nClick to continue."

    @property
    def text(self):
        return arcade.Text(self.message, 100, 400, bold=True, width=300,
                           font_name="Kenney High Square", font_size=60, multiline=True)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        self.text.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """

        game_view = self.window.views["Game"]
        game_view.setup()
        self.window.show_view(game_view)


class LevelUpView(arcade.View):
    """ View to show when a level is completed """

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    @property
    def level(self):
        return self.window.views["Game"].level

    @property
    def message(self):
        return f"You have completed level {self.level-1}.\nClick to continue."

    @property
    def text(self):
        return arcade.Text(self.message, 100, 400, bold=True, width=300,
                           font_name="Kenney High Square", font_size=60, multiline=True)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.text.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = self.window.views["Game"]
        game_view.setup()
        self.window.show_view(game_view)


class HowToPlay(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    @property
    def level(self):
        return self.window.views["Game"].level

    @property
    def message(self):
        return """Hello, Player!
    Welcome to the game
    It is quite a simple Game, all you have to do is to kill all the enemies using your SpaceShip
    and collect items and powerups falling from them.
    Use the arrow keys to move up and down or change the direction as needed in the level.
    Gamepad support will be added later on the game.
    """

    @property
    def text(self):
        return arcade.Text(self.message, 100, 400, bold=True, width=300,  multiline=True)

    def on_draw(self):
        self.clear()
        text.draw()
