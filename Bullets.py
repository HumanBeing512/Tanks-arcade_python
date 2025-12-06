import arcade
from Config import *


class Bullet(arcade.Sprite):
    def __init__(self, image, tank, side):
        super().__init__(image, 0.1)
        self.center_x = tank.center_x
        self.center_y = tank.center_y
        self.change_x = 12 * tank.part_x
        self.change_y = 12 * tank.part_y
        self.angle = tank.angle
        self.side = side

    def update(self):
        super().update()
        if self.left > SCREEN_WIDTH or self.right < 0 or self.bottom > SCREEN_HEIGHT or self.top < 0:
            self.kill()
