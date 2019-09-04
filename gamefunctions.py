#! python3
# gamefunctions.py
"""Functions for the main game to run"""

import random
import sys

import pygame

from Sprites.alien import Alien, AlienGroup
from Sprites.bullet import Bullet
from Sprites.powerups import PowerUp
from Sprites.rain import Rain
from settings import AlienGroupSettings


# -----------------------------------------------------------------
# SECTION: Event checking
# Check ship functions
def ship_movement(ship, event, boolean):
    """Sets the ship movement flags to enable movement"""

    if event.key == pygame.K_DOWN:
        ship.move_down = boolean

    if event.key == pygame.K_UP:
        ship.move_up = boolean

    if event.key == pygame.K_LEFT:
        ship.move_left = boolean

    if event.key == pygame.K_RIGHT:
        ship.move_right = boolean


def when_keyup(settings, ship, ship_hitbox, event):
    """Check for key-up events. Sets ship movement flags and movement speed."""

    if event.key == pygame.K_LSHIFT:
        ship_hitbox.show_box = False
        ship.ymove *= settings.shipspeed_factor
        ship.xmove *= settings.shipspeed_factor

    ship_movement(ship, event, False)


def when_keydown(settings, ship, ship_hitbox, event):
    """Quits if 'q' is pressed. Check for key-up events. Sets ship movement flags and movement speed."""

    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LSHIFT:
        ship_hitbox.show_box = True
        ship.ymove /= settings.shipspeed_factor
        ship.xmove /= settings.shipspeed_factor

    ship_movement(ship, event, True)


