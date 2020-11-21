from entity import Entity
import math

import pygame
from pygame.locals import *

class Golfer (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.stroke_radius = StrokeRadius()

    def set_color(self):
        self.color = (80, 240, 80)
        self.surface.fill(self.color)

    def handle_input(self, keys):
        if keys[K_LEFT]:
            self.stroke_radius.update_target(-1)
        if keys[K_RIGHT]:
            self.stroke_radius.update_target(1)

    def update(self):
        self.stroke_radius.update(self)

    def draw(self, displaysurface):
        super().draw(displaysurface)
        self.stroke_radius.draw(displaysurface)


class StrokeTarget:
    def __init__(self, stroke_radius):
        self.color = (50, 250, 250)
        self.radius = 10
        self.target = 0 # in degrees
        self.stroke_radius = stroke_radius

    def adjust(self, amount):
        self.target += amount
        self.target = self.target % 360

    def draw(self, displaysurface):
        position = self.stroke_radius.position
        size = self.stroke_radius.magnitude
        x = size * math.cos(self.target * math.pi / 180) + position[0]
        y = size * math.sin(self.target * math.pi / 180) + position[1]
        pygame.draw.circle(displaysurface, self.color, (x, y), self.radius, 1)

class StrokeRadius:
    def __init__(self):
        self.color = (250, 250, 80)
        self.magnitude = 70
        self.target = StrokeTarget(self)
        self.position = (0, 0)

    def update_target(self, amount):
        self.target.adjust(amount)

    def update(self, golfer):
        self.position = golfer.position

    def draw(self, displaysurface):
        pygame.draw.circle(displaysurface, self.color, self.position, self.magnitude, 1)
        self.target.draw(displaysurface)
