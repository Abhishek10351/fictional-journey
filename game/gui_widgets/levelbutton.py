import arcade.gui
import styles


class LevelButton(arcade.gui.UITextureButton):

    def __init__(self, text, is_disabled=False, **kwargs):
        self.is_disabled = is_disabled
        super().__init__(text=text, width=60, height=60,
                         texture=arcade.load_texture(
                             "assets/gui/textures/blue_button02.png"),
                         texture_hovered=arcade.load_texture(
                             "assets/gui/textures/blue_button01.png"),
                         texture_pressed=arcade.load_texture(
                             "assets/gui/textures/blue_button03.png"), style=styles.styled_texture_button,**kwargs)

    def do_render(self, surface):
        super().do_render(surface)
        if self.is_disabled:
            arcade.draw_rectangle_filled(
                0, 0, self.width*2, self.height*2,(204, 204, 204, 100))
