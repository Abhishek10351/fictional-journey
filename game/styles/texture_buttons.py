import arcade.color as color
from arcade.gui import UITextureButton

UIStyle = UITextureButton.UIStyle

styled_texture_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21)
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    )
}