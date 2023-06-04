from arcade import Sprite
from constants import SCREEN_WIDTH

class Enemy1(Sprite):

    """ Sprite for controlling the Enemy"""

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1  # change enemy direction
            self.center_y -= 10
            self.left = max(0, self.left)
            self.right = min(self.right, SCREEN_WIDTH)