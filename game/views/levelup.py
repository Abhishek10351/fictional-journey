import arcade
from constants import *


class LevelUpView(arcade.View):
    """ View to show when a level is completed """

    # todo add replay buttons, show stars

    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.manager = arcade.gui.UIManager()
        self.anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout(
            anchor_x="center", anchor_y="center")

    def setup(self):
        self.manager.clear()
        self.anchor_layout.clear()
        self.anchor_layout.add(self.text)
        self.manager.add(self.anchor_layout)

    @property
    def level(self):
        return self.window.levels[self.window.current_level-1]

    @property
    def message(self):
        return (f"Level {self.window.current_level} complete.\n"
                f"Score: {self.level.score}\n"
                f"High Score: {self.level.highscore}"
                )

    @property
    def text(self):
        return arcade.gui.UILabel(width=400, text=self.message, font_size=20,
                                  font_name="Kenney Future", multiline=True,
                                  text_color=(239, 35, 60),
                                  align="left")

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        self.window.show_view(self.window.views["LevelSelect"])

    def on_show_view(self):
        self.manager.enable()
        if self.window.controller:
            self.window.controller.push_handlers(self)


    def on_hide_view(self):
        self.manager.disable()
        if self.window.controller:
            self.window.controller.remove_handlers(self)
    def on_button_press(self, controller, button):
        if button in ["b", "back"]:
            self.window.show_view(self.window.views["LevelSelect"])
        elif button in ["start" "x"]:
            self.window.levels[self.window.current_level-1].setup()
            self.window.show_view(self.window.levels[self.window.current_level-1])
        # elif button in ["a"]:
        #     if self.window.current_level < self.window.total_levels:
        #         self.window.current_level += 1
        #         self.window.levels[self.window.current_level-1].setup()
        #         self.window.show_view(self.window.levels[self.window.current_level-1])