from arcade import Sprite

class EnemyLaser(Sprite):

    """ Sprite for controlling the Enemy Laser"""

    def update(self):
        self.center_y -= 5
        self.top = max(0, self.top)
