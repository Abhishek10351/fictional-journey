"""Lmao
"""
import arcade
import arcade.gui
from constants import SCREEN_HEIGHT


class BackButton(arcade.gui.UITextureButton):
    def __init__(self, **kwargs):
        super().__init__(
            texture=arcade.load_texture(
                'assets/gui/icons/arrow-left.png'),
            texture_hovered=arcade.load_texture(
                'assets/gui/icons/arrow-left hover.png'),
            texture_pressed=arcade.load_texture(
                'assets/gui/icons/arrow-left click.png'),
            width=50, height=50, y=SCREEN_HEIGHT-50, x=5,  **kwargs
        )
