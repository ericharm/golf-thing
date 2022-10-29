import math
from typing import Any
import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from src.entity import Entity
from src.keys import Keys
from src.club import Club
from src.category import Category
from src.entities.ball import Ball


class Golfer(Entity):
    def __init__(self, position: Vector2, size: Vector2) -> None:
        super().__init__(position, size)
        self.ball = Ball(self.position, Vector2(2, 2))
        self.append_child(self.ball)
        self.categories = {Category.Entity, Category.Golfer}
        self.stroke_radius = StrokeRadius()
        self.club = Club.Driver

    def set_color(self) -> None:
        self.color = (80, 240, 80)
        self.surface.fill(self.color)

    def handle_keypress(self, key: Keys) -> None:
        if key == Keys.Left:
            self.stroke_radius.update_target(-1)
        if key == Keys.Right:
            self.stroke_radius.update_target(1)

    # TODO: update these types
    def swing(self, power: Any, accuracy: Any) -> None:
        self.ball.apply_force(power, accuracy, self.club)

    def update(self) -> None:
        super().update()
        self.stroke_radius.update(self)

    def draw(self, screen: Surface) -> None:
        super().draw(screen)
        self.stroke_radius.draw(screen)


class StrokeRadius:
    def __init__(self) -> None:
        self.color = (250, 250, 80)
        self.magnitude = 70
        self.target = StrokeTarget(self)
        self.position = Vector2(0, 0)

    def update_target(self, amount: int) -> None:
        self.target.adjust(amount)

    def update(self, golfer: Golfer) -> None:
        self.position = golfer.position

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.magnitude, 1)
        self.target.draw(screen)


class StrokeTarget:
    def __init__(self, stroke_radius: StrokeRadius) -> None:
        self.color = (50, 250, 250)
        self.radius = 5
        self.target = 0  # in degrees
        self.stroke_radius = stroke_radius

    def adjust(self, amount: int) -> None:
        self.target += amount
        self.target = self.target % 360

    def draw(self, screen: Surface) -> None:
        position = self.stroke_radius.position
        size = self.stroke_radius.magnitude
        x = size * math.cos(self.target * math.pi / 180) + position.x
        y = size * math.sin(self.target * math.pi / 180) + position.y
        pygame.draw.circle(screen, self.color, (x, y), self.radius, 1)
