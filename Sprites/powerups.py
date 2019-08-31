#! python3
# powerups.py
"""Aliens will drop powerups randomly when they are killed"""

import pygame
from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self, screen, settings, alien):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen

        # Alien that was destroyed
        self.alien = alien
        self.alien_rect = self.alien.rect
        self.alien_center = self.alien_rect.center

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/powerupbox.bmp").convert_alpha(), 0, 0.2)
        self.mask = pygame.mask.from_surface(self.image)

        # Position powerup
        self.rect = self.image.get_rect()
        self.center = float(self.alien_center)
        self.rect.center = self.center
