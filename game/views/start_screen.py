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
        start_button.on_click = self.on_start_button_click
        self.start_screen.add(start_button.with_space_around(bottom=20))
        how_to_play = arcade.gui.UIFlatButton(
            text="How to Play", width=200)
        how_to_play.on_click = self.on_how_to_play_click
        self.start_screen.add(how_to_play.with_space_around(bottom=20))
        quit_button = arcade.gui.UIFlatButton(
            text="Exit", width=200, style=styles.danger_button)
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
        view = self.window.views["Game"]
        view.setup()
        self.window.show_view(view)

    def on_how_to_play_click(self, event):
        self.window.show_view(self.window.views["HowToPlay"])

    @property
    def level(self):
        return self.window.views["Game"].level

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()