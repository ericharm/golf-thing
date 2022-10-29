import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from src.entity import Entity


class Flag(Entity):
    def draw(self, screen: Surface) -> None:
        pole_top = Vector2(self.position.x, self.position.y - 40)
        triangle = [
            [self.position.x, self.position.y - 40],
            [self.position.x, self.position.y - 30],
            [self.position.x + 20, self.position.y - 35],
        ]
        pygame.draw.circle(screen, (30, 30, 100), self.position, 5)
        pygame.draw.line(screen, (200, 200, 200), self.position, pole_top)
        pygame.draw.polygon(screen, (250, 50, 50), triangle)
