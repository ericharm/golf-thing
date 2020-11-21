import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Entity:
    def __init__(self):
        self.position = (0, 0)
        self.size = (0, 0)
        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect(center = (self.position))

    def update(self):
        return True

    def draw(self, displaysurface):
        displaysurface.blit(self.surface, self.rect)

class Cursor (Entity):
    def __init__(self):
        super().__init__()
        self.size = (10, 10)
        self.color = (240, 0, 240)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect = self.surface.get_rect(center = (mouse_pos[0], mouse_pos[1])) # x, y

cursor = Cursor()
entites = [cursor]
pygame.mouse.set_visible(False)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))

    for entity in entites:
        entity.update()
        entity.draw(displaysurface)

    pygame.display.update()
    FramePerSec.tick(FPS)
