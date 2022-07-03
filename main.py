import arcade
import arcade.gui
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Invader"


class Game(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """
        self.x = 200
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
        self.Player = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", center_x=self.x, center_y=60)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass
    
    def on_draw(self):
        """Called whenever you need to draw your window
        """
        self.clear()
        
        self.Player.draw()
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


if __name__ == "__main__":
    app = Game()
    arcade.run()