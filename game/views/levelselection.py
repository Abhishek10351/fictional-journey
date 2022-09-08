import arcade
import arcade.gui
from constants import *
import styles


class LevelSelection(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        buttons = [arcade.gui.UIFlatButton(
            text=i, width=60, style=styles.primary_button) for i in range(1, self.window.total_levels+1)]
        self.levels = arcade.gui.UIBoxLayout(
            x=10, y=500, vertical=False, space_between=20, children=buttons)

        for i in buttons:
            i.on_click = self.on_click

        self.manager = arcade.gui.UIManager()
        self.manager.add(self.levels)
        self.manager.enable()

    def on_click(self, event):
        button = event.source
        game_level = self.window.levels[button.text]
        game_level.setup()
        self.window.show_view(game_level)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.clear()
        self.manager.disable()

    def on_show_view(self):
        self.clear()
        self.manager.enable()
