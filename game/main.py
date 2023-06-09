"""
The main file to control the game
"""

import pathlib
import arcade
from constants import *
import views
from window import Window
import pyglet.image
from constants import IMAGES_PATH

if __name__ == "__main__":

    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    window.set_icon(pyglet.image.load(IMAGES_PATH /
                                      "characters"/"aliens"/"enemy.png"))

    window.views = {"Menu": views.Menu(), "LevelSelect": views.LevelSelection(), "LevelUp": views.LevelUpView(),
                    "GameOver": views.GameOverView(), "HowToPlay": views.HowToPlay(),
                    "Settings": views.SettingsView(), "Pause": views.PauseScreen(), "Trophies": views.Trophies()
                    }

    window.levels = [getattr(views.levels, i)()
                     for i in dir(views.levels) if i.startswith("Level")]

    window.show_view(window.views["Menu"])
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.run()
