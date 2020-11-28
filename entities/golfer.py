from entity import Entity
import math

from bezier.curve import Curve
import numpy

import pygame
from pygame.locals import *

class Golfer (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.stroke_radius = StrokeRadius()
        self.ball_path = None

    def set_color(self):
        self.color = (80, 240, 80)
        self.surface.fill(self.color)

    def swing(self):
        mouse_pos = pygame.mouse.get_pos()
        self.ball_path = BallPath(Point(self.position[0], self.position[1]), Point(mouse_pos[0], mouse_pos[1]))

    def handle_input(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.swing()

    def update(self):
        self.stroke_radius.update(self)

    def draw(self, screen):
        super().draw(screen)
        self.stroke_radius.draw(screen)
        # pygame.draw.line(screen, (100, 100, 100), self.position, pygame.mouse.get_pos())

        mouse_pos = pygame.mouse.get_pos()
        left = self.position[0] if mouse_pos[0] > self.position[0] else mouse_pos[0]
        top = self.position[1] if mouse_pos[1] > self.position[1] else mouse_pos[1]
        width = abs(self.position[0] - mouse_pos[0])
        height = abs(self.position[1] - mouse_pos[1])
        rect = Rect(left, top, width, height)
        pygame.draw.rect(screen, (100, 100, 100), rect, 1)

        if (self.ball_path != None):
            self.ball_path.draw(screen)

class StrokeTarget:
    def __init__(self, stroke_radius):
        self.color = (50, 250, 250)
        self.radius = 5
        self.target = 0 # in degrees
        self.stroke_radius = stroke_radius

    def adjust(self, amount):
        self.target += amount
        self.target = self.target % 360

    def draw(self, screen):
        position = self.stroke_radius.position
        size = self.stroke_radius.magnitude
        x = size * math.cos(self.target * math.pi / 180) + position[0]
        y = size * math.sin(self.target * math.pi / 180) + position[1]
        pygame.draw.circle(screen, self.color, (x, y), self.radius, 1)

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

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.magnitude, 1)
        self.target.draw(screen)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BallPath():
    def __init__(self, start, end):
        mid_x = (end.x - start.x) / 2 + start.x
        mid_y = (end.y - start.y) / 2
        nodes = [[start.x, mid_x, end.x], [start.y, mid_y, end.y]]
        curve = Curve(nodes, 2)
        point_intervals = numpy.linspace(0.0, 1.0, 50)
        points = curve.evaluate_multi(point_intervals)
        self.points = []

        for i in range(0, len(points[0])):
            self.points.append((points[0][i], points[1][i]))

        self.selected = None
        self.current_point = 2

    def draw(self, screen):
        pygame.draw.lines(screen, pygame.Color("red"), False, [(p[0], p[1]) for p in self.points])
