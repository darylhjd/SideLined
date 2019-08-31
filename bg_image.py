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
        self.image = pygame.image.load(r"images/gloomy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.left = float(self.screen_rect.left)

        # Movement properties
        self.xmove = self.settings.bgx_move

    def scroll(self):
        self.left += self.xmove
        self.rect.left = self.left

        if self.rect.right < 0:
            self.left = 0
            self.rect.left = self.left

    def update(self):
        self.scroll()

        self.screen.blit(self.image, self.rect)
        if self.rect.right < self.settings.width:
            self.screen.blit(self.image, (self.rect.right, 0))
