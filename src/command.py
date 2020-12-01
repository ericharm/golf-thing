from queue import SimpleQueue as Queue

class Command:
    queue = Queue()

    @classmethod
    def dispatch(self, command):
        Command.queue.put(command)

    @classmethod
    def get_next(self):
        return None if Command.queue.empty() else Command.queue.get(False)

    @classmethod
    def has_queued_commands(self):
        return not Command.queue.empty()

    def __init__(self, category, action):
        self.category = category
        self.action = action

