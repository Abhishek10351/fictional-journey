import arcade
from arcade.gui import UISlider
from arcade.types import Color


class UITextureSlider(UISlider):

    def __init__(
        self,
        style=None,
        **kwargs
    ):
        style = style or UISlider.DEFAULT_STYLE

        super().__init__(style=style, **kwargs)

    def do_render(self, surface):
        surface.clear()
        style: UISlider.UIStyle = self.get_current_style()

        self.prepare_render(surface)

        slider_height = self.height // 4
        slider_left_x = self._x_for_value(self.vmin)
        cursor_center_x = self.value_x

        slider_bottom = (self.height - slider_height) // 2
        arcade.draw_xywh_rectangle_filled(
            slider_left_x - self.x,
            slider_bottom,
            self.width-30,
            slider_height-4,
            Color(94, 104, 117, 255),
        )

        arcade.draw_xywh_rectangle_filled(
            slider_left_x - self.x,
            slider_bottom,
            cursor_center_x - slider_left_x,
            slider_height-4,
            style.filled_bar,
        )

        rel_cursor_x = cursor_center_x - self.x

        if self.pressed:
            thumb = arcade.load_texture(
                "assets/gui/textures/thumb/dotWhite.png")
        elif self.hovered:
            thumb = arcade.load_texture(
                "assets/gui/textures/thumb/dotGreen.png")
        else:
            thumb = arcade.load_texture(
                "assets/gui/textures/thumb/dotBlue.png")

        surface.draw_texture(
            rel_cursor_x - thumb.width // 2, thumb.width/2, thumb.width, thumb.width, thumb)
