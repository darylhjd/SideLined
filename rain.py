#! python3
# rain.py
"""Class file for rain effect"""

import random
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
        self.kill_chance = 0.0005
        self.width = 3
        self.height = 15

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/raindroplet.bmp"), 0, 0.05)
        self.mask = pygame.mask.from_surface(self.image)

        # Position raindrop
        self.rect = self.image.get_rect()
        chance = random.random()
        self.rect.bottom = 0 if chance <= 0.60 else random.randint(0, self.screen_rect.height)
        self.rect.left = random.randint(0, self.screen_rect.right) if chance <= 0.60 else self.screen_rect.right
        self.bottom = float(self.rect.bottom)
        self.centerx = float(self.rect.centerx)

    def draw_rain(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        chance = random.random()
        self.bottom += self.settings.rainy_move
        self.centerx += self.settings.rainx_move

        if self.rect.top >= self.screen_rect.bottom or self.rect.left <= 0 or chance <= self.kill_chance:
            self.kill()

        self.rect.bottom = self.bottom
        self.rect.centerx = self.centerx

        self.draw_rain()
