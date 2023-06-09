import arcade.color as color
from arcade.gui import UITextureButton

UIStyle = UITextureButton.UIStyle

styled_texture_button = {
    "normal": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color = color.COOL_BLACK
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.GRAY
    )
}