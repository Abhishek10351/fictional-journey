import arcade
from arcade.gui import UISlider


class UITextureSlider(UISlider):
    """
    A slider that supports textures
    """

    def __init__(
        self,
        thumb=arcade.load_texture("assets/gui/textures/thumb.png"),
        style=None,
        **kwargs
    ):
        self.thumb = thumb
        style = style or UISlider.DEFAULT_STYLE

        super().__init__(style=style, **kwargs)

    def do_render(self, surface):
        style: UISlider.UIStyle = self.get_current_style()

        self.prepare_render(surface)

        # surface.draw_rectangle(0, 0, self.width, self.height, self.bar)
        arcade.draw_rectangle_filled(
            0, 0, self.width*2, self.height*2, arcade.color.WHITE)

        slider_height = self.height // 4
        slider_left_x = self._x_for_value(self.vmin)
        cursor_center_x = self.value_x

        slider_bottom = (self.height - slider_height) // 2

        arcade.draw_xywh_rectangle_filled(
            slider_left_x - self.x,
            slider_bottom,
            cursor_center_x - slider_left_x,
            slider_height,
            style.filled_bar,
        )

        rel_cursor_x = cursor_center_x - self.x
        surface.draw_texture(
            x=rel_cursor_x - self.thumb.width // 4 + 2,
            y=0,
            width=self.thumb.width,
            height=self.height,
            tex=self.thumb,
        )
