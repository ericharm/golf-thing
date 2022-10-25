from typing import Dict, Sequence
from pygame.constants import K_LEFT, K_RIGHT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.event import Event
from src.command import Command
from src.category import Category
from src.keys import Keys


class Player:
    def handle_input_event(self, event: Event) -> bool:
        del event
        return True

    def handle_realtime_input(self, keys: Sequence[bool]) -> bool:
        del keys
        return True


class GamePlayer(Player):
    def handle_realtime_input(self, keys: Sequence[bool]) -> bool:
        if keys[K_LEFT]:
            Command.dispatch(
                Command(
                    Category.Golfer, lambda golfer: golfer.handle_keypress(Keys.Left)
                )
            )
        if keys[K_RIGHT]:
            Command.dispatch(
                Command(
                    Category.Golfer, lambda golfer: golfer.handle_keypress(Keys.Right)
                )
            )
        return True

    def handle_input_event(self, event: Event) -> bool:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            Command.dispatch(
                Command(Category.SwingMeter, lambda meter: meter.handle_click())
            )
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            Command.dispatch(
                Command(Category.SwingMeter, lambda meter: meter.handle_unclick())
            )
        return True


class MenuPlayer(Player):
    def handle_input_event(self, event: Event) -> bool:
        del event
        return True

    def handle_realtime_input(self, keys: Sequence[bool]) -> bool:
        del keys
        return True
