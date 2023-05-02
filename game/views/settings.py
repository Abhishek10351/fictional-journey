import arcade
import arcade.gui
from datetime import timedelta
from arcade.gui.widgets.slider import UISlider
import styles
import arcade.gui.widgets


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings_screen = arcade.gui.UIBoxLayout()

        back_button = arcade.gui.UIFlatButton(text="Back", width=200)

        music_button = arcade.gui.UITextureToggle(on_texture=arcade.load_texture("assets/gui/musicOn.png"), off_texture=arcade.load_texture(
            "assets/gui/musicOff.png"), width=50, height=50)
        music_button.with_background(texture=arcade.load_texture(
            "assets/gui/button_textures/blue_button03.png"))
        
        sound_button = arcade.gui.UITextureToggle(on_texture=arcade.load_texture("assets/gui/soundOn.png"), off_texture=arcade.load_texture(
            "assets/gui/soundOff.png"), width=50, height=50)
        sound_button.with_background(texture=arcade.load_texture("assets/gui/button_textures/blue_button03.png"))

        self.sound_control = arcade.gui.UIBoxLayout(vertical = False, space_between=40)

        self.label = arcade.gui.UILabel(text="Settings", font_size=30)
        slider = UISlider(value=50, width=300, height=50)

        self.sound_control.add(music_button)
        self.sound_control.add(sound_button)
        self.settings_screen.add(back_button)
        # self.settings_screen.add(self.label)
        # self.settings_screen.add(slider)


        self.ui_anchor_layout = arcade.gui.UIAnchorLayout()
        self.ui_anchor_layout.add(self.sound_control, anchor_x="center_x", align_y=200)
        self.ui_anchor_layout.add(self.settings_screen, anchor_x="center_x", anchor_y="center_y")
        
        self.manager = arcade.gui.UIManager()
        self.manager.add(self.ui_anchor_layout)
        self.manager.enable()

        @back_button.event("on_click")
        def on_back(event):
            self.window.show_view(self.window.views["Menu"])
        
        @music_button.event("on_click")
        def on_play_music(event):
            self.window.play_music = not self.window.play_music
            

        @sound_button.event("on_click")
        def on_play_sound(event):
            self.window.play_sound = not self.window.play_sound

        
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