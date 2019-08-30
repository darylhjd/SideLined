#! python3
# screens.py
"""Class file for the screens used in SideLined"""

import pygame
from pygame import DOUBLEBUF, HWSURFACE


class Screen:
    def __init__(self, screen_dimensions):
        # Screen settings
        self.surface = pygame.display.set_mode(screen_dimensions, DOUBLEBUF | HWSURFACE)
        self.screen_rect = self.surface.get_rect()

