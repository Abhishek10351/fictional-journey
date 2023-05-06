import arcade
from gui_widgets import BackButton


class PauseScreen(arcade.View):
    
    def __init__(self):
        super().__init__()
        backbutton = BackButton()

        @backbutton.event
        def on_click(event):
            self.window.show_view(self.window.levels[0])
        self.manager = arcade.gui.UIManager()
        self.manager.add(backbutton)
        self.manager.enable()
    
    def on_show_view(self):
        self.manager.enable()
    
    def on_hide_view(self):
        self.manager.disable()
    
    def on_draw(self):
        self.clear()
        self.manager.draw()
