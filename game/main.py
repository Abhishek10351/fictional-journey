"""
The main file to control the game
"""
import random
import pathlib
import arcade
import arcade.gui
import pymunk
import sprites
from constants import *
import views
import styles


arcade.configure_logging(level=30)


class GameView(arcade.View):
    """Main welcome window
    """

    def __init__(self):
        """Initialize the window
        """
        super().__init__()
        self.total_seconds = 0.0
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"), width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.bg_music = arcade.Sound(
            "assets/music/funkyrobot.mp3")
        self.space = pymunk.Space()
        self.manager = None
        self.score = 0
        self.player = None
        self.bullet_list = None
        self.enemy = None
        self.enemy_list = None
        self.no_of_enemies = None
        self.current_stage = "Start"
        self.level = 1
        self.change = False

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.start_screen = arcade.gui.UIBoxLayout()
        self.start_screen.add(start_button.with_space_around(bottom=20))
        self.how_to_play = arcade.gui.UIFlatButton(text="How to Play", width=200)
        self.how_to_play.on_click = self.on_how_to_play_click
        self.start_screen.add(self.how_to_play.with_space_around(bottom=20))
        quit_button = arcade.gui.UIFlatButton(text="Exit", width=200, style=styles.danger_button)
        start_button.on_click = self.on_start_button_click
        self.start_screen.add(quit_button)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        @quit_button.event
        def on_click(event):
            arcade.exit()

    def on_start_button_click(self, event):
        self.current_stage = 1
        self.setup()
        self.change = False
    
    def on_how_to_play_click(self, event):
        self.current_stage = "Start"
        self.window.show_view(self.window.views["HowToPlay"])

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.clear()

        if self.current_stage == "Start":
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center_x",
                    anchor_y="center_y",
                    child=self.start_screen)
            )
        elif self.current_stage == 1:
            self.no_of_enemies = 10
            self.player = sprites.Player(
                "assets/images/player.png",
                center_x=SCREEN_WIDTH/2, center_y=50)
            self.bullet_list = arcade.SpriteList()
            self.enemy_list = arcade.SpriteList()
            total = 0
            while total < self.no_of_enemies:
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
        if self.current_stage == 1:
            self.player.update()
            for i in self.bullet_list:
                if i.top >= SCREEN_HEIGHT or i.collides_with_list(self.enemy_list):
                    for j in i.collides_with_list(self.enemy_list):
                        j.kill()
                        sound = arcade.Sound("assets/sounds/hit.wav")
                        sound.volume = 0.4
                        sound.play()
                        self.score += 1
                    i.kill()
            for i in self.enemy_list:
                if i.bottom <= self.player.top:
                    view = views.GameOverView()
                    self.window.show_view(view)
                if i.left < 0 or i.right > SCREEN_WIDTH:
                    i.change_x *= -1  # change enemy direction
                    i.change_y = -10
                    i.left = max(0, i.left)
                    i.right = min(i.right, SCREEN_WIDTH)
            if len(self.enemy_list) == 0:
                self.no_of_enemies += 10
                self.window.show_view(self.window.views["LevelUp"])
                self.level += 1
            self.enemy_list.update()
            self.bullet_list.update()
            for i in self.enemy_list:
                i.change_y = 0

    def on_draw(self):
        """Render the screen
        """
        self.clear()
        if self.current_stage == 1:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT,
                                                self.background)
            self.player.draw()
            self.enemy_list.draw()
            self.bullet_list.draw()

        elif self.current_stage == "Start":
            self.manager.draw()

    def on_key_press(self, symbol, modifiers):
        """Called when a key is pressed
        """
        if self.current_stage == 1:
            if symbol == arcade.key.LEFT:
                self.player.change_x = -10
            if symbol == arcade.key.RIGHT:
                self.player.change_x = +10
            if symbol == arcade.key.SPACE:
                bullet = sprites.Bullet(f"assets/images/laser{random.choice(('Red', 'Blue'))}.png",
                                        center_x=self.player.center_x,
                                        center_y=self.player.center_y+self.player.height,
                                        hit_box_algorithm="Detailed")
                if not bullet.collides_with_list(self.bullet_list):
                    self.bullet_list.append(bullet)
                    arcade.Sound("assets/sounds/laser.wav").play()

    def on_key_release(self, symbol, modifiers):
        """Called whenever a key is released
        """
        if self.current_stage == 1:
            if symbol == arcade.key.LEFT:
                self.player.change_x = 0
            if symbol == arcade.key.RIGHT:
                self.player.change_x = 0
    
    def on_mouse_press(self, x, y, button, modifiers):
        clicked = True


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    window.views = {"Game": start_view, "LevelUp": views.LevelUpView(), "GameOver": views.GameOverView(), "HowToPlay": views.HowToPlay()}
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.run()

