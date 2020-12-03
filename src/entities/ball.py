import math
import numpy
from bezier.curve import Curve
import pygame
from pygame.locals import *
from pygame.math import Vector2
from src.entity import Entity
from src.keys import Keys
from src.command import Command
from src.category import Category

class Ball (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.categories = { Category.Entity, Category.Ball }
        self.path = None

    def apply_force(self, power, accuracy, club):
        mouse_pos = pygame.mouse.get_pos()
        self.path = BallPath(self.position, Vector2(mouse_pos[0], mouse_pos[1]))

    def set_at(self, position):
        # maybe we first slide a state on top of the stack displaying info about the shot
        self.position = position
        self.path = None
        self.parent.set_position(position)

    def update(self):
        if (self.path != None):
            self.path.update()

    def draw(self, screen):
        if (self.path != None):
            self.path.draw(screen)

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
            self.points.append(Vector2(points[0][i], points[1][i]))

        self.current_point = 2

    def update(self):
        if (self.current_point < self.point_count):
            self.current_point += 1
        else:
            # somewhere in here we check for collision with the flag
            Command.dispatch(Command(Category.Ball, lambda ball: ball.set_at(self.points[-1])))

    def draw(self, screen):
        pygame.draw.lines(screen, pygame.Color("cyan"), False, [(p.x, p.y) for p in self.points[0:self.current_point]])
