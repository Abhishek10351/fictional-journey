import arcade
from gui_widgets import *

class Trophies(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

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