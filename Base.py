import arcade


class Base(arcade.Sprite):
    def __init__(self, image, window):
        super().__init__(image, 1.7)
        self.shots = 0
        self.window = window
        self.bar_color = arcade.color.GREEN

    def draw(self):
        arcade.draw_lrbt_rectangle_outline(self.center_x - 125, self.center_x + 125, self.center_y + 300,
                                           self.center_y + 315, arcade.color.BLACK, 3)
        indent = self.shots * 25
        if self.shots < 10:
            arcade.draw_lrbt_rectangle_filled(self.center_x - 122, self.center_x + 122 - indent, self.center_y + 303,
                                              self.center_y + 312, self.bar_color)

    def update(self):
        hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
        for bullet in hits:
            bullet.kill()
            self.shots += 1