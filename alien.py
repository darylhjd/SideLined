#! python3
# alien.py
"""Class file for aliens"""

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Alien(Sprite):
    def __init__(self, screen, settings):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"image/ufo.bmp").convert_alpha(), 0, 0.2)
        self.mask = pygame.mask.from_surface(self.image)

        # Position alien
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


class AlienGroup(Group):
    def __init__(self, alien_screen, settings):
        Group.__init__(self)
        self.settings = settings

        # Alien screen
        self.alien_screen = alien_screen
        self.alien_screen_rect = self.alien_screen.get_rect()

        # Movement flags
        self.ymove = -self.settings.alienvertical_spawn * self.settings.alien_speed
        self.xmove = -self.settings.alienhorizontal_spawn * self.settings.alien_speed
