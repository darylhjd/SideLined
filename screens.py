#! python3
# screens.py
"""Class file for the screens used in SideLined"""

import pygame


class Backscreen:
    def __init__(self, screen_dimensions):
        self.screen = pygame.Surface(screen_dimensions)
        self.screen_rect = self.screen.get_rect()
