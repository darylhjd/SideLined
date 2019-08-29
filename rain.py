#! python3
# rain.py
"""Class file for rain effect"""

import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    def __init__(self, screen, settings):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Properties
        self.color = (230, 230, 230)
        self.width = 5
        self.height = 15
        self.rect = pygame.transform.rotozoom(pygame.Rect(0, 0, self.width, self.height), -45, 1)

        # Position raindrop
