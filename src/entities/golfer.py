import math
import pygame
from src.entity import Entity
from src.keys import Keys
from src.club import Club
from src.category import Category
from src.entities.ball import Ball


class Golfer(Entity):
    def __init__(self, position, size) -> None:
        super().__init__(position, size)
        self.ball = Ball(self.position, (2, 2))
        self.append_child(self.ball)
        self.categories = {Category.Entity, Category.Golfer}
        self.stroke_radius = StrokeRadius()
        self.club = Club.Driver

    def set_color(self) -> None:
        self.color = (80, 240, 80)
        self.surface.fill(self.color)

    def handle_keypress(self, key) -> None:
        if key == Keys.Left:
            self.stroke_radius.update_target(-1)
        if key == Keys.Right:
            self.stroke_radius.update_target(1)

    def swing(self, power, accuracy) -> None:
        self.ball.apply_force(power, accuracy, self.club)

    def update(self):
        super().update()
        self.stroke_radius.update(self)

    def draw(self, screen):
        super().draw(screen)
        self.stroke_radius.draw(screen)


class StrokeTarget:
    def __init__(self, stroke_radius) -> None:
        self.color = (50, 250, 250)
        self.radius = 5
        self.target = 0  # in degrees
        self.stroke_radius = stroke_radius

    def adjust(self, amount) -> None:
        self.target += amount
        self.target = self.target % 360

    def draw(self, screen) -> None:
        position = self.stroke_radius.position
        size = self.stroke_radius.magnitude
        x = size * math.cos(self.target * math.pi / 180) + position.x
        y = size * math.sin(self.target * math.pi / 180) + position.y
        pygame.draw.circle(screen, self.color, (x, y), self.radius, 1)


class StrokeRadius:
    def __init__(self) -> None:
        self.color = (250, 250, 80)
        self.magnitude = 70
        self.target = StrokeTarget(self)
        self.position = (0, 0)

    def update_target(self, amount) -> None:
        self.target.adjust(amount)

    def update(self, golfer) -> None:
        self.position = golfer.position

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.magnitude, 1)
        self.target.draw(screen)
