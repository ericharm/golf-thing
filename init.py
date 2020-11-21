from entities.cursor import Cursor
from entities.golfer import Golfer

import pygame
from pygame.locals import *

# move this into a yaml file
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

class App:
    def __init__(self):
        pygame.init()
        vec = pygame.math.Vector2  # 2 for two dimensional
        self.ticker = pygame.time.Clock()
        self.displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
        cursor = Cursor((0, 0), (10, 10))
        golfer = Golfer((150, 150), (10, 10))
        self.entites = [cursor, golfer]
        pygame.mouse.set_visible(False)

    def draw(self):
        self.displaysurface.fill((0,0,0))

        for entity in self.entites:
            entity.draw(self.displaysurface)

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

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()


app = App()
app.run()
