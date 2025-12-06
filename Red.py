import math
import arcade
import time
from Bullets import Bullet
from Config import *


class RedTank(arcade.Sprite):
    def __init__(self, window):
        super().__init__("red.png", 0.12)
        self.active = True
        self.angle = 180
        self.shots = 0
        self.window = window
        self.bullet_time = time.time()
        self.part_x = 0
        self.part_y = 0
        self.change_x = 1
        self.change_y = 1

    def update(self):
        if self.active:
            hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
            for bullete in hits:
                if bullete.side == 0:
                    bullete.kill()
                    self.shots += 1
            if self.shots >= 10:
                self.texture = arcade.load_texture("red_broken.png")
                self.active = False
            delta_x = self.window.green.center_x - self.center_x
            delta_y = self.window.green.center_y - self.center_y
            self.angle = -math.degrees(math.atan2(delta_y, delta_x))
            radius = arcade.get_distance_between_sprites(self, self.window.green)
            if radius <= 250:
                self.fire()
                self.part_x = math.cos(math.radians(-self.angle))
                self.part_y = math.sin(math.radians(-self.angle))
                self.center_x += self.part_x * self.change_x
                self.center_y += self.part_y * self.change_y
            elif arcade.get_distance_between_sprites(self.window.green_base, self) <= 400:
                delta_x = self.window.green_base.center_x - self.center_x
                delta_y = self.window.green_base.center_y - self.center_y
                self.angle = -math.degrees(math.atan2(delta_y, delta_x))
                self.fire()
            else:
                self.angle = 180
                self.center_x -= 1

    def fire(self):
        if time.time() - self.bullet_time >= 2:
            self.part_x = math.cos(math.radians(-self.angle))
            self.part_y = math.sin(math.radians(-self.angle))
            shell = Bullet("red_bullet.png", self, 1)
            self.bullet_time = time.time()
            self.window.projectiles.append(shell)

    def draw(self):
        arcade.draw_lrbt_rectangle_outline(self.center_x - 75, self.center_x + 75, self.center_y + 70,
                                           self.center_y + 85, arcade.color.BLACK, 3)
        indent = self.shots * 15
        if self.shots < 10:
            arcade.draw_lrbt_rectangle_filled(self.center_x - 72, self.center_x + 72 - indent,
                                              self.center_y + 73,
                                              self.center_y + 82, arcade.color.ORANGE)
