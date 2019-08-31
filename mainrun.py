#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from pygame import DOUBLEBUF, HWSURFACE
from pygame.sprite import Group

import gamefunctions as gf
from Background.bg_image import BGImage
from Sprites.ship import Ship
from settings import Settings


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_dimensions, DOUBLEBUF | HWSURFACE)
    pygame.display.set_caption("SideLined: On Your Own...")

    ship = Ship(screen, settings)
    bullets = Group()
    rains = Group()

    aliens_grouplist = []

    bgimage = BGImage(screen, settings)

    clock = pygame.time.Clock()

    while True:
        gf.check_events(screen, settings, ship, bullets, aliens_grouplist)
        gf.update_screen(screen, settings, ship, bullets, rains, bgimage, aliens_grouplist)
        clock.tick(140)


run_game()
