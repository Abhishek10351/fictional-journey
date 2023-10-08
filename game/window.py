import arcade
import pyglet.media
from datetime import timedelta
from views import levels
from game_data import fetch, execute


class Window(arcade.Window):
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)
        self.total_time = timedelta(seconds=0.0)

        self.total_levels = len(
            [i for i in dir(levels) if i.startswith("Level")])
        self.levels = [
            getattr(levels, f"Level{i}")()
            for i in range(1, self.total_levels+1)]
        self.current_level = 1  # the level currently played
        self.bg_music = arcade.load_sound("assets/music/funkyrobot.mp3")
        self.bg_music_player = self.bg_music.play(
            volume=self.volume/100, loop=True)
        if fetch("SELECT music FROM settings;")[0] == 0:
            self.bg_music_player.pause()
        self.game_level_time = timedelta(seconds=0.0)

    def on_update(self, delta_time):
        self.total_time += timedelta(seconds=delta_time)
        self.game_level_time += timedelta(seconds=delta_time)

    @property
    def sound(self):
        return fetch("SELECT sound FROM settings;")[0]

    @property
    def volume(self):
        return fetch("SELECT volume FROM settings;")[0]

    @volume.setter
    def volume(self, value):
        execute("UPDATE settings SET volume = ?;", value)
        self.bg_music_player.volume = value/100
