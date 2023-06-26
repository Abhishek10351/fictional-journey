import random
import pathlib
import arcade
import arcade.gui
from arcade.hitbox import algo_detailed
import sprites
from constants import *
from ..level import *


class Level4(Level):

    def __init__(self):
        """Initialize the window
        """
        super().__init__()
        self.no_of_enemies = 10
        self.points = arcade.SpriteList()

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        super().setup()

        self.player = sprites.Player2("player_green.png",
                                     center_x=SCREEN_WIDTH/2, center_y=50)

        self.enemy_lasers_shooted = 0
        self.create_enemies(
            sprites.Enemy1, "enemyGreen.png", self.no_of_enemies, 0.5)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """

        self.check_enemy_hit(powerups=["shield"])
        for i in self.enemy_list:
            if i.bottom <= self.player.top:
                self.game_over()

        if len(self.enemy_list) == 0:
            self.level_complete()
        super().on_update(delta_time)

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        super().on_key_press(symbol, modifiers)
        if symbol == arcade.key.LEFT:
            self.player.change_x = -5
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5
        
        if symbol == arcade.key.UP:
            self.player.change_angle = 1  
        if symbol == arcade.key.DOWN:
            self.player.change_angle = -1

        if symbol == arcade.key.SPACE:
            self.shoot_laser()

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if symbol in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0
        if symbol in [ arcade.key.UP, arcade.key.DOWN]:
            self.player.change_angle = 0
