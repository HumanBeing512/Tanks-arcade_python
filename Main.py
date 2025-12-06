import arcade

from Config import *
from Tanks import GreenTank
from Bullets import Bullet
from Base import Base
import Red


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Textures
        self.background = arcade.load_texture("background.png")
        # Sprites
        self.green = GreenTank(self)
        self.green_base = Base("green_base.png", self)
        self.red_base = Base("red_base.png", self)
        # Fields
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.run = True
        self.result = 0
        # Sprite Lists
        self.projectiles = arcade.SpriteList()
        self.red_tanks = arcade.SpriteList()
        # Sounds
        self.projectile_sound = arcade.load_sound("shot.mp3")

    def setup(self):
        self.green.center_x = 90
        self.green.center_y = 190
        self.green_base.center_x = 165
        self.green_base.center_y = 350
        self.red_base.center_x = 1035
        self.red_base.center_y = 350
        self.red_base.bar_color = arcade.color.ORANGE
        for i in range(1, 4):
            tank = Red.RedTank(self)
            tank.center_x = 800
            tank.center_y = 200 * i - 50
            self.red_tanks.append(tank)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, self.rect)
        arcade.draw_sprite(self.green)
        arcade.draw_sprite(self.green_base)
        arcade.draw_sprite(self.red_base)
        self.green_base.draw()
        self.green.draw()
        self.red_base.draw()
        self.projectiles.draw()
        for tank in self.red_tanks:
            arcade.draw_sprite(tank)
            tank.draw()

    def on_update(self, delta_time):
        if self.run:
            self.green.update()
            self.red_base.update()
            self.green_base.update()
            for bullet in self.projectiles:
                bullet.update()
            red_destroyed = 0
            for tank in self.red_tanks:
                tank.update()
                if not tank.active:
                    red_destroyed += 1
            if self.red_base.shots >= 10 and red_destroyed == 3:
                self.run = False
                self.result = "Win"

        if self.green.shots >= 10 or self.green_base.shots >= 10:
            self.run = False
            self.result = "Lost"

            if self.result == "Win":
                arcade.load_texture("win.png")
            if self.result == "Lose":
                arcade.load_texture("lose.png")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.green.change_angle = -2.5
            self.left_pressed = True
            self.right_pressed = False

        if key == arcade.key.RIGHT:
            self.green.change_angle = 2.5
            self.left_pressed = False
            self.right_pressed = True

        if key == arcade.key.UP:
            self.green.change_x = 4
            self.green.change_y = 4
            self.up_pressed = True
            self.down_pressed = False

        if key == arcade.key.DOWN:
            self.green.change_x = -3
            self.green.change_y = -3
            self.up_pressed = False
            self.down_pressed = True

        if key == arcade.key.SPACE:
            new_bullet = Bullet("green_bullet.png", self.green, 0)
            self.projectiles.append(new_bullet)
            arcade.play_sound(self.projectile_sound, 0.01)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT and not self.right_pressed:
            self.green.change_angle = 0
        if key == arcade.key.RIGHT and not self.left_pressed:
            self.green.change_angle = 0
        if key == arcade.key.UP and not self.down_pressed:
            self.green.change_x = 0
            self.green.change_y = 0
        if key == arcade.key.DOWN and not self.up_pressed:
            self.green.change_x = 0
            self.green.change_y = 0


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
