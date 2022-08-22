import pygame
from constants import *


class Block:
    def __init__(self, x, y, size, speed, mass, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.mass = mass
        self.color = color

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def update_x_position(self):
        self.x += self.speed
        # self.speed = self.speed -  self.speed/(abs(self.speed))*0.01 # friction

    # from elastic collision formula
    def get_speed_after_collision(self, object_2):
        return ((self.mass-object_2.mass)/(self.mass + object_2.mass))*self.speed + \
            ((2*object_2.mass)/(self.mass + object_2.mass))*object_2.speed

    def check_wall_collision(self):
        if self.x <= 0:
            self.x = 0
            self.speed *= -1
        elif self.x + self.size >= WIDTH:
            self.x = WIDTH - self.size
            self.speed *= -1
