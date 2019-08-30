#! python3
# gamefunctions.py
"""Functions for the main game to run"""


import sys
import random
import pygame
from pygame.sprite import Group

from bullet import Bullet
from rain import Rain
from alien import Alien, AlienGroup


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
    if event.key == pygame.K_LSHIFT:
        ship.ymove *= 2
        ship.xmove *= 2

    ship_movement(ship, event, False)


def when_keydown(ship, event):
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LSHIFT:
        ship.ymove /= 2
        ship.xmove /= 2

    ship_movement(ship, event, True)


def spawn_aliengroup(screen, settings, aliens_grouplist, alien_screen, position_chance, start):
    aliens = AlienGroup(alien_screen, settings)
    for alien_num in range(settings.aliengroup_size):
        alien = Alien(screen, settings)
        if 0 <= position_chance < 0.4:  # Left and right
            alien.centery = start + (alien_num * settings.alienvertical_spawn * alien.rect.width)
            alien.centerx = settings.alienhorizontal_spawn * ()
        else:  # Top and bottom
            alien.centerx = start

        aliens.add(alien)


def create_aliens(screen, settings, aliens_grouplist, alien_screen):
    # Chance of creating a new group
    if random.random() <= settings.aliengroup_spawnchance:

        # Decides which side of the screen the aliens will spawn from.
        # There are four sides to choose from: top, bottom, right, left
        position_chance = random.random()

        if position_chance < 0.1:  # From left of screen
            settings.alienhorizontal_spawn = -1
            y_start = random.randint(0, settings.height)

            if settings.height/3 < y_start < 2/3 * settings.height:
                settings.alienvertical_spawn = random.choice({-1, 1})
            else:
                settings.alienvertical_spawn = 0

            start = y_start

        elif 0.1 <= position_chance < 0.4:  # From right of screen
            settings.alienhorizontal_spawn = 1
            y_start = random.randint(0, settings.height)

            if settings.height/3 < y_start < 2/3 * settings.height:
                settings.alienvertical_spawn = random.choice({-1, 1})
            else:
                settings.alienvertical_spawn = 0

            start = y_start

        elif 0.4 <= position_chance < 0.7:  # From top of screen
            settings.alienvertical_spawn = -1
            x_start = random.randint(0, settings.width)

            if settings.width/3 < x_start < 2/3 * settings.width:
                settings.alienhorizontal_spawn = random.choice({-1, 1})
            else:
                settings.alienhorizontal_spawn = 0

            start = x_start

        else:  # From bottom of screen
            settings.alienvertical_spawn = 1
            x_start = random.randint(0, settings.width)

            if settings.width/3 < x_start < 2/3 * settings.width:
                settings.alienhorizontal_spawn = random.choice({-1, 1})
            else:
                settings.alienhorizontal_spawn = 0

            start = x_start

        spawn_aliengroup(screen, settings, aliens_grouplist, alien_screen, position_chance, start)


def auto_shooting(screen, settings, ship, bullets):
    if pygame.key.get_pressed()[pygame.K_z]:
        if settings.currentsb_interval == settings.sb_interval:
            bullets.add(Bullet(screen, settings, ship))
            settings.currentsb_interval = 0

        settings.currentsb_interval += 1


def check_events(screen, settings, ship, bullets, aliens_grouplist, alien_screen):
    create_aliens(screen, settings, aliens_grouplist, alien_screen)

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


def move_background(screen, settings, bgimage):
    screen.blit(bgimage.image, bgimage.rect)

    if bgimage.rect.right < settings.width:
        screen.blit(bgimage.image, (bgimage.rect.right, 0))


def update_screen(screen, settings, ship, bullets, rains, bgimage, aliens_grouplist):
    bgimage.scroll()
    move_background(screen, settings, bgimage)

    bullets.update()
    ship.update()

    create_rain(screen, settings, rains)
    pygame.sprite.spritecollide(ship, rains, dokill=True, collided=pygame.sprite.collide_mask)
    rains.update()

    pygame.display.update()
