from typing import Optional, Sequence
from pygame.surface import Surface
from pygame.event import Event

from src.command import Command


class State:
    def on_command(self, command: Optional[Command]) -> Optional[bool]:
        del command
        return True

    def handle_input_event(self, event: Event) -> Optional[bool]:
        del event
        return True

    def handle_realtime_input(self, keys: Sequence[bool]) -> Optional[bool]:
        del keys
        return True

    def update(self) -> Optional[bool]:
        return True

    def draw(self, screen: Surface) -> Optional[bool]:
        del screen
        return True
