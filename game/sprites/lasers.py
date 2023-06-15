from arcade import Sprite
from constants import IMAGES_PATH
import math


class Laser(Sprite):
    """Sprite to move the laser"""

    def __init__(self, image_path, **kwargs):
        self.image_path = IMAGES_PATH / "lasers" / image_path
        super().__init__(self.image_path, **kwargs)

        angle = math.radians(self.angle)

        self.change_x = math.sin(angle) * 5
        self.change_y = math.cos(angle) * 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
