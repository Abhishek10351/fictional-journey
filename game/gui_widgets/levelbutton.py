import arcade
import styles
from game_data import fetch
from .buttons import TextureButton


class LevelButton(TextureButton):

    def __init__(self, text, **kwargs):
        super().__init__(text=text, width=60, height=60,
                         texture=arcade.load_texture(
                             "assets/gui/textures/blue_button02.png"),
                         texture_hovered=arcade.load_texture(
                             "assets/gui/textures/blue_button01.png"),
                         texture_pressed=arcade.load_texture(
                             "assets/gui/textures/blue_button03.png"), style=styles.styled_texture_button, **kwargs)

    def do_render(self, surface):
        self.prepare_render(surface)
        unlocked = fetch(
            "SELECT unlocked FROM levels WHERE level = ?", int(self.text))[0]

        style = self.get_current_style()
        if not unlocked:
            style = self.style["disabled"]

        self.apply_style(style)

        current_state = self.get_current_state()
        current_texture = self._textures.get(current_state)
        if unlocked:
            surface.draw_texture(
                0, 0, self.width, self.height, current_texture)
        else:
            surface.draw_texture(0, 0, self.width, self.height, arcade.load_texture(
                "assets/gui/textures/metalpanel.png"))
