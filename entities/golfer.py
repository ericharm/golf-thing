from entity import Entity

import pygame
from pygame.locals import *

class Golfer (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.stroke_radius = StrokeRadius()

    def set_color(self):
        self.color = (80, 240, 80)
        self.surface.fill(self.color)

    def update(self):
        self.stroke_radius.update(self)

    def draw(self, displaysurface):
        super().draw(displaysurface)
        self.stroke_radius.draw(displaysurface)


class StrokeRadius:
    def __init__(self):
        self.color = (250, 250, 250)
        self.magnitude = 70
        self.target = 90 # in degrees

    def update(self, golfer):
        self.position = golfer.position

    def draw(self, displaysurface):
        pygame.draw.circle(displaysurface, self.color, self.position, self.magnitude, 1)
