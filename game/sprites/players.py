from pathlib import Path
import arcade
from arcade.hitbox import algo_detailed
from constants import SCREEN_WIDTH, IMAGES_PATH
import math


base_file_path = IMAGES_PATH / "characters" / "players"


class Player(arcade.Sprite):

    """
    Sprite for controlling the player
    """

    def __init__(self, filename, scale=1, **kwargs):
        file_path = base_file_path / filename
        super().__init__(arcade.load_texture(
            file_path, hit_box_algorithm=algo_detailed), scale, **kwargs)

    @property
    def center_laser(self):
        return (self.center_x, self.center_y+self.height)

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


class Player2(arcade.Sprite):

    """
    Player sprite that can rotate
    """

    def __init__(self, filename, scale=1, **kwargs):
        file_path = base_file_path / filename
        super().__init__(arcade.load_texture(
            file_path, hit_box_algorithm=algo_detailed), scale, **kwargs)

        self.laser_points = [self.left+5, self.right-5]

    @property
    def center_laser(self):
        x = self.center_x + self.height * math.cos(math.radians(self.angle))
        y = self.center_y + self.height * math.sin(math.radians(self.angle))
        return (x, y)

    @property
    def right_laser(self):

        x, y = arcade.math.rotate_point(
            self.laser_points[1], self.center_y+20, self.center_x, self.center_y,  self.angle)

        return (x, y)

    @property
    def left_laser(self):

        x, y = arcade.math.rotate_point(
            self.laser_points[0], self.center_y+20, self.center_x, self.center_y,  self.angle)

        return (x, y)

    def update(self):
        if self.angle <= 90:
            self.angle += self.change_angle
        else:
            self.angle = 90

        if self.angle >= -90:
            self.angle += self.change_angle
        else:
            self.angle = -90
