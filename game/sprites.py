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
        powerup_object = fetch(
            "SELECT * FROM powerups WHERE id = ?", powerup_id)
        self.name = powerup_object[1]
        self.description = powerup_object[2]
        self.duration = powerup_object[3]
        self.rarity = powerup_object[4]
        self.image = Path(__file__).parent / powerup_object[5]

        super().__init__(
            path_or_texture=self.image, **kwargs)
        self.change_y = -1.5

    def use(self, view):
        if self.name == "Shield":
            self.use_shield(view)

    def use_shield(self, view):
        shield_id = int(self.powerup_id[-1])
        if shield_id < 4 and shield_id:
            if view.shield < shield_id:
                view.shield = shield_id
                arcade.schedule_once(
                    partial(self.reset_shield, view=view), self.duration)
        else:
            view.shield = 0

    def reset_shield(self, delta_time: float, view):
        view.shield = 0
        arcade.unschedule(self.reset_shield)
