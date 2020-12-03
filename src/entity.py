import pygame
from pygame.locals import *
from src.category import Category

class Entity:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.surface = pygame.Surface(size)
        self.set_color()
        self.categories = { Category.Entity }
        self.children = []
        self.parent = None

    def set_color(self):
        self.color = (0, 0, 0)

    def set_position(self, position):
        self.position = position

    def append_child(self, entity):
        self.children.append(entity)
        entity.parent = self

    def on_command(self, command):
        if (len(self.categories.intersection({ command.category }))):
            (command.action)(self)
        for child in self.children:
            child.on_command(command)

    def update(self):
        for child in self.children:
            child.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.position.x, self.position.y, self.size.x, self.size.y])
        for child in self.children:
            child.draw(screen)

