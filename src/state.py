class State:
    def on_command(self, command):
        return True

    def handle_input_event(self, event):
        return True

    def handle_realtime_input(self, keys):
        return True

    def update(self):
        return True

    def draw(self, screen):
        return True
