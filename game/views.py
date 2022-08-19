import arcade
import arcade.gui
from constants import *
import styles


class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.start_screen = arcade.gui.UIBoxLayout()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.start_screen.add(start_button.with_space_around(bottom=20))
        self.how_to_play = arcade.gui.UIFlatButton(
            text="How to Play", width=200)
        self.how_to_play.on_click = self.on_how_to_play_click
        self.start_screen.add(self.how_to_play.with_space_around(bottom=20))
        quit_button = arcade.gui.UIFlatButton(
            text="Exit", width=200, style=styles.danger_button)
        start_button.on_click = self.on_start_button_click
        self.start_screen.add(quit_button)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.start_screen)
        )

        @quit_button.event
        def on_click(event):
            arcade.exit()

    def on_start_button_click(self, event):
        self.current_stage = self.level
        view = self.window.views["Game"]
        view.setup()
        self.window.show_view(view)

    def on_how_to_play_click(self, event):
        self.current_stage = "Start"
        self.window.show_view(self.window.views["HowToPlay"])

    @property
    def level(self):
        return self.window.views["Game"].level

    def on_draw(self):
        self.clear()
        self.manager.draw()


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

        game_view = self.window.views["StartScreen"]
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
        game_view = self.window.views["StartScreen"]
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
        return """Hello, Player! Welcome to the game.
    It is quite a simple Game, all you have to do is to kill all the enemies using your SpaceShip
    and collect items and powerups falling from them.
    Use the arrow keys to move up and down or change the direction as needed in the level.
    Gamepad support will be added later on the game.
    """

    @property
    def text(self):
        return arcade.Text(self.message, 100, 400, bold=True, width=400,  multiline=True, color=arcade.color.RED, font_size=16, align="center")

    def on_draw(self):
        self.clear()
        self.text.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """

        game_view = self.window.views["StartScreen"]
        self.window.show_view(game_view)
