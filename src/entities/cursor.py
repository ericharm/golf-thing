import pygame
from pygame.locals import *
from src.entity import Entity

class Cursor (Entity):
    def __init__(self, position, size):
        super().__init__(position, size)

    def set_color(self):
        self.color = (240, 0, 240)
        self.surface.fill(self.color)

    def update(self):
        self.position = pygame.mouse.get_pos()
