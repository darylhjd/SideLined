#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import pygame
import sys


def when_keyup(ship, event):
    if event.key == pygame.K_LEFT:
        ship.move_down = False

    if event.key == pygame.K_RIGHT:
        ship.move_up = False


def when_keydown(ship, event):
    if event.key == pygame.K_LEFT:
        ship.move_down = True

    if event.key == pygame.K_RIGHT:
        ship.move_up = True


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(ship, event)

        if event.type == pygame.KEYUP:
            when_keyup(ship, event)


def update_screen(screen, settings, ship):
    screen.fill(settings.bgcolor)
    ship.move()
    ship.blitme()
    pygame.display.update()
