import arcade
import pyglet.media
from datetime import timedelta
from views import levels
from game_data import fetch


class Window(arcade.Window):
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)
        self.total_time = timedelta(seconds=0.0)

        self.total_levels = len([i
                                 for i in dir(levels) if i.startswith("Level")])
        self.levels_completed = 0  # the last level completed
        self.current_level = 1  # the level currently played
        self.bg_music = arcade.load_sound("assets/music/funkyrobot.mp3")
        self.bg_music_player = self.bg_music.play(volume=1)
        self.completed = False
        self.game_level_time = timedelta(seconds=0.0)

    def on_update(self, delta_time):
        self.total_time += timedelta(seconds=delta_time)
        self.game_level_time += timedelta(seconds=delta_time)

    @property
    def play_sound(self):
        return fetch("SELECT sound FROM settings;")[0]

    @property
    def volume(self):
        return fetch("SELECT volume FROM settings;")[0]
