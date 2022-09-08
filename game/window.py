import arcade


class Window(arcade.Window):
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)
        self.total_levels = 2
        self.level = 1
        self.bg_music = arcade.Sound(
            "assets/music/funkyrobot.mp3")
        self.completed = False
