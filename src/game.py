from src.config import Config
from src.entity import Entity
from src.entities.cursor import Cursor
from src.entities.golfer import Golfer
from src.entities.flag import Flag
from src.entities.swing_meter import SwingMeter
from src.command import Command
from pygame.math import Vector2

class Game:
    def __init__(self):
        self.world = Entity(Vector2(0, 0), Vector2(Config.WIDTH, Config.HEIGHT))
        self.world.append_child(Flag(Vector2(450, 300), Vector2(2, 2)))
        self.world.append_child(Cursor(Vector2(0, 0), Vector2(10, 10)))
        self.world.append_child(Golfer(Vector2(250, 250), Vector2(10, 10)))
        self.world.append_child(SwingMeter(Vector2(300, 400), Vector2(100, 10)))

    def draw(self, screen):
        self.world.draw(screen)

    def update(self):
        while Command.has_queued_commands():
            self.world.on_command(Command.get_next())
        self.world.update()
