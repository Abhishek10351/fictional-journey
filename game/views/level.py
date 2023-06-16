from datetime import timedelta
import random
import pathlib
from constants import *
import arcade
import sprites
from game_data import fetchall


class Level(arcade.View):
    """ Base class for all levels """

    score = arcade.gui.Property(0)
    shield = arcade.gui.Property(0)
    lives = arcade.gui.Property(3)

    def __init__(self):
        super().__init__()

        self.total_time = timedelta(minutes=0, seconds=0, microseconds=0)
        self.background = arcade.load_texture(pathlib.Path(
            "assets/images/background.jpg"))

        self.score = 0
        arcade.gui.bind(self, "score", self.update_score)

        self.score_label = arcade.gui.UILabel(
            text=f"{self.score:0>5}", x=SCREEN_WIDTH-120, y=SCREEN_HEIGHT-80, font_name="Kenney Future", font_size=20)
        self.shield = 0
        self.shield_path = ASSETS_PATH / "images" / "powerups" / "shields"
        arcade.gui.bind(self, "shield", self.update_shield)
        self.shield_colors = [arcade.color.BRONZE,
                              arcade.color.SILVER, arcade.color.GOLD]

        self.player = None
        self.safety_screens = arcade.SpriteList(True)
        self.lasers = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_lasers = arcade.SpriteList()
        self.double_lasers = False
        self.streak = 0
        self.powerups = arcade.SpriteList()
        self.lives = 3
        arcade.gui.bind(self, "lives", self.update_lives)
        self.lives_layout = arcade.gui.UIBoxLayout(
            y=SCREEN_HEIGHT-40, vertical=False, space_between=10)
        self.lives_layout.add(arcade.gui.UIImage(arcade.load_texture(
            "assets/heart/heart.png"), width=30, height=30))
        self.lives_layout.add(arcade.gui.UIImage(arcade.load_texture(
            "assets/heart/numeralX.png"), width=20, height=20))
        self.lives_layout.add(arcade.gui.UILabel(
            text="3", font_size=20, font_name="Kenney Mini Square"))
        self.manager = arcade.gui.UIManager()
        self.powerups_rarity = fetchall("SELECT id, rarity FROM powerups")
        self.powerups_rarity_weights = {
            "Common": 0.7, "Uncommon": 0.5, "Rare": 0.3, "Epic": 0.15, "Legendary": 0.05}
        self.powerups_rarity = {
            i[0]: self.powerups_rarity_weights[i[1]]
             for i in self.powerups_rarity}
        self.laser_sound = arcade.load_sound("assets/sounds/laser.wav")

    def setup(self):
        self.clear()
        self.total_time = timedelta(seconds=0)
        self.lives = 3
        self.manager.clear()

        self.manager.add(self.lives_layout)
        self.score = 0
        self.shield = 0
        self.shield_image = arcade.gui.UIImage(arcade.load_texture(
            self.shield_path / "shield_gold.png"), 
            x=SCREEN_WIDTH-120, y=SCREEN_HEIGHT-40, width=30, height=30)

        self.manager.add(self.score_label)
        self.safety_screens.clear()
        self.lasers.clear()
        self.enemy_list.clear()
        self.enemy_lasers.clear()
        self.powerups.clear()

    def on_update(self, delta_time):
        self.total_time += timedelta(seconds=delta_time)
        self.check_powerup_collision()
        self.player.update()
        self.lasers.update()
        self.enemy_list.update()
        self.enemy_lasers.update()
        self.powerups.update()

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed. """
        if symbol == arcade.key.P:
            self.window.show_view(self.window.views["Pause"])
        if symbol == arcade.key.R:
            self.setup()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player.draw()
        if self.shield > 0:
            self.player.draw_hit_box(self.shield_colors[self.shield-1], 2)
        self.lasers.draw()
        self.enemy_list.draw()
        self.enemy_lasers.draw()
        self.powerups.draw()
        self.manager.draw()

    def game_over(self):
        self.window.views["GameOver"].setup()
        self.window.show_view(self.window.views["GameOver"])

    def level_complete(self):
        if (self.window.current_level > self.window.levels_completed):
            self.window.levels_completed += 1

        # self.set_high_score()

        self.window.views["LevelUp"].setup()
        self.window.show_view(self.window.views["LevelUp"])

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def update_score(self):
        if self.score < 0:
            self.score = 0
            self.game_over()
        self.manager.remove(self.score_label)
        self.score_label.text = f"{self.score:0>5}"
        self.score_label.fit_content()
        self.manager.add(self.score_label)

    def add_powerup(self, powerup, x, y):
        self.powerups.append(sprites.Powerup(powerup, center_x=x, center_y=y))

    def create_enemies(self, enemy_instance, enemy_path, no_of_enemies, scale=1):
        total = 0
        while total < no_of_enemies:
            enemy = enemy_instance(enemy_path, center_x=random.randint(
                0, 525), center_y=random.randint(350, 525), scale=scale)
            enemy_x_change = list(range(-5, 5))
            enemy_x_change.remove(0)
            enemy.change_x = random.choice(enemy_x_change)
            if not enemy.collides_with_list(self.enemy_list) or enemy.left > 0:
                total += 1
                self.enemy_list.append(enemy)

    def update_shield(self):

        self.shield = max(0, self.shield)
        self.shield = min(3, self.shield)
        self.manager.remove(self.shield_image)
        if self.shield == 1:
            self.shield_image.texture = arcade.load_texture(
                self.shield_path/"shield_bronze.png")
        elif self.shield == 2:
            self.shield_image.texture = arcade.load_texture(
                self.shield_path/"shield_silver.png")
        elif self.shield == 3:
            self.shield_image.texture = arcade.load_texture(
                self.shield_path/"shield_gold.png")
        if self.shield > 0:
            self.manager.add(self.shield_image)

    def check_powerup_collision(self):
        for powerup in self.powerups:
            if powerup.collides_with_sprite(self.player):
                powerup.use(self)
                powerup.kill()

    def check_player_hit(self):

        for laser in self.enemy_lasers:
            if laser.collides_with_sprite(self.player):
                laser.kill()

                if not self.shield:
                    self.lives -= 1
                else:
                    self.shield -= 1

    def make_safety_screens(self, x_start):
        safety_screen_block_width = 5
        safety_screen_block_height = 10
        safety_screen_width_count = 20
        safety_screen_height_count = 5
        y_start = 150
        for x in range(x_start,
                       x_start + safety_screen_width_count * safety_screen_block_width,
                       safety_screen_block_width):
            for y in range(y_start,
                           y_start + safety_screen_height_count * safety_screen_block_height,
                           safety_screen_block_height):
                safety_screen_sprite = arcade.SpriteSolidColor(
                    safety_screen_block_width,
                    safety_screen_block_height, x, y,
                    color=arcade.color.LIGHT_GRAY)

                self.safety_screens.append(safety_screen_sprite)

    def check_safety_screens(self):
        for laser in self.lasers:

            screens = arcade.check_for_collision_with_list(laser, self.safety_screens)
            if screens:
                laser.kill()
                for screen in screens:
                    screen.kill()
        
        for laser in self.enemy_lasers:
            screens = arcade.check_for_collision_with_list(laser, self.safety_screens)
            if screens:
                laser.kill()
                for screen in screens:
                    screen.kill()

    def shoot_laser(self):
        if self.double_lasers:

            laser = sprites.Laser(
                "Blue.png",
                center_x=self.player.left_laser[0],
                center_y=self.player.left_laser[1], angle=self.player.angle)

            if not laser.collides_with_list(self.lasers):
                self.lasers.append(laser)

            laser = sprites.Laser(
                "Blue.png",
                center_x=self.player.right_laser[0],
                center_y=self.player.right_laser[1], angle=self.player.angle)
            if not laser.collides_with_list(self.lasers):
                self.lasers.append(laser)
        else:
            laser = sprites.Laser(
                "Blue.png",
                center_x=self.player.center_laser[0],
                center_y=self.player.center_laser[1], angle=self.player.angle)
            if not laser.collides_with_list(self.lasers):
                self.lasers.append(laser)

        if self.window.sound:
            arcade.Sound(
                "assets/sounds/laser.wav").play(volume=self.window.volume)

    def check_enemy_hit(self, powerups=[]):
        for i in self.lasers:

            if i.top >= SCREEN_HEIGHT:
                self.streak = 0
                self.lasers.remove(i)
            elif i.collides_with_list(self.enemy_list):
                for j in i.collides_with_list(self.enemy_list):
                    self.enemy_list.remove(j)
                    if self.window.sound:
                        arcade.Sound(
                            "assets/sounds/hit.wav").play(volume=self.window.volume)
                    if "shield" in powerups and ("Shield" not in [i.name for i in self.powerups]):
                        if random.randint(1, 5) == 1:
                            powerups = list(self.powerups_rarity.keys())
                            rarities = list(self.powerups_rarity.values())
                            selected_powerup = random.choices(
                                powerups, rarities, k=1)
                            self.add_powerup(
                                selected_powerup[0], j.center_x, j.center_y)
                    self.streak += 1
                    if self.streak > 1:
                        self.score += 100 * self.streak
                    self.score += 100
                self.lasers.remove(i)

    def update_lives(self):
        if self.lives == 0:
            self.game_over()
        self.manager.remove(self.lives_layout)
        self.lives_layout.clear()

        self.lives_layout.add(arcade.gui.UIImage(arcade.load_texture(
            "assets/heart/heart.png"), width=30, height=30))
        self.lives_layout.add(arcade.gui.UIImage(arcade.load_texture(
            "assets/heart/numeralX.png"), width=20, height=20))
        self.lives_layout.add(arcade.gui.UILabel(
            text=str(self.lives), font_size=20, font_name="Kenney Future"))
        self.manager.add(self.lives_layout)
