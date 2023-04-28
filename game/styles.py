import arcade.color as color
from arcade.gui import UIFlatButton
from arcade.gui import UITextureButton

danger_button = {
    "normal": UIFlatButton.UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(217, 4, 41)
    ),
    "hover": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(217, 4, 41),
        border=(255, 166, 158),
        border_width=2,
    ),
    "press": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(255, 166, 158)
    ),
    "disabled": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(255, 166, 158)
    )
}
primary_button = {
    "normal": UIFlatButton.UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(52, 152, 219)
    ),
    "hover": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(52, 152, 219),
        border=(41, 128, 185),
        border_width=2,
    ),
    "press": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
        border=None,
        border_width=2,
    ),
    "disabled": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
    )
}

dark_texture_button = {
    "normal": UITextureButton.UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "hover": UITextureButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    ),
    "press": UITextureButton.UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21)
    ),
    "disabled": UITextureButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE
    )
}
light_button = {
    "normal": UIFlatButton.UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE
    ),
    "hover": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE,
        border=(21, 19, 21),
        border_width=2,
    ),
    "press": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(21, 19, 21)
    ),
    "disabled": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE,
    )
}
dark_button = {
    "normal": UIFlatButton.UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(21, 19, 21)
    ),
    "hover": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        border=color.WHITE,
        border_width=2,
    ),
    "press": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE
    ),
    "disabled": UIFlatButton.UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
    )
}
