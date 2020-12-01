from src.config import Config
from src.entity import Entity
from src.entities.cursor import Cursor
from src.entities.golfer import Golfer
from src.entities.flag import Flag
from src.entities.swing_meter import SwingMeter
from src.command import Command

class Game:
    def __init__(self):
        self.world = Entity((0, 0), (Config.WIDTH, Config.HEIGHT))
        self.world.append_child(Flag((450, 300), (2, 2)))
        self.world.append_child(Cursor((0, 0), (10, 10)))
        self.world.append_child(Golfer((250, 250), (10, 10)))
        self.world.append_child(SwingMeter((300, 400), (100, 10)))

    def draw(self, screen):
        self.world.draw(screen)

    def update(self):
        while Command.has_queued_commands():
            self.world.on_command(Command.get_next())
        self.world.update()
