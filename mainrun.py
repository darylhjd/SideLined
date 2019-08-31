#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from pygame import DOUBLEBUF, HWSURFACE
from pygame.sprite import Group

import gamefunctions as gf
from bg_image import BGImage
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
    powerups = Group()

    aliens_grouplist = []

    bgimage = BGImage(screen, settings)

    clock = pygame.time.Clock()

    while True:
        # Check events
        gf.check_ship_movement(settings, ship)
        gf.check_collisions(ship, bullets, rains, aliens_grouplist, powerups)

        # Update objects
        gf.update_background(bgimage)
        gf.update_ship(ship)
        gf.update_bullets(screen, settings, ship, bullets)
        gf.update_rain(screen, settings, rains)
        gf.update_aliens(screen, settings, ship, aliens_grouplist)

        pygame.display.update()
        clock.tick(140)


run_game()
