#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import pygame
import sys


def check_events(ship, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.move_up = True

            if event.key == pygame.K_RIGHT:
                ship.move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.move_up = False

            if event.key == pygame.K_RIGHT:
                ship.move_down = False


def update_screen(screen, settings, ship):
    screen.fill(settings.bgcolor)
    ship.move()
    ship.blitme()
    pygame.display.update()
