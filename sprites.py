"""
All the sprites needed for the game
"""
import arcade
from constants import SCREEN_WIDTH


class Player(arcade.Sprite):
    """ 
    Sprite for controlling the player
    """

    def update(self):
        self.center_x += self.change_x
        self.left = max(0, self.left)
        self.right = min(self.right, SCREEN_WIDTH)
