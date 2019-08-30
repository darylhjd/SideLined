#! python3
# alien.py
"""Class file for aliens"""

import pygame
from pygame.sprite import Sprite


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
