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


def when_keydown(ship, event):
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LEFT:
        ship.move_down = True

    if event.key == pygame.K_RIGHT:
        ship.move_up = True


def auto_shooting(screen, settings, ship, bullets):
    if pygame.key.get_pressed()[pygame.K_z]:
        settings.current_interval += 1

        if settings.current_interval == settings.bullet_interval:
            new_bullet = Bullet(screen, settings, ship)
            bullets.add(new_bullet)
            settings.current_interval = 0


def check_events(screen, settings, ship, bullets):
    auto_shooting(screen, settings, ship, bullets)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(ship, event)

        if event.type == pygame.KEYUP:
            when_keyup(ship, event)


def update_screen(screen, settings, ship, bullets):
    screen.fill(settings.bgcolor)
    bullets.update()
    ship.move()
    ship.blitme()
    pygame.display.update()
