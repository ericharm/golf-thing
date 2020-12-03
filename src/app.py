import sys
import pygame
from pygame.locals import *
from src.command import Command
from src.config import Config
from src.game import Game
from src.state_stack import StateStack

class App:
    def __init__(self):
        pygame.init()
        self.ticker = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        StateStack.push(Game())
        pygame.display.set_caption("Golf")
        # pygame.mouse.set_visible(False)

    def draw(self):
        for state in StateStack.stack:
            state.draw(self.screen)
        pygame.display.update()

    def update(self):
        top_state = StateStack.peek()
        if top_state:
            while Command.has_queued_commands():
                top_state.on_command(Command.get_next())
            top_state.update()
        self.ticker.tick(Config.FPS)

    def handle_input(self):
        top_state = StateStack.peek()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                top_state.handle_input_event(event) if top_state else None
        keys = pygame.key.get_pressed()
        top_state.handle_realtime_input(keys) if top_state else None

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()


