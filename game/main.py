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
import pyglet.image
from pathlib import Path

if __name__ == "__main__":
    
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_icon(pyglet.image.load(
        Path('assets/images/aliens/enemy.png')))
    window.views = {"Menu": views.Menu(), "LevelUp": views.LevelUpView(), 
    "GameOver": views.GameOverView(), "HowToPlay": views.HowToPlay(), "Settings": views.SettingsView(), 
    "Pause": views.PauseScreen()}
    window.show_view(window.views["Menu"])
    window.levels = [getattr(views.levels, i)()
                     for i in dir(views.levels) if i.startswith("Level")]
    arcade.set_background_color(arcade.color.SKY_BLUE)

    try:
        arcade.run()
    except KeyboardInterrupt:
        arcade.exit()
    except Exception as e:
        print(e)
        arcade.exit()

# https://trello.com/b/oAkhlW4y/space-invaders
