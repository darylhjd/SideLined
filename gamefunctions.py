#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import sys
import random
import pygame

from Sprites.bullet import Bullet
from Sprites.rain import Rain
from Sprites.alien import Alien, AlienGroup
from settings import AGroupS


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
        y_start = random.randint(0 + ship.height, settings.height - ship.height)
        hspawn_d = -1 if 0 <= position_chance < 0.05 else 1
        vspawn_d = decide_secondary(y_start, settings.height)

        x_start = -50 if hspawn_d == -1 else 50 + settings.width

    else:  # From top and bottom of screen
        x_start = random.randint(0 + ship.width, settings.width - ship.width)
        hspawn_d = decide_secondary(x_start, settings.width)
        vspawn_d = -1 if 0.6 <= position_chance < 0.8 else 1

        y_start = -50 if vspawn_d == -1 else 50 + settings.height

    start_coor = (x_start, y_start)
    agsettings = AGroupS(hspawn_d, vspawn_d, start_coor)
    aliengroup = AlienGroup(agsettings)

    spawn_aliengroup(screen, aliens_grouplist, agsettings, aliengroup)


def auto_shooting(screen, settings, ship, bullets):
    if pygame.key.get_pressed()[pygame.K_z]:
        if settings.currentsb_interval == settings.sb_interval:
            bullets.add(Bullet(screen, settings, ship))
            settings.currentsb_interval = 0

        settings.currentsb_interval += 1


def check_events(screen, settings, ship, bullets, aliens_grouplist):
    if random.random() <= settings.aliengroup_spawnchance or not len(aliens_grouplist):
        create_aliens(screen, settings, ship, aliens_grouplist)

    auto_shooting(screen, settings, ship, bullets)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(settings, ship, event)

        if event.type == pygame.KEYUP:
            when_keyup(settings, ship, event)


def create_rain(screen, settings, rains):
    if settings.currentrain_interval == settings.rain_interval:
        rains.add(Rain(screen, settings))
        settings.currentrain_interval = 0

    settings.currentrain_interval += 1


def move_background(screen, settings, bgimage):
    screen.blit(bgimage.image, bgimage.rect)

    if bgimage.rect.right < settings.width:
        screen.blit(bgimage.image, (bgimage.rect.right, 0))


def check_collisions(ship, bullets, rains, aliens_grouplist):
    pygame.sprite.spritecollide(ship, rains, dokill=True, collided=pygame.sprite.collide_mask)

    for group in aliens_grouplist:
        pygame.sprite.groupcollide(bullets, group, True, True)
        pygame.sprite.groupcollide(rains, group, True, False, collided=pygame.sprite.collide_mask)
        if pygame.sprite.spritecollideany(ship, group, collided=pygame.sprite.collide_mask):
            print("hit")


def update_screen(screen, settings, ship, bullets, rains, bgimage, aliens_grouplist):
    bgimage.scroll()
    move_background(screen, settings, bgimage)

    bullets.update()
    ship.update()

    check_collisions(ship, bullets, rains, aliens_grouplist)

    for group in aliens_grouplist:
        group.update()
    for group in [group for group in aliens_grouplist if not len(group)]:
        aliens_grouplist.remove(group)

    create_rain(screen, settings, rains)
    rains.update()

    pygame.display.update()
