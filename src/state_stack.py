class StateStack:
    stack = []

    @classmethod
    def push(self, state):
        return StateStack.stack.append(state)

    @classmethod
    def pop(self):
        return StateStack.stack.pop(state)

    @classmethod
    def peek(self):
        return StateStack.stack[-1] if len(StateStack.stack) else None

    @classmethod
    def swap(self, state):
        if (len(StateStack.stack)):
            StateStack.pop()
        StateStack.push(stack)
