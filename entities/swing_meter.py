from entity import Entity

import pygame
from pygame.locals import *
from enum import Enum

class ChargeDirection (Enum):
    Up = 1
    Down = 2

class SwingMeter (Entity):
    MAX_POWER = 100

    def __init__(self, position, size):
        super().__init__(position, size)
        self.power = 0
        self.accuracy = 0
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

    def handle_input_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and not self.aiming:
            self.charge()
        elif event.type == MOUSEBUTTONUP and event.button == 1 and self.powering:
            self.aim()

    def update(self):
        if (self.powering):
            if (self.power < SwingMeter.MAX_POWER) and self.charge_direction is ChargeDirection.Up:
                self.power += 1
            elif (self.power > 0):
                self.charge_direction = ChargeDirection.Down
                self.power -= 1
            else:
                # the player misses the swing entirely
                self.powering = False
                self.aiming = False

    def draw(self, screen):
        super().draw(screen)
        top = self.position[1]
        power_left = self.position[0] + self.size[0] - self.power
        power_meter = [power_left, top, self.power, self.size[1]]
        pygame.draw.rect(screen, (220, 220, 220), power_meter)

