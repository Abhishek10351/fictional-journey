import arcade
import arcade.gui
import Sprites
from constants import *


class Game(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
        self.total_seconds = 0.0
        self.background = arcade.load_texture("assets/background.jpg")
        self.Player = Sprites.Player(":resources:images/space_shooter/playerShip1_blue.png", center_x=200, center_y=60)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.total_seconds += delta_time
        self.Player.update()
    def on_draw(self):
        """Called whenever you need to draw your window
        """
        self.clear() 
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
      
        self.Player.draw()
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.LEFT and self.Player.left >=0:
            self.Player.change_x = -10
        if key == arcade.key.RIGHT:
            self.Player.change_x = +10

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT:
            self.Player.change_x = 0
        if key == arcade.key.RIGHT:
            self.Player.change_x = 0


if __name__ == "__main__":
    app = Game()
    arcade.run()