import arcade
import arcade.gui
from constants import SCREEN_HEIGHT, GUI_PATH
from .buttons import TextureButton
from styles import normal_button

icons_path = GUI_PATH / "icons"


class BackButton(TextureButton):
    def __init__(self, **kwargs):
        super().__init__(
            texture=arcade.load_texture(
                icons_path/'arrow-left.png'),
            texture_hovered=arcade.load_texture(
                icons_path/'arrow-left hover.png'),
            texture_pressed=arcade.load_texture(
                icons_path/'arrow-left click.png'),
            width=50, height=50, y=SCREEN_HEIGHT-50, x=5, 
            style=normal_button,  **kwargs
        )
