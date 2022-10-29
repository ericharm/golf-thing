from typing import Any, Optional, cast
import numpy
from bezier.curve import Curve
import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from src.entity import Entity
from src.command import Command
from src.category import Category


class Ball(Entity):
    def __init__(self, position: Vector2, size: Vector2) -> None:
        super().__init__(position, size)
        self.categories = {Category.Entity, Category.Ball}
        self.path: Optional[BallPath] = None

    # TODO: update types
    def apply_force(self, power: Any, accuracy: Any, club: Any) -> None:
        del power
        del accuracy
        del club
        mouse_pos = pygame.mouse.get_pos()
        self.path = BallPath(self.position, Vector2(mouse_pos[0], mouse_pos[1]))

    def set_at(self, position: Vector2) -> None:
        # maybe we first slide a state on top of the stack displaying info about the shot
        self.position = position
        self.path = None
        cast(Entity, self.parent).set_position(position)

    def update(self) -> None:
        if self.path:
            self.path.update()

    def draw(self, screen: Surface) -> None:
        if self.path:
            self.path.draw(screen)


class BallPath(Entity):
    # currently draws 1 bezier, but should draw a series of them to account for bounces
    def __init__(self, start: Vector2, end: Vector2) -> None:
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

    def update(self) -> None:
        if self.current_point < self.point_count:
            self.current_point += 1
        else:
            # somewhere in here we check for collision with the flag
            Command.dispatch(
                Command(Category.Ball, lambda ball: ball.set_at(self.points[-1]))
            )

    def draw(self, screen: Surface) -> None:
        pygame.draw.lines(
            screen,
            pygame.Color("cyan"),
            False,
            [(p.x, p.y) for p in self.points[0 : self.current_point]],
        )
