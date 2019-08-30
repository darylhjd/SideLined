#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import pygame
import sys
from bullet import Bullet
from rain import Rain


def ship_movement(ship, event, boolean):
    if event.key == pygame.K_DOWN:
        ship.move_down = boolean

    if event.key == pygame.K_UP:
        ship.move_up = boolean

    if event.key == pygame.K_LEFT:
        ship.move_left = boolean

    if event.key == pygame.K_RIGHT:
        ship.move_right = boolean


def when_keyup(ship, event):
    ship_movement(ship, event, False)


def when_keydown(ship, event):
    if event.key == pygame.K_q:
        sys.exit()

    ship_movement(ship, event, True)


def auto_shooting(screen, settings, ship, bullets):
    if pygame.key.get_pressed()[pygame.K_z]:
        if settings.currentsb_interval == settings.sb_interval:
            bullets.add(Bullet(screen, settings, ship))
            settings.currentsb_interval = 0

        settings.currentsb_interval += 1


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
    if settings.currentrain_interval == settings.rain_interval:
        rains.add(Rain(screen, settings))
        settings.currentrain_interval = 0

    settings.currentrain_interval += 1


def update_screen(screen, settings, ship, bullets, rains, bg_image):
    screen.blit(bg_image, (0, 0))

    bullets.update()
    ship.update()

    create_rain(screen, settings, rains)
    pygame.sprite.spritecollide(ship, rains, dokill=True, collided=pygame.sprite.collide_mask)
    rains.update()

    pygame.display.update()
