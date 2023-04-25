import arcade
import arcade.gui


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings_screen = arcade.gui.widgets.layout.UIBoxLayout()
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # self
    def on_draw(self):
        self.clear()
        self.manager.draw()
    
    def on_show_view(self):
        self.manager.enable()
    
    def on_hide_view(self):
        self.manager.disable()