def check_ship_movement(settings, ship, ship_hitbox):
    """Main event check loop.
    Calls when_keydown(), when_keyup()."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            when_keydown(settings, ship, ship_hitbox, event)

        if event.type == pygame.KEYUP:
            when_keyup(settings, ship, ship_hitbox, event)
# End Ship functions


# Check Collisions functions
def check_aliens_collisions(ship, ship_hitbox, bullets, rains, aliens_grouplist, alien_collisions):
    """Checks all collisions with aliens.
    Ship: Sets htibox accordingly and detects hits with alien.
    Rain: Deletes any rain sprites that falls on any alien sprite.
    Bullet: Deletes bullet and alien sprites that collide with each other."""

    # If player is moving slowly, then pick the smaller hitbox
    to_collide = ship_hitbox if ship_hitbox.show_box else ship

    for group in aliens_grouplist:
        # Detecting collision between ship and any alien
        if pygame.sprite.spritecollideany(to_collide, group, collided=pygame.sprite.collide_mask):
            print("hit")

        # Delete raindrops that hit aliens.
        pygame.sprite.groupcollide(rains, group, True, False, collided=pygame.sprite.collide_mask)

        # Detect collisions between bullets and aliens and delete them. Update alien_collisions for update_powerups()
        alien_collisions.update(pygame.sprite.groupcollide(bullets, group, True, True))


def check_powerup_collisions(settings, ship, powerups):
    """Checks for collisions with ship and powerup. Increases power accordingly."""

    # sb_interval will keep decreasing until it reaches max power.
    if settings.sb_interval > settings.max_sb_interval:
        powerups_collected = len(pygame.sprite.spritecollide(ship, powerups, dokill=True,
                                                             collided=pygame.sprite.collide_mask))

        # Decrease sb_interval by the number of powerups collected and the factor pincrease_power
        settings.sb_interval -= powerups_collected * settings.pincrease_power
        settings.update_aliengroup_spawnchance()


def check_other_non_critical_collisions(ship, rains):
    """Checks all other collisions
    Ship & Rain: Deletes all rain sprites that collide with the ship."""

    # Delete raindrops that hit the ship.
    pygame.sprite.spritecollide(ship, rains, dokill=True, collided=pygame.sprite.collide_mask)
# End Collisions functions
# END SECTION: Event checking
# -----------------------------------------------------------------


# -----------------------------------------------------------------
# SECTION: Updating of objects
def update_background(bgimage):
    """Scrolls the background and blits it on the screen."""

    bgimage.update()


# Powerup functions
def create_powerup(screen, settings, alien, powerups):
    """Creates a PowerUp object and adds it to the powerup group."""

    powerup = PowerUp(screen, settings, alien)
    powerups.add(powerup)


def create_powerups(screen, settings, alien_collisions, powerups):
    """Gets the aliens that are hit and for each, give a chance to spawn a powerup.
    Calls create_powerup()"""

    # Key is the bullet, and the value is a list of aliens that the bullet hit
    aliens_hit = [item for sublist in alien_collisions.values() for item in sublist]

    # Clears the dictionary so past collisions will npt be re-rolled a chance.
    alien_collisions.clear()

    for alien in aliens_hit:
        # PowerUp will only spawn if the value is less or equal to settings.powerup_spawnchance
        if random.random() <= settings.powerup_spawnchance:
            create_powerup(screen, settings, alien, powerups)


def update_powerups(screen, settings, alien_collisions, powerups):
    """Creates powerups when necessary.
    Calls create_powerups()"""

    create_powerups(screen, settings, alien_collisions, powerups)
    powerups.update()
# End Powerup functions


def update_ship(ship, ship_hitbox):
    """Update ship position and show hitbox if necessary."""

    ship.update()
    # Takes ship for an argument to check ship position and blit accordingly.
    ship_hitbox.update(ship)


# Bullet functions
def auto_shooting(screen, settings, ship, bullets):
    """Creates bullets when the 'z' key is pressed.
    Creation is determined by settings.currentsb_interval and settings.sb_interval.
    Also affected by check_powerup_collisions()"""

    if pygame.key.get_pressed()[pygame.K_z]:
        if settings.currentsb_interval >= settings.sb_interval:
            bullets.add(Bullet(screen, settings, ship))
            settings.currentsb_interval = 0

        settings.currentsb_interval += 1


def update_bullets(screen, settings, ship, bullets):
    """Creates bullets when necessary and updates their position."""

    auto_shooting(screen, settings, ship, bullets)
    # Update bullet position and blit
    bullets.update()
# End Bullet functions


# Rain functions
def create_rain(screen, settings, rains):
    """Creates rain at fixed intervals.
    Affected by settings.currentrain_interval and settings.rain_interval"""

    if settings.currentrain_interval == settings.rain_interval:
        rains.add(Rain(screen, settings))
        settings.currentrain_interval = 0

    settings.currentrain_interval += 1


def update_rain(screen, settings, rains):
    """Creates rain when necessary and updates position of each raindrop"""

    create_rain(screen, settings, rains)
    # Update position of rain and blit on screen.
    rains.update()
# End Rain functions


# Alien functions
def spawn_aliengroup(screen, aliens_grouplist, agsettings, aliengroup):
    """Creates a group of aliens of size aliengroup.size and spawns them in the appropriate direction.
    Dircetion is determined by create_aliens() and decide_secondary()"""

    for alien_num in range(aliengroup.size):
        alien = Alien(screen, aliengroup)
        # Aliens will be spaced 2 times of width apart
        alien.centerx = agsettings.xstart + (alien_num * agsettings.hspawn_d * 2 * alien.rect.width)
        # Aliens will be spaced 4 times of height apart
        alien.centery = agsettings.ystart + (alien_num * agsettings.vspawn_d * 4 * alien.rect.height)
        aliengroup.add(alien)

    # Append aliengroup to aliens_grouplist to keep track of all alien groups.
    aliens_grouplist.append(aliengroup)


def decide_secondary(start, parameter):
    return random.choice([-1, 0, 1]) if parameter/3 < start < 2/3 * parameter else 0


def create_aliens(screen, settings, ship, aliens_grouplist):
    """Decides which side of the screen the aliens will spawn from.
    Calls decide_secondary() and spawn_aliengroup()"""

    position_chance = random.random()

    if 0 <= position_chance < 0.6:  # From left and right of screen
        # Buffer to make sure that the ship can always hit an alien no matter where it spawn.
        y_start = random.randint(0 + ship.height * 2, settings.height - ship.height * 2)

        # Less than 5% chance of spawning from the left; behind the ship. The rest will spawn in front
        hspawn_d = -1 if 0 <= position_chance < 0.05 else 1

        # Decides the slant of the alien group. 0 means it is horizontal movement only
        vspawn_d = decide_secondary(y_start, settings.height)

        # Starting x_coor of first alien. Decided by hspawn_d which is decided on top.
        x_start = -50 if hspawn_d == -1 else 50 + settings.width

    else:  # From top and bottom of screen
        # Buffer to make sure that the ship can always hit an alien no matter where it spawn.
        x_start = random.randint(0 + ship.width * 2, settings.width - ship.width * 2)

        # Decides the slant of the alien group. 0 means  it is vertical movement only
        hspawn_d = decide_secondary(x_start, settings.width)

        # There is an equal chance for the aliens to spawn either from the top or bottom.
        vspawn_d = -1 if 0.6 <= position_chance < 0.8 else 1

        # Starting y_coor of first alien. Decided by vspawn_d which is decided on top.
        y_start = -50 if vspawn_d == -1 else 50 + settings.height

    # Starting coordinate of very first alien in the group
    start_coor = (x_start, y_start)
    # Instantiate the settings for this particular alien group.
    agsettings = AlienGroupSettings(hspawn_d, vspawn_d, start_coor)
    # Instantiate an alien group to hold this group of aliens.
    aliengroup = AlienGroup(agsettings)

    # Moves on to spawn the aliens
    spawn_aliengroup(screen, aliens_grouplist, agsettings, aliengroup)


def update_aliens(screen, settings, ship, aliens_grouplist):
    """Decides if an alien group will spawn.
    Calls create_aliens()"""

    # Only spawn if chance is less or equal to settings.aliengroup_spawnchance, or if there is no alien group at all.
    if random.random() <= settings.aliengroup_spawnchance or not len(aliens_grouplist):
        create_aliens(screen, settings, ship, aliens_grouplist)

    # Iterate through all alien groups. If alien group is empty, remove it from aliens_grouplist.
    # On next iteration, empty group will not be iterated through.
    # If not, update positions of all alien in the group, and blit.
    for alien_group in aliens_grouplist.copy():
        if len(alien_group) == 0:
            aliens_grouplist.remove(alien_group)
        else:
            alien_group.update()
# End alien functions
# END SECTION: Updating of objects
# -----------------------------------------------------------------
