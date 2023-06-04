"""
All the sprites needed for the game
"""
import arcade
from arcade.hitbox import algo_detailed
from constants import SCREEN_WIDTH
from game_data import fetch
from pathlib import Path
from functools import partial


class Player(arcade.Sprite):

    """
    Sprite for controlling the player
    """

    def __init__(self, filename, scale=1, **kwargs):
        file_paths = Path(__file__).parent / "assets" / "images"/ "players"
        super().__init__(arcade.load_texture(
            filename, hit_box_algorithm=algo_detailed), scale, **kwargs)
    
    @property
    def center_laser(self):
        return (self.center_x,self.center_y+self.height)
    @property
    def right_laser(self):
        return (self.left+5, self.center_y+20)
    
    @property
    def left_laser(self):
        return (self.right-5, self.center_y+20)

    def update(self):
        self.center_x += self.change_x
        self.left = max(0, self.left)
        self.right = min(self.right, SCREEN_WIDTH)


class Bullet(arcade.Sprite):

    """
    Sprite for the bullet
    """

    def update(self):
        self.center_y += 5
        self.top = max(0, self.top)


class Enemy1(arcade.Sprite):

    """ Sprite for controlling the Enemy"""

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1  # change enemy direction
            self.center_y -= 10
            self.left = max(0, self.left)
            self.right = min(self.right, SCREEN_WIDTH)


class EnemyBullet(arcade.Sprite):

    """ Sprite for controlling the Enemy"""

    def update(self):
        self.center_y -= 5
        self.top = max(0, self.top)


