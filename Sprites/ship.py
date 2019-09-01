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
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/ship.bmp").convert_alpha(), 270, 0.2)
        self.mask = pygame.mask.from_surface(self.image)

        # Position ship
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.centery = float(self.screen_rect.centery)
        self.centerx = float(self.rect.centerx)

        # Movement flags and properties
        self.ymove = self.settings.shipy_move
        self.xmove = self.settings.shipx_move
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.move_up and self.rect.top > 0:
            self.centery -= self.ymove

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ymove

        if self.move_left and self.rect.left > 0:
            self.centerx -= self.xmove

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.xmove

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def update(self):
        self.move()
        self.blitme()


class ShipHitBox:
    def __init__(self, screen, ship):
        # Screen settings
        self.screen = screen

        # Ship settings
        self.ship = ship

        # Image
        self.image = pygame.transform.rotozoom(pygame.image.load(r"images/better_hitbox.bmp").convert_alpha(),
                                               0, 0.015)
        self.mask = pygame.mask.from_surface(self.image)

        # Position hitbox
        self.rect = self.image.get_rect()
        self.centerx = float(self.ship.centerx + 17)
        self.centery = float(self.ship.centery)

        # Flags
        self.show_box = False

    def update_position(self, ship):
        self.centerx = float(ship.centerx + 17)
        self.centery = float(ship.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, ship):
        self.update_position(ship)
        if self.show_box:
            self.blitme()
