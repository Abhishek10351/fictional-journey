"""
All the sprites needed for the game
"""
import arcade
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(arcade.Sprite):

    """
    Sprite for controlling the player
    """
    def __init__(self):
        super().__init__(filename=":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x=200
        self.center_y=60
        self.change_x = 0
        self.speed = 5
        self.boundary_right = SCREEN_WIDTH
        self.boundary_top = 0
        self.boundary_bottom = SCREEN_HEIGHT
    def update(self):
        self.center_x += self.change_x
        self.left = max(0, self.left)
        self.right = min(self.right, SCREEN_WIDTH)


class Bullet(arcade.Sprite):
    
        """
        Sprite for the bullet
        """
        def __init__(self):
            super().__init__(filename=":resources:images/space_shooter/laserBlue01.png")
            self.change_x = 0
            self.change_y = 0
            self.speed = 5
            self.boundary_right = SCREEN_WIDTH
            self.boundary_top = 0
            self.boundary_bottom = SCREEN_HEIGHT
        def update(self):
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.top = max(0, self.top)