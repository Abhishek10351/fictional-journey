from arcade import Sprite
from constants import SCREEN_WIDTH, IMAGES_PATH


class Enemy1(Sprite):

    """ Sprite for controlling the Enemy"""

    def __init__(self, image_path, **kwargs):
        self.image_path = IMAGES_PATH / "characters" / "aliens" / image_path
        super().__init__(self.image_path, **kwargs)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1  # change enemy direction
            self.center_y -= 10
            self.left = max(0, self.left)
            self.right = min(self.right, SCREEN_WIDTH)
