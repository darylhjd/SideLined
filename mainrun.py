#! python3
# mainrun.py
"""Sideways shooter game owo"""

import pygame
from pygame import DOUBLEBUF, HWSURFACE
from pygame.sprite import Group

import gamefunctions as gf
from Sprites.ship import Ship
from bg_image import BGImage
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
    alien_collisions = {}

    bgimage = BGImage(screen, settings)

    clock = pygame.time.Clock()

    while True:
        # Check events
        gf.check_ship_movement(settings, ship)
        gf.check_aliens_collisions(ship, bullets, rains, aliens_grouplist, alien_collisions)
        gf.check_powerup_collisions(settings, ship, powerups)
        gf.check_other_non_critical_collisions(ship, rains)

        # Update objects
        gf.update_background(bgimage)
        gf.update_powerups(screen, settings, alien_collisions, powerups)
        gf.update_ship(ship)
        gf.update_bullets(screen, settings, ship, bullets)
        gf.update_rain(screen, settings, rains)
        gf.update_aliens(screen, settings, ship, aliens_grouplist)

        pygame.display.update()
        clock.tick(140)


run_game()
