"""
The main file to control the game
"""
import random
import arcade
import sprites
import constants


class Game(arcade.Window):
    """Main welcome window
    """

    def __init__(self):
        """Initialize the window
        """
        super().__init__(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
            constants.SCREEN_TITLE)
        self.total_seconds = 0.0
        self.background = None
        self.player = None
        self.red_bullet = None
        self.blue_bullet = None
        self.bullets = None
        self.bullet_list = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        self.bullet_list = arcade.SpriteList()
        self.background = arcade.load_texture("assets/background.jpg")
        self.player = sprites.Player(
            ":resources:images/space_shooter/playerShip1_blue.png",
            center_x=constants.SCREEN_WIDTH/2, center_y=50)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """
        self.total_seconds += delta_time
        self.player.update()
        for i in self.bullet_list:
            if i.top >= constants.SCREEN_HEIGHT:
                i.kill()
        self.bullet_list.update()

    def on_draw(self):
        """Render the screen
        """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.background)

        self.player.draw()
        self.bullet_list.draw()

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.player.change_x = +10
        if symbol == arcade.key.SPACE:
            self.blue_bullet = sprites.Bullet(":resources:/images/space_shooter/laserBlue01.png",
                                              center_x=self.player.center_x,
                                              center_y=self.player.center_y+self.player.height,
                                              hit_box_algorithm="Detailed", angle=90)
            self.red_bullet = sprites.Bullet(":resources:/images/space_shooter/laserRed01.png",
                                             center_x=self.player.center_x,
                                             center_y=self.player.center_y+self.player.height,
                                             hit_box_algorithm="Detailed")
            self.bullets = (self.red_bullet, self.blue_bullet)
            self.bullet_list.append(random.choice(self.bullets))

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0


if __name__ == "__main__":
    app = Game()
    app.setup()
    arcade.run()
