import arcade
from gui_widgets import *
from gui_widgets import TrophyImage
from game_data import fetch


class Trophies(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

    def setup(self):
        self.manager.clear()
        self.trophies = [TrophyImage(i) for i in fetch(
            "SELECT * FROM trophies ORDER BY number ASC")]
        self.trophy_layout = arcade.gui.UIGridLayout(
            row_count=5, col_count=5, children=self.trophies, vertical_spacing=10, horizontal_spacing=10, align_items="center")
        self.manager.add(self.trophy_layout)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()

    def on_show_view(self):
        self.clear()
        self.manager.enable()

    def on_hide_view(self):
        self.clear()
        self.manager.disable()
