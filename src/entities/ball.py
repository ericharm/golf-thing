import math
import numpy
from bezier.curve import Curve
import pygame
from pygame.locals import *
from pygame.math import Vector2
from src.entity import Entity
from src.keys import Keys

class Ball (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.ball_path = None

    def apply_force(self, power, accuracy):
        mouse_pos = pygame.mouse.get_pos()
        self.ball_path = BallPath(self.position, Vector2(mouse_pos[0], mouse_pos[1]))

    def update(self):
        if (self.ball_path != None):
            self.ball_path.update()

    def draw(self, screen):
        if (self.ball_path != None):
            self.ball_path.draw(screen)

class BallPath:
    # currently draws 1 bezier, but should draw a series of them to account for bounces
    def __init__(self, start, end):
        self.point_count = 50
        mid_x = (end.x - start.x) / 2 + start.x
        mid_y = (end.y - start.y) / 2
        nodes = [[start.x, mid_x, end.x], [start.y, mid_y, end.y]]
        curve = Curve(nodes, 2)
        point_intervals = numpy.linspace(0.0, 1.0, self.point_count)
        points = curve.evaluate_multi(point_intervals)
        self.points = []

        for i in range(0, len(points[0])):
            self.points.append((points[0][i], points[1][i]))

        self.selected = None
        self.current_point = 2

    def update(self):
        if (self.current_point < self.point_count):
            self.current_point += 1

    def draw(self, screen):
        pygame.draw.lines(screen, pygame.Color("cyan"), False, [(p[0], p[1]) for p in self.points[0:self.current_point]])
