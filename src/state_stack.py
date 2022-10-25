from typing import List, Optional
from src.state import State


class StateStack:
    stack: List[State] = []

    @classmethod
    def push(cls, state: State) -> None:
        StateStack.stack.append(state)

    @classmethod
    def pop(cls) -> Optional[State]:
        return StateStack.stack.pop()

    @classmethod
    def peek(cls) -> Optional[State]:
        return StateStack.stack[-1] if len(StateStack.stack) else None

    @classmethod
    def swap(cls, state: State) -> None:
        if len(StateStack.stack):
            StateStack.pop()
        StateStack.push(state)
