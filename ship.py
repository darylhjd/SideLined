#! python3
# ship.py
"""Class file for the Ship in the game"""

import pygame


class Ship:
    def __init__(self, screen, settings):
        self.settings = settings

        # Screen settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/ship.bmp"), 270, 0.2)

        # Position ship
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.centery = float(self.rect.centery)

        # Movement flags and properties
        self.move_up = False
        self.move_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.move_up and self.rect.top > 0:
            self.centery -= self.settings.ship_ymove

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.ship_ymove

        self.rect.centery = self.centery
