from arcade import Sprite
from constants import IMAGES_PATH, SCREEN_WIDTH, SCREEN_HEIGHT
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
        # Remove the sprite if it goes off-screen
        if (self.top < 0 or self.bottom >SCREEN_HEIGHT) or (self.left > SCREEN_WIDTH or self.right<0):
            self.kill()
