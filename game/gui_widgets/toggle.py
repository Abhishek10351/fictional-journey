import arcade.gui
from constants import TEXTURES_PATH, ICON_PATH

bg_dir = TEXTURES_PATH / "buttons" / "small"


class TextureToggle(arcade.gui.UITextureToggle):
    def __init__(self, on_texture, off_texture, value=False):
        on_texture = ICON_PATH / on_texture
        off_texture = ICON_PATH / off_texture
        super().__init__(on_texture=arcade.load_texture(on_texture),
                         off_texture=arcade.load_texture(off_texture),
                         value=value, height=50, width=50)

        if self.disabled:
            bg = arcade.load_texture(bg_dir/"metalPanel.png")
        else:
            bg = arcade.load_texture(bg_dir/"blue_button01.png")

        self.with_background(texture=bg)

    def do_render(self, surface):
        self.prepare_render(surface)
        tex = self.normal_on_tex if self.value else self.normal_off_tex
        if self.pressed:
            tex = self.pressed_on_tex if self.value else self.pressed_off_tex
        elif self.hovered:
            tex = self.hover_on_tex if self.value else self.hover_off_tex
        surface.draw_texture(0, 0, self.content_width,
                             self.content_height, tex)

        if self.disabled:
            bg = arcade.load_texture(bg_dir/"metalPanel.png")
        elif self.pressed:
            bg = arcade.load_texture(bg_dir/"blue_button03.png")
        elif self.hovered:
            bg = arcade.load_texture(bg_dir/"blue_button02.png")
        else:
            bg = arcade.load_texture(bg_dir/"blue_button01.png")

        self.with_background(texture=bg)
