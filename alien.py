#! python3
# alien.py
"""Class file for aliens"""

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class AlienGroup(Group):
    def __init__(self, alien_screen, agsettings):
        Group.__init__(self)
        self.agsettings = agsettings

        # Group settings
        self.size = self.agsettings.aliengroup_size

        # Alien screen
        self.alien_screen = alien_screen
        self.alien_screen_rect = self.alien_screen.rect

        # Movement flags
        self.ymove = self.agsettings.v_d * self.agsettings.alien_speed
        self.xmove = self.agsettings.v_d * self.agsettings.alien_speed


class Alien(Sprite):
    def __init__(self, screen, aliengroup):
        Sprite.__init__(self)

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
        self.ymove = aliengroup.ymove
        self.xmove = aliengroup.xmove

    def update(self):
        self.centery += self.ymove
        self.centerx += self.xmove

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.screen.blit(self.image, self.rect)
