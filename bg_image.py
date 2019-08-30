#! python3
# bg_image.py
"""Class file for background image"""

import pygame


class BGImage:
    def __init__(self, screen, settings):
        self.settings = settings

        # Screen settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Image
        self.image = pygame.image.load(r"images/evengloomy.png").convert()
        self.rect = self.image.get_rect()
        self.left = float(self.screen_rect.left)

    def scroll(self):
        self.left += self.settings.bgx_move
        self.rect.left = self.left

        if self.rect.right < 0:
            self.left = 0
            self.rect.left = self.left
