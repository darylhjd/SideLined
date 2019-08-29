#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import pygame
import sys
from bullet import Bullet
from rain import Rain


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
        settings.currentbullet_interval += 1

        if settings.currentbullet_interval == settings.bullet_interval:
            bullets.add(Bullet(screen, settings, ship))
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


def create_rain(screen, settings, rains):
    settings.currentrain_interval += 1
    
    if settings.currentrain_interval == settings.rain_interval:
        rains.add(Rain(screen, settings))
        settings.currentrain_interval = 0


def update_screen(screen, settings, ship, bullets, rains):
    screen.fill(settings.bgcolor)

    bullets.update()

    ship.move()
    ship.blitme()

    create_rain(screen, settings, rains)

    rains.update()

    pygame.display.update()
