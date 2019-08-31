#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from pygame import DOUBLEBUF, HWSURFACE
from pygame.sprite import Group

from settings import Settings
import gamefunctions as gf
from ship import Ship
from bg_image import BGImage
from backscreen import Backscreen


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_dimensions, DOUBLEBUF | HWSURFACE)
    pygame.display.set_caption("SideLined: On Your Own...")

    ship = Ship(screen, settings)
    bullets = Group()
    rains = Group()

    aliens_grouplist = []
    alien_screen = Backscreen(settings.alienscreen_dimensions, screen)

    bgimage = BGImage(screen, settings)

    clock = pygame.time.Clock()

    while True:
        gf.check_events(screen, settings, ship, bullets, aliens_grouplist, alien_screen)
        gf.update_screen(screen, settings, ship, bullets, rains, bgimage, aliens_grouplist)
        clock.tick(140)


run_game()
