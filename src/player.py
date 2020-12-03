from src.command import Command
from src.category import Category
from src.keys import Keys
import pygame
from pygame.locals import *

class Player:
    def handle_input_event(self, event):
        return True

    def handle_realtime_input(self, keys):
        return True

class GamePlayer (Player):
    def handle_realtime_input(self, keys):
        if keys[K_LEFT]:
            Command.dispatch(Command(Category.Golfer, lambda golfer: golfer.handle_keypress(Keys.Left)))
        if keys[K_RIGHT]:
            Command.dispatch(Command(Category.Golfer, lambda golfer: golfer.handle_keypress(Keys.Right)))

    def handle_input_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("adding a command")
            Command.dispatch(Command(Category.SwingMeter, lambda meter: meter.handle_click()))
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            Command.dispatch(Command(Category.SwingMeter, lambda meter: meter.handle_unclick()))

class MenuPlayer (Player):
    def handle_input_event(self, event):
        return True

    def handle_realtime_input(self, keys):
        return True
