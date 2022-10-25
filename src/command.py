from queue import SimpleQueue as Queue
from typing import Any, Callable, Optional

from src.category import Category


class Command:
    queue: Queue[Any] = Queue()

    @classmethod
    def dispatch(cls, command: Any) -> None:
        Command.queue.put(command)

    @classmethod
    def get_next(cls) -> Optional[Any]:
        return None if Command.queue.empty() else Command.queue.get(False)

    @classmethod
    def has_queued_commands(cls) -> bool:
        return not Command.queue.empty()

    def __init__(self, category: Category, action: Callable) -> None:
        self.category = category
        self.action = action
