import random
import pathlib
import arcade
import arcade.gui
from arcade.hitbox import algo_detailed
import sprites
from constants import *
from ..level import *


class Level3(Level):

    def __init__(self):
        """Initialize the window
        """
        super().__init__()
        self.no_of_enemies = 10

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        super().setup()

        self.player = sprites.Player("player_blue.png",
                                     center_x=SCREEN_WIDTH/2, center_y=50)

        self.enemy_lasers_shooted = 0
        self.create_enemies(
            sprites.Enemy1, "enemyGreen.png", self.no_of_enemies, 0.5)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """
        seconds = self.total_time.total_seconds()

        if seconds > self.enemy_lasers_shooted:
            enemy = random.choice(self.enemy_list)
            enemy_laser = sprites.Laser(
                "Red.png",
                center_x=enemy.center_x,
                center_y=enemy.bottom, angle=180)
            self.enemy_lasers.append(enemy_laser)
            self.enemy_lasers_shooted += 1

        self.check_player_hit()
        self.check_enemy_hit(powerups=["shield"])
        for i in self.enemy_list:
            if i.bottom <= self.player.top:
                self.game_over()

        if len(self.enemy_list) == 0:
            self.level_complete()
        for i in self.enemy_list:
            i.change_y = 0
        super().on_update(delta_time)

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        super().on_key_press(symbol, modifiers)
        if symbol == arcade.key.LEFT:
            self.player.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.player.change_x = +10
        if symbol == arcade.key.SPACE:
            self.shoot_laser()

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
