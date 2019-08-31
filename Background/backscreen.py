#! python3
# backscreen.py
"""Class file for the screens used in SideLined"""

import pygame


class Backscreen:
    def __init__(self, screen_dimensions, screen):
        # Main screen
        self.mscreen = screen
        self.mscreen_rect = self.mscreen.get_rect()

        # Alien screen
        self.screen = pygame.Surface(screen_dimensions)

        # Position alien screen
        self.rect = self.screen.get_rect(center=(self.mscreen_rect.centerx, self.mscreen_rect.centery))
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
