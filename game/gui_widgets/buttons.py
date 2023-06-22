import arcade.gui


class TextureButton(arcade.gui.UITextureButton):
    def __init__(self, text="", font_size=12,
                 font_name="Kenney Future", **kwargs):
        self.font_size = font_size
        self.font_name = font_name
        super().__init__(text=text, **kwargs)



    def apply_style(self, style):

        font_color = style.get("font_color")

        font_name_changed = self._label.label.font_name != self.font_name
        font_size_changed = self._label.label.font_size != self.font_size
        font_color_changed = self._label.label.color != font_color

        if font_name_changed or font_size_changed or font_color_changed:

            with self._label.label:
                self._label.label.font_name = self.font_name
                self._label.label.font_size = self.font_size
                self._label.label.color = font_color

            self._label.fit_content()
            self.ui_label.rect = self.ui_label.rect.max_size(
                self.content_width, self.content_height)
