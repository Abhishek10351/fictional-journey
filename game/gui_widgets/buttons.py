import arcade.gui
from constants import TEXTURES_PATH
import styles
import arcade.color
from PIL import ImageEnhance


# !add flat button but with single argument for font size and font name
class TextureButton(arcade.gui.UITextureButton):
    def __init__(self, text="", font_size=12,
                 font_name="Kenney Future", **kwargs):

        self.font_size = font_size
        self.font_name = font_name
        super().__init__(text=text, **kwargs)
        with self._label.label:
            self._label.label.font_name = self.font_name
            self._label.label.font_size = self.font_size

        self._label.fit_content()
        self.ui_label.rect = self.ui_label.rect.max_size(
            self.content_width, self.content_height)

    def apply_style(self, color):

        font_color_changed = self._label.label.color != color
        if font_color_changed:
            with self._label.label:
                self._label.label.color = color

            self._label.fit_content()
            self.ui_label.rect = self.ui_label.rect.max_size(
                self.content_width, self.content_height)


class StyledTextureButton(TextureButton):
    def __init__(self, size="large", color="blue",
                 outlined=False, flat=False, **kwargs):

        texture_path = TEXTURES_PATH / "buttons" / size / color

        texture = texture_path/ f"{color}_button00.png"
        texture_hover = texture_path/ f"{color}_button01.png"
        texture_pressed = texture_path/ f"{color}_button02.png"
        texture_disabled = texture_path.parent / "grey" / "grey_button00.png"

        texture = arcade.load_texture(texture)
        texture_hover = arcade.load_texture(texture_hover)
        texture_pressed = arcade.load_texture(texture_pressed)
        texture_disabled = arcade.load_texture(texture_disabled)

        super().__init__(texture=texture, texture_hovered=texture_hover,
                         texture_pressed=texture_pressed,
                         texture_disabled=texture_disabled,
                         style=styles.normal_button, **kwargs)
