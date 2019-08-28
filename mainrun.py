#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from settings import Settings
import gamefunctions as gf
from ship import Ship


def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_dimensions)
    ship = Ship(screen, settings)

    while True:
        gf.check_events(ship, settings)
        gf.update_screen(screen, settings, ship)


run_game()
