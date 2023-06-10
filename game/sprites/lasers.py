from arcade import Sprite
from constants import IMAGES_PATH
import math


class Laser(Sprite):

    """
    Sprite for the laser
    """

    def __init__(self, image_path, **kwargs):
        self.image_path = IMAGES_PATH / "lasers" / image_path
        super().__init__(self.image_path, **kwargs)

    def update(self):
        self.center_y += 5
        self.top = max(0, self.top)


class Laser2(Sprite):
    """ Laser  that shoots at an angle"""

    def __init__(self, image_path, **kwargs):
        self.image_path = IMAGES_PATH / "lasers" / image_path
        super().__init__(self.image_path, **kwargs)

        angle = math.radians(self.angle)

        self.change_x = math.sin(angle) * 5
        self.change_y = math.cos(angle) * 5
