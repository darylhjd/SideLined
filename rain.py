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
        self.color = (230, 230, 230)
        self.width = 3
        self.height = 15
        self.surface = pygame.transform.rotozoom(pygame.Surface((self.width, self.height)), -30, 1)
        self.rect = self.surface.get_rect()

        # Position raindrop
        chance = random.random()
        if chance <= 0.50:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(0, self.screen_rect.right)
        else:
            self.rect.left = self.screen_rect.right
            self.rect.bottom = random.randint(0, self.screen_rect.height)

        self.bottom = float(self.rect.bottom)
        self.centerx = float(self.rect.centerx)

    def draw_rain(self):
        self.surface.fill(self.color)
        self.screen.blit(self.surface, self.rect)

    def update(self):
        kill_chance = random.random()
        self.bottom += self.settings.rainy_move
        self.centerx += self.settings.rainx_move

        if self.rect.top >= self.screen_rect.bottom or self.rect.left <= 0 or kill_chance <= 0.001:
            self.kill()

        self.rect.bottom = self.bottom
        self.rect.centerx = self.centerx

        self.draw_rain()
