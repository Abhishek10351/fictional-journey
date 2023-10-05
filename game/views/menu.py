import arcade
import arcade.gui
from constants import *
import styles
from views import levelselection, settings
from gui_widgets.buttons import StyledTextureButton


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.start_screen = arcade.gui.UIBoxLayout(space_between=20)

        start_button = StyledTextureButton(
            text="Start Game", width=200, disabled=True, color="yellow")
        start_button.on_click = self.on_start_button_click
        how_to_play = StyledTextureButton(
            text="How to Play", width=200, height=50, color="green")
        how_to_play.on_click = self.on_how_to_play_click

        settings_button = StyledTextureButton(
            text="Settings", width=200, color="blue")
        settings_button.on_click = self.on_settings_button_click

        quit_button = StyledTextureButton(
            text="Exit", width=200, color="red")

        self.start_screen.add(start_button)
        self.start_screen.add(how_to_play)
        self.start_screen.add(settings_button)
        self.start_screen.add(quit_button)

        self.ui_anchor_layout = arcade.gui.UIAnchorLayout()
        self.ui_anchor_layout.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.start_screen)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.manager.add(self.ui_anchor_layout)

        @quit_button.event("on_click")
        def on_exit(event):
            arcade.exit()

    def on_settings_button_click(self, event):
        self.window.show_view(self.window.views["Settings"])

    def on_start_button_click(self, event):
        self.window.show_view(self.window.views["LevelSelect"])

    def on_how_to_play_click(self, event):
        self.window.show_view(self.window.views["HowToPlay"])

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()
