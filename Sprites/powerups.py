#! python3
# powerups.py
"""Aliens will drop powerups randomly when they are killed"""

import pygame
from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self, screen, settings, alien):
        Sprite.__init__(self)
        self.settings = settings

        # Screen settings
        self.screen = screen

        # Alien that was destroyed
        self.alien = alien
        self.alien_rect = self.alien.rect
        self.alien_center = self.alien_rect.center

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/powerbox.bmp").convert_alpha(), 0, 0.1)
        self.mask = pygame.mask.from_surface(self.image)

        # Position powerup
        self.rect = self.image.get_rect()
        self.rect.center = self.alien_center
        self.centerx = self.rect.centerx

    def draw_powerup(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        self.centerx += self.settings.bgx_move * 1.3

        if self.centerx <= 0:
            self.kill()

        self.rect.centerx = self.centerx

    def update(self):
        self.move()
        self.draw_powerup()
