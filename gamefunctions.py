#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import random
import sys

import pygame

from Sprites.alien import Alien, AlienGroup
from Sprites.bullet import Bullet
from Sprites.rain import Rain
from settings import AlienGroupSettings


# -----------------------------------------------------------------
# SECTION: Event checking
# Check ship functions
def ship_movement(ship, event, boolean):
    if event.key == pygame.K_DOWN:
        ship.move_down = boolean

    if event.key == pygame.K_UP:
        ship.move_up = boolean

    if event.key == pygame.K_LEFT:
        ship.move_left = boolean

    if event.key == pygame.K_RIGHT:
        ship.move_right = boolean


def when_keyup(settings, ship, event):
    if event.key == pygame.K_LSHIFT:
        ship.ymove *= settings.shipspeed_factor
        ship.xmove *= settings.shipspeed_factor

    ship_movement(ship, event, False)


def when_keydown(settings, ship, event):
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LSHIFT:
        ship.ymove /= settings.shipspeed_factor
        ship.xmove /= settings.shipspeed_factor

    ship_movement(ship, event, True)


def check_ship_movement(settings, ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(settings, ship, event)

        if event.type == pygame.KEYUP:
            when_keyup(settings, ship, event)
# End Ship functions


# Check Collisions functions
def create_powerups(alien_collisions, powerups):
    pass


def check_collisions(ship, bullets, rains, aliens_grouplist, powerups):
    # Delete raindrops that hit the ship.
    pygame.sprite.spritecollide(ship, rains, dokill=True, collided=pygame.sprite.collide_mask)

    alien_collisions = {}
    for group in aliens_grouplist:
        # Detect collisions between bullets and aliens and delete them
        aliengroup_collisions = pygame.sprite.groupcollide(bullets, group, True, True)
        alien_collisions.update(aliengroup_collisions)

        # Delete raindrops that hit aliens.
        pygame.sprite.groupcollide(rains, group, True, False, collided=pygame.sprite.collide_mask)

        # Detecting collision between ship and any alien
        if pygame.sprite.spritecollideany(ship, group, collided=pygame.sprite.collide_mask):
            print("hit")

    create_powerups(alien_collisions, powerups)
# End Collisions functions
# END SECTION: Event checking
# -----------------------------------------------------------------


# -----------------------------------------------------------------
# SECTION: Updating of objects
def update_background(bgimage):
    bgimage.update()


def update_ship(ship):
    ship.update()


# Bullet functions
def auto_shooting(screen, settings, ship, bullets):
    if pygame.key.get_pressed()[pygame.K_z]:
        if settings.currentsb_interval == settings.sb_interval:
            bullets.add(Bullet(screen, settings, ship))
            settings.currentsb_interval = 0

        settings.currentsb_interval += 1


def update_bullets(screen, settings, ship, bullets):
    auto_shooting(screen, settings, ship, bullets)
    bullets.update()
# End Bullet functions


# Rain functions
def create_rain(screen, settings, rains):
    if settings.currentrain_interval == settings.rain_interval:
        rains.add(Rain(screen, settings))
        settings.currentrain_interval = 0

    settings.currentrain_interval += 1


def update_rain(screen, settings, rains):
    create_rain(screen, settings, rains)
    rains.update()
# End Rain functions


# Alien functions
def spawn_aliengroup(screen, aliens_grouplist, agsettings, aliengroup):
    for alien_num in range(aliengroup.size):
        alien = Alien(screen, aliengroup)
        alien.centerx = agsettings.xstart + (alien_num * agsettings.hspawn_d * 2 * alien.rect.width)
        alien.centery = agsettings.ystart + (alien_num * agsettings.vspawn_d * 4 * alien.rect.height)
        aliengroup.add(alien)

    aliens_grouplist.append(aliengroup)


def decide_secondary(start, parameter):
    return random.choice([-1, 1]) if parameter/3 < start < 2/3 * parameter else 0


def create_aliens(screen, settings, ship, aliens_grouplist):
    # Decides which side of the screen the aliens will spawn from.
    position_chance = random.random()

    if 0 <= position_chance < 0.6:  # From left and right of screen
        y_start = random.randint(0 + ship.height * 2, settings.height - ship.height * 2)
        hspawn_d = -1 if 0 <= position_chance < 0.05 else 1
        vspawn_d = decide_secondary(y_start, settings.height)

        x_start = -50 if hspawn_d == -1 else 50 + settings.width

    else:  # From top and bottom of screen
        x_start = random.randint(0 + ship.width * 2, settings.width - ship.width * 2)
        hspawn_d = decide_secondary(x_start, settings.width)
        vspawn_d = -1 if 0.6 <= position_chance < 0.8 else 1

        y_start = -50 if vspawn_d == -1 else 50 + settings.height

    start_coor = (x_start, y_start)
    agsettings = AlienGroupSettings(hspawn_d, vspawn_d, start_coor)
    aliengroup = AlienGroup(agsettings)

    spawn_aliengroup(screen, aliens_grouplist, agsettings, aliengroup)


def update_aliens(screen, settings, ship, aliens_grouplist):
    if random.random() <= settings.aliengroup_spawnchance or not len(aliens_grouplist):
        create_aliens(screen, settings, ship, aliens_grouplist)

    for alien_group in aliens_grouplist.copy():
        if len(alien_group) == 0:
            aliens_grouplist.remove(alien_group)
        else:
            alien_group.update()
# End alien functions
# END SECTION: Updating of objects
# -----------------------------------------------------------------
