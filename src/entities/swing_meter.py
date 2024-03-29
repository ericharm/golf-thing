import pygame
from enum import Enum

from pygame.math import Vector2
from pygame.surface import Surface
from src.entity import Entity
from src.category import Category
from src.command import Command


class ChargeDirection(Enum):
    Up = 1
    Down = 2


class SwingMeter(Entity):
    MAX_POWER = 100
    MIN_ACCURACY = -10
    MAX_ACCURACY = 10

    def __init__(self, position: Vector2, size: Vector2) -> None:
        super().__init__(position, size)
        self.categories = {Category.Entity, Category.SwingMeter}
        self.power = 0
        self.accuracy = SwingMeter.MIN_ACCURACY
        self.powering = False
        self.aiming = False
        self.charge_direction = ChargeDirection.Up

    def set_color(self) -> None:
        self.color = (80, 20, 20)
        self.surface.fill(self.color)

    def charge(self) -> None:
        self.powering = True

    def aim(self) -> None:
        self.powering = False
        # self.aiming = True
        Command.dispatch(
            Command(
                Category.Golfer, lambda golfer: golfer.swing(self.power, self.accuracy)
            )
        )
        self.reset()

    def reset(self) -> None:
        self.power = 0
        self.accuracy = SwingMeter.MIN_ACCURACY
        self.powering = False
        self.aiming = False

    def handle_click(self) -> None:
        if self.aiming:
            self.aiming = False
        else:
            self.charge()

    def handle_unclick(self) -> None:
        if self.powering:
            self.aim()

    def update(self) -> None:
        if self.powering:
            if (
                self.power < SwingMeter.MAX_POWER
            ) and self.charge_direction is ChargeDirection.Up:
                self.power += 1
            elif self.power > 0:
                self.charge_direction = ChargeDirection.Down
                self.power -= 1
            else:
                self.powering = False
                self.aiming = False

    def draw(self, screen: Surface) -> None:
        super().draw(screen)
        power_left = self.position.x + self.size.x - self.power
        power_meter = ((power_left, self.position.y), (self.power, self.size.y))
        pygame.draw.rect(screen, (220, 220, 220), power_meter)
