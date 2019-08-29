#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import pygame
import sys
from bullet import Bullet


def when_keyup(ship, event):
    if event.key == pygame.K_LEFT:
        ship.move_down = False

    if event.key == pygame.K_RIGHT:
        ship.move_up = False


def when_keydown(screen, settings, ship, bullets, event):
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LEFT:
        ship.move_down = True

    if event.key == pygame.K_RIGHT:
        ship.move_up = True

    if event.key == pygame.K_z:
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet)


def check_events(screen, settings, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(screen, settings, ship, bullets, event)

        if event.type == pygame.KEYUP:
            when_keyup(ship, event)


def update_screen(screen, settings, ship, bullets):
    screen.fill(settings.bgcolor)
    bullets.update()
    ship.move()
    ship.blitme()
    pygame.display.update()
