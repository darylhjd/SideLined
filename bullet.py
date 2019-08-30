#! python3
# bullet.py
"""Class file for the bullet sprite"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, settings, ship):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Properties
        self.color = (60, 60, 60)
        self.width = self.settings.sb_width
        self.height = self.settings.sb_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Position bullet
        self.rect.centery = ship.centery
        self.left = float(ship.rect.right)

        # Movement properties
        self.speed = self.settings.sb_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.left += self.speed

        if self.left >= self.screen_rect.right:
            self.kill()

        self.rect.left = self.left

        self.draw_bullet()
