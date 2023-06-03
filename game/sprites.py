"""
All the sprites needed for the game
"""
import arcade
from arcade.hitbox import algo_detailed
from constants import SCREEN_WIDTH


class Player(arcade.Sprite):

    """
    Sprite for controlling the player
    """

    def __init__(self, filename, scale=1, **kwargs):
        super().__init__(arcade.load_texture(
            filename, hit_box_algorithm=algo_detailed), scale, **kwargs)

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


class EnemyBullet(arcade.Sprite):

    """ Sprite for controlling the Enemy"""

    def update(self):
        self.center_y -= 5
        self.top = max(0, self.top)


class Powerup(arcade.Sprite):

    def __init__(self, powerup_id, **kwargs):
        self.powerup_id = powerup_id
        super().__init__(
            path_or_texture=f"assets/powerups/shields/{powerup_id}", **kwargs)
        self.change_y = -1.5
