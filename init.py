from entities.cursor import Cursor
from entities.golfer import Golfer
from entities.flag import Flag
from entities.swing_meter import SwingMeter
import sys
import pygame
from pygame.locals import *

# move this into a yaml file
HEIGHT = 600
WIDTH = 800
ACC = 0.5
FRIC = -0.12
FPS = 60

class App:
    def __init__(self):
        pygame.init()
        vec = pygame.math.Vector2  # 2 for two dimensional
        self.ticker = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Golf")
        flag = Flag((450, 300), (2, 2))
        cursor = Cursor((0, 0), (10, 10))
        golfer = Golfer((250, 250), (10, 10))
        swing_meter = SwingMeter((300, 400), (100, 10))
        self.entites = [cursor, golfer, flag, swing_meter]
        pygame.mouse.set_visible(False)

    def draw(self):
        self.screen.fill((0,0,0))

        for entity in self.entites:
            entity.draw(self.screen)

        pygame.display.update()

    def update(self):
        for entity in self.entites:
            entity.update()
        self.ticker.tick(FPS)


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            else:
                for entity in self.entites:
                    entity.handle_input_event(event)
        keys = pygame.key.get_pressed()
        for entity in self.entites:
            entity.handle_realtime_input(keys)

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()


app = App()
app.run()
