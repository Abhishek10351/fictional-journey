"""
The main file to control the game
"""
import random
import pathlib
import arcade
import arcade.gui
import sprites
from constants import *
import views
import styles
from window import Window


if __name__ == "__main__":
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = views.StartScreen()
    window.views = {"StartScreen": start_view, "Game": start_view, "LevelUp": views.LevelUpView(
    ), "GameOver": views.GameOverView(), "HowToPlay": views.HowToPlay()}
    window.show_view(window.views["StartScreen"])
    window.levels = [getattr(views.levels, i)()  for i in dir(views.levels) if i.startswith("Level")]
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.run()
