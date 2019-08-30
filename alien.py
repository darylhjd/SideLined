#! python3
# alien.py
"""Class file for aliens"""

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Alien(Sprite):
    def __init__(self, screen, settings, aliens):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/ufo.bmp"), 0, 0.1)
        self.mask = pygame.mask.from_surface(self.image)

        # Position alien
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement properties
        self.ymove = aliens.ymove
        self.xmove = aliens.xmove

    def update(self):
        self.centery += self.ymove
        self.centerx += self.xmove

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.screen.blit(self.image, self.rect)


class AlienGroup(Group):
    def __init__(self, alien_screen, settings):
        Group.__init__(self)
        self.settings = settings

        # Alien screen
        self.alien_screen = alien_screen
        self.alien_screen_rect = self.alien_screen.get_rect()
        self.alien_screen_centerx = self.alien_screen_rect.centerx

        # Movement flags
        self.ymove = -self.settings.alienvertical_spawn * self.settings.alien_speed
        self.xmove = -self.settings.alienhorizontal_spawn * self.settings.alien_speed
