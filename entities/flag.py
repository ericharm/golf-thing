from entity import Entity

import pygame
from pygame.locals import *

class Flag (Entity):

    def draw(self, screen):
        pole_top = (self.position[0], self.position[1] - 40)
        triangle = [
            [self.position[0], self.position[1] - 40],
            [self.position[0], self.position[1] - 30],
            [self.position[0] + 20, self.position[1] - 35],
        ]
        pygame.draw.circle(screen, (30, 30, 100), self.position, 5)
        pygame.draw.line(screen, (200, 200, 200), self.position, pole_top)
        pygame.draw.polygon(screen, (250, 50, 50), triangle)
