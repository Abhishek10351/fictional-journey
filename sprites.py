"""
All the sprites needed for the game
"""
import arcade
from constants import SCREEN_WIDTH


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left <= 0:
            self.left = max(0, self.left)
        if self.right >= SCREEN_WIDTH:
            self.right = min(self.right, SCREEN_WIDTH)
