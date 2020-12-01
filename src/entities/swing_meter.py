import pygame
from pygame.locals import *
from enum import Enum
from src.entity import Entity

class ChargeDirection (Enum):
    Up = 1
    Down = 2

class SwingMeter (Entity):
    MAX_POWER = 100
    MIN_ACCURACY = -10
    MAX_ACCURACY = 10

    def __init__(self, position, size):
        super().__init__(position, size)
        self.power = 0
        self.accuracy = -10
        self.powering = False
        self.aiming = False
        self.charge_direction = ChargeDirection.Up

    def set_color(self):
        self.color = (80, 20, 20)
        self.surface.fill(self.color)

    def charge(self):
        self.powering = True

    def aim(self):
        self.powering = False
        self.aiming = True

    def handle_click(self):
        if self.aiming:
            self.aiming = False
        else:
            self.charge()

    def handle_unclick(self):
        if self.powering:
            self.aim()

    def update(self):
        if (self.powering):
            if (self.power < SwingMeter.MAX_POWER) and self.charge_direction is ChargeDirection.Up:
                self.power += 1
            elif (self.power > 0):
                self.charge_direction = ChargeDirection.Down
                self.power -= 1
            else:
                self.powering = False
                self.aiming = False

    def draw(self, screen):
        super().draw(screen)
        top = self.position[1]
        power_left = self.position[0] + self.size[0] - self.power
        power_meter = [power_left, top, self.power, self.size[1]]
        pygame.draw.rect(screen, (220, 220, 220), power_meter)

