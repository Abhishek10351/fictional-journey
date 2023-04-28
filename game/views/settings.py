import arcade
import arcade.gui
from datetime import timedelta
from arcade.gui.widgets.slider import UISlider
import styles
import arcade.gui.widgets

class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings_screen = arcade.gui.widgets.layout.UIBoxLayout()

        back_button = arcade.gui.widgets.buttons.UIFlatButton(text="Back", width=200)
        #texture_test_button = arcade.gui.widgets.buttons.UITextureButton(text="lol",texture=arcade.load_texture("assets/gui/buttons/blue_button08.png"), texture_hovered=arcade.load_texture("assets/gui/buttons/blue_button07.png"), texture_pressed=arcade.load_texture("assets/gui/buttons/blue_button09.png"),width=50, height=50)
        a = arcade.TextureAtlas((50,50), textures=[arcade.load_texture("assets/gui/musicOn.png"),arcade.load_texture("assets/gui/button_textures/blue_button03.png")])

        music_button = arcade.gui.widgets.buttons.UITextureButton(texture=arcade.load_texture("assets/gui/musicOn.png"), texture_hovered=arcade.load_texture(
            "assets/gui/musicOn.png"), texture_pressed=arcade.load_texture("assets/gui/musicOff.png"), width=50, height=50, style=styles.dark_button)
        # music_button.do_render(surface)
        music_button.with_background(texture=arcade.load_texture(
            "assets/gui/button_textures/blue_button03.png"))
        sound_button = arcade.gui.widgets.buttons.UITextureButton(texture=arcade.load_texture("assets/gui/soundOn.png"), texture_hovered=arcade.load_texture("assets/gui/soundOn.png"), texture_pressed=arcade.load_texture("assets/gui/soundOff.png"), width=50, height=50)

        self.sound_control = arcade.gui.widgets.layout.UIBoxLayout(vertical = False)


        self.label = arcade.gui.widgets.text.UILabel(text="Settings", font_size=30)
        slider = UISlider(value=50, width=300, height=50)

        self.sound_control.add(music_button)
        self.sound_control.add(sound_button)
        self.settings_screen.add(back_button)
        self.settings_screen.add(self.label)
        # self.settings_screen.add(texture_test_button)
        self.settings_screen.add(slider)


        self.ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
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
            if self.window.play_music:
                music_button.texture = arcade.load_texture("assets/gui/musicOn.png")
                music_button.texture_hovered = arcade.load_texture("assets/gui/musicOn.png")
                music_button.texture_pressed = arcade.load_texture("assets/gui/musicOff.png")
            else:
                music_button.texture = arcade.load_texture("assets/gui/musicOff.png")
                music_button.texture_hovered = arcade.load_texture("assets/gui/musicOff.png")
                music_button.texture_pressed = arcade.load_texture("assets/gui/musicOn.png")

        @sound_button.event("on_click")
        def on_play_sound(event):
            self.window.play_sound = not self.window.play_sound
            if self.window.play_sound:
                sound_button.texture = arcade.load_texture("assets/gui/soundOn.png")
                sound_button.texture_hovered = arcade.load_texture("assets/gui/soundOn.png")
                sound_button.texture_pressed = arcade.load_texture("assets/gui/soundOff.png")
            else:
                sound_button.texture = arcade.load_texture("assets/gui/soundOff.png")
                sound_button.texture_hovered = arcade.load_texture("assets/gui/soundOff.png")
                sound_button.texture_pressed = arcade.load_texture("assets/gui/soundOn.png")

        
    def on_update(self, delta_time):
        time = self.window.game_level_time
        self.label.text = f"{time.seconds//60}:{time.seconds%60}:{time.microseconds//1000}"

    def on_draw(self):
        self.clear()
        self.manager.draw()
    
    def on_show_view(self):
        self.window.game_level_time = timedelta(seconds=0)
        self.manager.enable()
    
    def on_hide_view(self):
        self.manager.disable()