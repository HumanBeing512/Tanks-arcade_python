import arcade
import time
import math


class GreenTank(arcade.Sprite):
    def __init__(self, window):
        super().__init__("green.png", 0.12)
        self.active = True
        self.shots = 0
        self.window = window

    def update(self):
        if self.active:
            self.angle += self.change_angle
            self.part_x = math.cos(math.radians(-self.angle))
            self.part_y = math.sin(math.radians(-self.angle))
            self.center_x += self.change_x * self.part_x
            self.center_y += self.change_y * self.part_y
            hitlist = arcade.check_for_collision_with_list(self, self.window.projectiles)
            if hitlist:
                for bullet in hitlist:
                    if bullet.side == 1:
                        bullet.kill()
                        self.shots += 1
                    if self.shots >= 10:
                        self.active = False
                        self.texture = arcade.load_texture("green_broken.png")

    def draw(self):
        arcade.draw_lrbt_rectangle_outline(self.center_x - 75, self.center_x + 75, self.center_y + 100,
                                           self.center_y + 115, arcade.color.BLACK, 3)
        indent = self.shots * 15
        if self.shots < 10:
            arcade.draw_lrbt_rectangle_filled(self.center_x - 72, self.center_x + 72 - indent,
                                              self.center_y + 103,
                                              self.center_y + 112, arcade.color.GREEN)
