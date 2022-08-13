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


class LevelCompleteView(arcade.View):
    """ View to show when a level is completed """

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "assets/images/background.jpg")
        self.text = "Level Completed"
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
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
