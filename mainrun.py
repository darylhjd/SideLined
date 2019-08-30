#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from pygame.sprite import Group

from settings import Settings
import gamefunctions as gf
from ship import Ship


def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_dimensions)

    ship = Ship(screen, settings)
    bullets = Group()
    rains = Group()
    clock = pygame.time.Clock()
    bg_image = pygame.image.load(r"images/mountains.png")

    while True:
        gf.check_events(screen, settings, ship, bullets)
        gf.update_screen(screen, settings, ship, bullets, rains, bg_image)
        clock.tick(120)


run_game()
