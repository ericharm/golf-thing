import pygame
from pygame.locals import *
from src.entity import Entity
from pygame.math import Vector2


class Cursor(Entity):
    def __init__(self, position, size):
        super().__init__(position, size)

    def set_color(self):
        self.color = (240, 0, 240)
        self.surface.fill(self.color)

    def update(self):
        mouse = pygame.mouse.get_pos()
        self.position = Vector2(mouse[0], mouse[1])
