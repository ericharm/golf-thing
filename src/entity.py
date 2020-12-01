import pygame
from pygame.locals import *

class Entity:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.surface = pygame.Surface(size)
        self.set_color()
        self.children = []
        self.parent = None

    def set_color(self):
        self.color = (0, 0, 0)

    def append_child(self, entity):
        self.children.append(entity)
        entity.parent = self

    def on_command(self, command):
        if (command.category == type(self)):
            (command.action)(self)
        for child in self.children:
            child.on_command(command)

    def update(self):
        for child in self.children:
            child.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.position[0], self.position[1], self.size[0], self.size[1]])
        for child in self.children:
            child.draw(screen)

