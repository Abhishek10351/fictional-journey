import arcade
import arcade.gui


class BackButton(arcade.gui.UITextureButton):
    def __init__(self, **kwargs):
        super().__init__(
            # Set the bottom texture for the button
            texture=arcade.load_texture(
                'assets/gui/arrowLeftBlack.png'),
            # Set the texture for the button when it's pressed
            texture_hovered=arcade.load_texture(
                'assets/gui/arrowLeftWhite.png'),
            texture_pressed=arcade.load_texture(
                'assets/gui/arrowLeftBlack.png'),
            width=50, height=50
        )

    def on_update(self, dt):
        if self.pressed:
            self.with_background(color=arcade.color.WHITE)
        elif self.hovered:
            self.with_background(color=arcade.color.BLACK)
        else:
            self.with_background(color=arcade.color.WHITE)
