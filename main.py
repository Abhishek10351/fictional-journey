"""
The main file to control the game
"""
import random
import pathlib
import arcade
import sprites
import constants

NO_OF_ENEMIES = 10


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
        self.score = 0
        self.player = None
        self.red_bullet = None
        self.blue_bullet = None
        self.bullet_list = None
        self.enemy = None
        self.enemy_list = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        self.background = arcade.load_texture("assets/images/background.jpg")
        self.player = sprites.Player(
            "assets/images/player.png",
            center_x=constants.SCREEN_WIDTH/2, center_y=50)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        total = 0
        while total < NO_OF_ENEMIES:
            self.enemy = sprites.Enemy("assets/images/enemy.png", center_x=random.randint(
                0, 525), center_y=random.randint(350, 525))
            enemy_x_change = list(range(-5, 5))
            enemy_x_change.remove(0)
            self.enemy.change_x = random.choice(enemy_x_change)
            if not self.enemy.collides_with_list(self.enemy_list) or self.enemy.left > 0:
                total += 1
                self.enemy_list.append(self.enemy)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """
        self.total_seconds += delta_time
        self.player.update()
        for i in self.bullet_list:
            if i.top >= constants.SCREEN_HEIGHT or i.collides_with_list(self.enemy_list):
                for j in i.collides_with_list(self.enemy_list):
                    j.kill()
                    self.score += 1
                i.kill()
        for i in self.enemy_list:
            if i.left < 0 or i.right > constants.SCREEN_WIDTH:
                i.change_x *= -1  # change enemy direction
                i.change_y = -5            
                i.left = max(0,i.left)
                i.right = min(i.right, constants.SCREEN_WIDTH)
        self.enemy_list.update()
        self.bullet_list.update()
        for i in self.enemy_list:
            i.change_y = 0

    def on_draw(self):
        """Render the screen
        """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.background)

        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.player.change_x = +10
        if symbol == arcade.key.SPACE:
            self.blue_bullet = sprites.Bullet("assets\images\laserBlue.png",
                                              center_x=self.player.center_x,
                                              center_y=self.player.center_y+self.player.height,
                                              hit_box_algorithm="Detailed", angle=90)
            self.red_bullet = sprites.Bullet("assets\images\laserRed.png",
                                             center_x=self.player.center_x,
                                             center_y=self.player.center_y+self.player.height,
                                             hit_box_algorithm="Detailed")
            bullet = random.choice((self.red_bullet, self.blue_bullet))
            if not bullet.collides_with_list(self.bullet_list):
                self.bullet_list.append(bullet)

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
