import math
import numpy
from bezier.curve import Curve
import pygame
from pygame.locals import *
from src.entity import Entity
from src.keys import Keys

# move this way up the chain and stop using tuples for x/y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        self.ball_path = BallPath(Point(self.position.x, self.position.y), Point(mouse_pos[0], mouse_pos[1]))

    def handle_keypress(self, key):
        if key == Keys.Left:
            self.stroke_radius.update_target(-1)
        if key == Keys.Right:
            self.stroke_radius.update_target(1)

    def update(self):
        self.stroke_radius.update(self)
        if (self.ball_path != None):
            self.ball_path.update()

    def draw(self, screen):
        super().draw(screen)
        self.stroke_radius.draw(screen)

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
        x = size * math.cos(self.target * math.pi / 180) + position.x
        y = size * math.sin(self.target * math.pi / 180) + position.y
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
