from src.config import Config
from src.entity import Entity
from src.player import GamePlayer
from src.entities.golfer import Golfer
from src.entities.flag import Flag
from src.entities.swing_meter import SwingMeter
from src.command import Command
from src.state import State
from pygame.math import Vector2

class Game (State):
    def __init__(self):
        self.player = GamePlayer()
        self.world = Entity(Vector2(0, 0), Vector2(Config.WIDTH, Config.HEIGHT))
        self.world.append_child(Flag(Vector2(450, 300), Vector2(2, 2)))
        self.world.append_child(SwingMeter(Vector2(300, 400), Vector2(100, 10)))
        self.world.append_child(Golfer(Vector2(250, 250), Vector2(10, 10)))

    def on_command(self, command):
        self.world.on_command(command)

    def handle_input_event(self, event):
        self.player.handle_input_event(event)

    def handle_realtime_input(self, keys):
        self.player.handle_realtime_input(keys)

    def draw(self, screen):
        self.world.draw(screen)

    def update(self):
        self.world.update()
