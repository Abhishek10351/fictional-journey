import arcade
import arcade.gui
from gui_widgets import BackButton


class PauseScreen(arcade.View):

    def __init__(self):
        super().__init__()

        back_button = BackButton()

        @back_button.event
        def on_click(event):
            self.window.show_view(self.window.views["Menu"])

        message = "You have paused the game. \nYou can resume the game by pressing the ESC key. \n"
        self.text = arcade.gui.widgets.text.UITextArea(
            text=message, font_name="Kenney Future", width=450, height=200, font_size=20, bold=True, color=arcade.color.WHITE)

        self.manager = arcade.gui.UIManager()
        self.manager.add(back_button)
        self.manager.add(arcade.gui.UIAnchorLayout(
            children=[self.text], anchor_x="center", anchor_y="center"))

        self.manager.enable()

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(
                self.window.levels[self.window.current_level - 1])
