#! python3
# alien.py
"""Class file for aliens"""

import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite


class AlienGroup(Group):
    def __init__(self, agsettings):
        Group.__init__(self)
        self.agsettings = agsettings

        # Group settings
        self.size = self.agsettings.aliengroup_size

        # Movement flags
        self.ymove = self.agsettings.v_d * self.agsettings.alien_speed
        self.xmove = self.agsettings.h_d * self.agsettings.alien_speed


class Alien(Sprite):
    def __init__(self, screen, aliengroup):
        Sprite.__init__(self)

        # Screen settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/ufo.bmp"), 0, 0.08)
        self.mask = pygame.mask.from_surface(self.image)

        # Position alien
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement properties
        self.ymove = aliengroup.ymove
        self.xmove = aliengroup.xmove

    def move(self):
        self.centery += self.ymove
        self.centerx += self.xmove

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def check_inarea(self):
        if not -1000 <= self.centerx < self.screen_rect.width + 1000 or \
           not -1000 <= self.centery <= self.screen_rect.height + 1000:
            self.kill()

    def update(self):
        self.move()
        self.check_inarea()
        self.screen.blit(self.image, self.rect)
