import random
import pathlib
import arcade
import arcade.gui
import sprites
from constants import *
from ..level import *


class Level1(Level):

    def __init__(self):
        """Initialize the window
        """
        super().__init__()
        self.no_of_enemies = 10

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        super().setup()

        self.player = sprites.Player(
            "assets/images/players/player_blue.png", center_x=SCREEN_WIDTH/2, center_y=50)
        self.create_enemies(
            sprites.Enemy1, "assets/images/aliens/enemy.png", self.no_of_enemies)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """
        for i in self.bullets:
            if i.top >= SCREEN_HEIGHT or i.collides_with_list(self.enemy_list):
                for j in i.collides_with_list(self.enemy_list):
                    j.kill()
                    arcade.Sound(
                        "assets/sounds/hit.wav").play(volume=self.window.volume)
                    self.score += 100
                i.kill()
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
            self.player.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.player.change_x = +10
        if symbol == arcade.key.SPACE:
            colour = random.choice(('Red', 'Blue'))
            bullet = sprites.Bullet(f"assets/images/lasers/{colour}.png",
                                    center_x=self.player.center_x,
                                    center_y=self.player.center_y+self.player.height)
            if not bullet.collides_with_list(self.bullets):
                self.bullets.append(bullet)
                arcade.Sound("assets/sounds/laser.wav").play(volume=0.2)

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
