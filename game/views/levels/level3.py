import random
import pathlib
import arcade
import arcade.gui
from arcade.hitbox import algo_detailed
import sprites
from constants import *
from ..level import *


class Level3(Level):

    def __init__(self):
        """Initialize the window
        """
        super().__init__()
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"), width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.no_of_enemies = 20

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()
        super().setup()

        self.player = sprites.Player(
            arcade.load_texture(pathlib.Path("assets/images/players/player_blue.png"),
                                hit_box_algorithm=algo_detailed()),
            center_x=SCREEN_WIDTH/2, center_y=50)

        self.enemy_bullets_shooted = 0
        total = 0
        while total < self.no_of_enemies:
            enemy = sprites.Enemy1("assets/images/aliens/enemyGreen.png", scale=0.5, center_x=random.randint(
                0, 525), center_y=random.randint(350, 525))
            enemy_x_change = list(range(-5, 5))
            enemy_x_change.remove(0)
            enemy.change_x = random.choice(enemy_x_change)
            if not enemy.collides_with_list(self.enemy_list) or enemy.left > 0:
                total += 1
                self.enemy_list.append(enemy)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
                """
        seconds = self.total_time.total_seconds()
        if seconds > self.enemy_bullets_shooted:
            enemy = random.choice(self.enemy_list)
            enemy_bullet = sprites.EnemyBullet("assets/images/lasers/Red.png",
                                               center_x=enemy.center_x,
                                               center_y=enemy.center_y, angle=180)
            self.enemy_bullets.append(enemy_bullet)
            self.enemy_bullets_shooted += 1

        if self.player.collides_with_list(self.enemy_bullets):
            self.player.kill()
            self.window.views["GameOver"].setup()
            self.window.show_view(self.window.views["GameOver"])
        for i in self.bullets:
            if i.top >= SCREEN_HEIGHT or i.collides_with_list(self.enemy_list):
                for j in i.collides_with_list(self.enemy_list):
                    j.kill()
                    if self.window.play_sound:
                        arcade.Sound("assets/sounds/hit.wav").play(volume=0.20)
                    self.score += 1
                i.kill()
        for i in self.enemy_list:
            if i.bottom <= self.player.top:
                view = self.window.views["GameOver"]
                self.window.show_view(view)
            if i.left < 0 or i.right > SCREEN_WIDTH:
                i.change_x *= -1  # change enemy direction
                i.change_y = -10
                i.left = max(0, i.left)
                i.right = min(i.right, SCREEN_WIDTH)

        if len(self.enemy_list) == 0:
            if self.window.levels_completed < self.window.current_level:
                self.window.levels_completed = 1
            self.window.show_view(self.window.views["LevelUp"])
        for i in self.enemy_list:
            i.change_y = 0
        super().on_update(delta_time)

    def on_draw(self):
        """Render the screen
        """
        self.clear()
        super().on_draw()

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        super().on_key_press(symbol, modifiers)
        if symbol == arcade.key.LEFT:
            self.player.change_x = -10
        if symbol == arcade.key.RIGHT:
            self.player.change_x = +10
        if symbol == arcade.key.SPACE:
            bullet = sprites.Bullet(f"assets/images/lasers/Blue.png",
                                    center_x=self.player.center_x,
                                    center_y=self.player.center_y+self.player.height,
                                    hit_box_algorithm="Detailed")
            if not bullet.collides_with_list(self.bullets):
                self.bullets.append(bullet)
                if self.window.play_sound:
                    arcade.Sound("assets/sounds/laser.wav").play(volume=0.5)

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
