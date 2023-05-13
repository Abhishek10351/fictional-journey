import arcade
import arcade.gui
from datetime import timedelta
from gui_widgets import BackButton
from gui_textures.slider import UITextureSlider

class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings_screen = arcade.gui.UIBoxLayout()

        back_button = BackButton()

        self.music_button = arcade.gui.UITextureToggle(on_texture=arcade.load_texture("assets/gui/musicOn.png"), off_texture=arcade.load_texture(
            "assets/gui/musicOff.png"), width=50, height=50)
        self.music_button.with_background(texture=arcade.load_texture(
            "assets/gui/textures/blue_button03.png"))
        
        self.sound_button = arcade.gui.UITextureToggle(on_texture=arcade.load_texture("assets/gui/soundOn.png"), off_texture=arcade.load_texture(
            "assets/gui/soundOff.png"), width=50, height=50, value=True)
        self.sound_button.with_background(texture=arcade.load_texture("assets/gui/textures/blue_button03.png"))

        self.sound_control = arcade.gui.UIBoxLayout(vertical = False, space_between=40)

        self.label = arcade.gui.UILabel(text="Settings", font_size=30)
        slider = UITextureSlider(value=50, width=300, height=50)

        self.sound_control.add(self.music_button)
        self.sound_control.add(self.sound_button)
        self.settings_screen.add(slider)


        self.ui_anchor_layout = arcade.gui.UIAnchorLayout()
        self.ui_anchor_layout.add(self.sound_control, anchor_x="center_x", align_y=200)
        self.ui_anchor_layout.add(self.settings_screen, anchor_x="center_x", anchor_y="center_y")
        
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
