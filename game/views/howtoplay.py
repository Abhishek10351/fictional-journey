import arcade
import arcade.gui
from constants import *
from gui_widgets import BackButton

class HowToPlay(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.message = """Hello, Player! Welcome to the game.
        It is quite a simple Game, all you have to do is to kill all the enemies using your SpaceShip
        and collect items and powerups falling from them.
        Use the arrow keys to move up and down or change the direction as needed in the level.
        Gamepad support will be added later on the game.
        """

        self.text = arcade.Text(self.message, 100, 400, bold=True, width=400,  multiline=True,
                                color=arcade.color.RED, font_size=14, align="center", font_name="Comic Sans ms")
        button = BackButton()
        self.manager = arcade.gui.UIManager()
        self.manager.add(button)
        @button.event
        def on_click(event):
            self.window.show_view(self.window.views["Menu"])

    def on_draw(self):
        self.clear()
        self.text.draw()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()
    
    def on_show_view(self):
        self.manager.enable()
