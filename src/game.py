from typing import Optional, Sequence
from pygame.surface import Surface
from pygame.event import Event
from src.command import Command
from src.config import Config
from src.entities.flag import Flag
from src.entities.golfer import Golfer
from src.entities.swing_meter import SwingMeter
from src.entity import Entity
from src.player import GamePlayer
from src.state import State
from pygame.math import Vector2


class Game(State):
    def __init__(self) -> None:
        self.player = GamePlayer()
        self.world = Entity(Vector2(0, 0), Vector2(Config.WIDTH, Config.HEIGHT))
        self.world.append_child(Flag(Vector2(450, 300), Vector2(2, 2)))
        self.world.append_child(SwingMeter(Vector2(300, 400), Vector2(100, 10)))
        self.world.append_child(Golfer(Vector2(250, 250), Vector2(10, 10)))

    def on_command(self, command: Optional[Command]) -> None:
        self.world.on_command(command)

    def handle_input_event(self, event: Event) -> None:
        self.player.handle_input_event(event)

    def handle_realtime_input(self, keys: Sequence[bool]) -> None:
        self.player.handle_realtime_input(keys)

    def draw(self, screen: Surface) -> None:
        self.world.draw(screen)

    def update(self) -> None:
        self.world.update()
