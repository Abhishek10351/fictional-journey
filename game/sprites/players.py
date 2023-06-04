from pathlib import Path
import arcade
from arcade.hitbox import algo_detailed
from constants import SCREEN_WIDTH

class Player(arcade.Sprite):

    """
    Sprite for controlling the player
    """

    def __init__(self, filename, scale=1, **kwargs):
        file_paths = Path(__file__).parent / "assets" / "images" / "players"
        super().__init__(arcade.load_texture(
            filename, hit_box_algorithm=algo_detailed), scale, **kwargs)

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
