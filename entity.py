import pygame
from pygame.locals import *

class Entity:
    def __init__(self, position, size):
        self.position = position
        self.surface = pygame.Surface(size)
        self.set_color()

    def set_color(self):
        return True

    def handle_realtime_input(self, keys):
        return True

    def handle_input_event(self, event):
        return True

    def update(self):
        return True

    def draw(self, screen):
        screen.blit(self.surface, self.surface.get_rect(center = (self.position)))
