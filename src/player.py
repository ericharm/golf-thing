from src.command import Command
from src.entities.golfer import Golfer
from src.entities.swing_meter import SwingMeter
from src.keys import Keys
import pygame
from pygame.locals import *

class Player:

    def handle_realtime_input(self, keys):
        if keys[K_LEFT]:
            Command.dispatch(Command(Golfer, lambda golfer: golfer.handle_keypress(Keys.Left)))
        if keys[K_RIGHT]:
            Command.dispatch(Command(Golfer, lambda golfer: golfer.handle_keypress(Keys.Right)))

    def handle_input_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            Command.dispatch(Command(SwingMeter, lambda meter: meter.handle_click()))
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            Command.dispatch(Command(SwingMeter, lambda meter: meter.handle_unclick()))
