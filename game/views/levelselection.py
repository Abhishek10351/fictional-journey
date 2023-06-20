import arcade
import arcade.gui
from constants import *
from gui_widgets import BackButton, LevelButton
from game_data import fetch


class LevelSelection(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        back_button = BackButton()

        @back_button.event
        def on_click(event):
            self.window.show_view(self.window.views["Menu"])

        self.buttons = [LevelButton(
            text=str(i+1)) for i in range(self.window.total_levels)]
        self.levels = arcade.gui.UIBoxLayout(
            x=10, y=400, vertical=False, space_between=20, children=self.buttons)

        for i in self.buttons:
            i.on_click = self.on_click

        self.manager = arcade.gui.UIManager()
        self.manager.add(back_button)
        self.manager.add(self.levels)
        self.manager.enable()

    def is_playable(self, level):
        return fetch("SELECT unlocked FROM levels WHERE level = ?", level)[0]

    def on_click(self, event):
        button = event.source
        level = int(button.text)

        if self.is_playable(level):
            self.window.current_level = level
            game_level = self.window.levels[level - 1]
            game_level.setup()
            self.window.show_view(game_level)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_show_view(self):
        self.clear()
        self.manager.enable()

    def on_hide_view(self):
        self.clear()
        self.manager.disable()
