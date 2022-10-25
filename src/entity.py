from typing import Any, List, Optional
import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from src.category import Category
from src.command import Command


class Entity:
    def __init__(self, position: Vector2, size: Vector2) -> None:
        self.position = position
        self.size = size
        self.surface = pygame.Surface(size)
        self.set_color()
        self.categories = {Category.Entity}
        self.children: List[Entity] = []
        self.parent = None

    def set_color(self) -> None:
        self.color = (0, 0, 0)

    def set_position(self, position: Vector2) -> None:
        self.position = position

    def append_child(self, entity: Any) -> None:
        self.children.append(entity)
        entity.parent = self

    def on_command(self, command: Optional[Command]) -> None:
        if command:
            if len(self.categories.intersection({command.category})):
                (command.action)(self)
            for child in self.children:
                child.on_command(command)

    def update(self) -> None:
        for child in self.children:
            child.update()

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(
            screen,
            self.color,
            ((self.position.x, self.position.x), (self.size.x, self.size.y)),
        )
        for child in self.children:
            child.draw(screen)
