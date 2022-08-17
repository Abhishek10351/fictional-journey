import arcade
from constants import *

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "assets/images/background.jpg")
        self.text = "You Lost."
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text(self.text, 200, 400, bold=True,
                         font_name="Kenney High Square", font_size=80)

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class LevelUpView(arcade.View):
    """ View to show when a level is completed """

    def __init__(self, level):
        super().__init__()
        self.texture = arcade.load_texture(
            "assets/images/background.jpg")
        self.message = f"You have completed level {level}.\nClick to continue."
        self.text = arcade.Text(self.message, 10, 400, bold=True,width=300,
                    font_name="Kenney High Square", font_size=60, multiline=True)
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        self.text.draw()
        

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = self.window.views["Game"]
        game_view.setup()
        self.window.show_view(game_view)
