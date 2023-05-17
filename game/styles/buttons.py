import arcade.color as color
from arcade.gui import UIFlatButton

UIStyle = UIFlatButton.UIStyle

primary_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(52, 152, 219)
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(52, 152, 219),
        border=(41, 128, 185),
        border_width=2,
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
        border=None,
        border_width=2,
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
    )
}
success_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(39, 174, 96)  # Success button background color
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(39, 174, 96),
        border=(46, 204, 113),  # Hover border color
        border_width=2,
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(46, 204, 113)  # Pressed button background color
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(46, 204, 113)
    )
}

danger_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(217, 4, 41)
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(217, 4, 41),
        border=(255, 166, 158),
        border_width=2,
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(255, 166, 158)
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(255, 166, 158)
    )
}

light_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE,
        border=(21, 19, 21),
        border_width=2,
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(21, 19, 21)
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE,
    )
}
dark_button = {
    "normal": UIStyle(
        font_size=12,
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(21, 19, 21)
    ),
    "hover": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        border=color.WHITE,
        border_width=2,
    ),
    "press": UIStyle(
        font_name="Kenney Future",
        font_color=(21, 19, 21),
        bg=color.WHITE
    ),
    "disabled": UIStyle(
        font_name="Kenney Future",
        font_color=color.WHITE,
        bg=(41, 128, 185),
    )
}
