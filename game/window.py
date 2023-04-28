import arcade
import pyglet.media
from datetime import timedelta


class Window(arcade.Window):
    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)
        self.total_time = timedelta(seconds=0.0)
        self.total_levels = 2
        self.levels_completed = 0  # the last level completed
        self.current_level = 1  # the level currently played
        self.bg_music = pyglet.media.Player()
        self.bg_music.queue(pyglet.media.load("assets/music/funkyrobot.mp3"))
        self.completed = False
        self.game_level_time = timedelta(seconds=0.0)
        self.volume = 0.5
        self.play_music = True
        self.play_sound = True

    def on_update(self, delta_time):
        self.total_time += timedelta(seconds=delta_time)
        self.game_level_time += timedelta(seconds=delta_time)
