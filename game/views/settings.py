import arcade
import arcade.gui
from datetime import timedelta
from gui_widgets import BackButton, UITextureSlider, TextureToggle
from game_data import fetch, execute
from constants import ASSETS_PATH, GUI_PATH


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings_screen = arcade.gui.UIBoxLayout()

        back_button = BackButton()

        self.music_button = TextureToggle("musicOn.png", "musicOff.png",
                                          value=self.window.bg_music_player.playing)
        self.music_button.on_click = self.set_music

        self.sound_button = TextureToggle(
            "soundOn.png", "soundOff.png", value=True)

        self.sound_control = arcade.gui.UIBoxLayout(
            vertical=False, space_between=40)

        self.label = arcade.gui.UILabel(text="Settings", font_size=30)
        self.slider = UITextureSlider(
            value=self.window.volume, width=300, height=50)

        @self.slider.event("on_change")
        def on_change(value):
            volume = int(value.new_value)
            if (volume != int(value.old_value)):
                self.window.volume = volume

        self.sound_control.add(self.music_button)
        self.sound_control.add(self.sound_button)
        self.settings_screen.add(self.slider)

        self.ui_anchor_layout = arcade.gui.UIAnchorLayout()
        self.ui_anchor_layout.add(
            self.sound_control, anchor_x="center_x", align_y=200)
        self.ui_anchor_layout.add(
            self.settings_screen, anchor_x="center_x", anchor_y="center_y")

        self.manager = arcade.gui.UIManager()
        self.manager.add(self.ui_anchor_layout)
        self.manager.add(back_button)
        self.manager.enable()

        @back_button.event("on_click")
        def on_back(event):
            self.window.show_view(self.window.views["Menu"])

    def on_update(self, delta_time):
        time = self.window.game_level_time
        self.label.text = f"{time.seconds//60}:{time.seconds%60}:{time.microseconds//10000}"

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_show_view(self):
        self.window.game_level_time = timedelta(seconds=0)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def set_music(self, event):
        self.music_button.value = not self.music_button.value
        if self.music_button.value:
            self.window.bg_music_player.play()
        else:
            self.window.bg_music_player.pause()
        execute("UPDATE settings SET music = ?;", self.music_button.value)

    def set_sound(self):
        self.sound_button.value = not self.sound_button.value
        execute("UPDATE settings SET sound = ?;", self.sound_button.value)
