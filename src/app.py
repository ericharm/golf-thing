import sys
import pygame
from pygame.locals import *
from src.config import Config
from src.game import Game
from src.player import Player

class App:
    def __init__(self):
        pygame.init()
        self.ticker = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.game = Game()
        self.player = Player()
        pygame.display.set_caption("Golf")
        pygame.mouse.set_visible(False)

    def draw(self):
        self.game.draw(self.screen)
        pygame.display.update()

    def update(self):
        self.game.update()
        self.ticker.tick(Config.FPS)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.player.handle_input_event(event)
        keys = pygame.key.get_pressed()
        self.player.handle_realtime_input(keys)

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()


