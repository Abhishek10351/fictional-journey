"""Lmao
"""
import arcade
import arcade.gui
from constants import SCREEN_HEIGHT


class BackButton(arcade.gui.UITextureButton):
    def __init__(self, back_view=None,**kwargs):
        self.back_view = back_view
        super().__init__(
            texture=arcade.load_texture(
                'assets/gui/icons/arrowLeftBlack.png'),
            texture_hovered=arcade.load_texture(
                'assets/gui/icons/arrowLeftWhite.png'),
            texture_pressed=arcade.load_texture(
                'assets/gui/icons/arrowLeftBlack.png'),
            width=50, height=50, y=SCREEN_HEIGHT-50, **kwargs
        )

    def on_update(self, dt):
        if self.pressed:
            color=arcade.color.WHITE
        elif self.hovered:
            color=arcade.color.BLACK
        else:
            color=arcade.color.WHITE
        self.with_background(color=color)
