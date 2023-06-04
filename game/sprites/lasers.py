from arcade import Sprite

class Laser(Sprite):

    """
    Sprite for the laser
    """

    def update(self):
        self.center_y += 5
        self.top = max(0, self.top)