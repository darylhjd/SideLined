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
        self.ship_mask = pygame.mask.from_surface(self.image)
        self.mask = self.ship_mask

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

        # Small hitbox image
        self.hb_image = pygame.transform.rotozoom(pygame.image.load(r"images/better_hitbox.bmp"),
                                                  0, 0.03)
        self.hb_mask = pygame.mask.from_surface(self.hb_image)

        # Position hitbox
        self.hb_rect = self.hb_image.get_rect()
        self.hb_centerx = float(self.centerx + 17)
        self.hb_centery = float(self.centery)

        # Hitbox flags
        self.show_hitbox = False

    def update_mask(self):
        self.mask = self.hb_mask if self.show_hitbox else self.ship_mask

    def update_hitbox(self):
        self.update_mask()
        if self.show_hitbox:
            self.screen.blit(self.hb_image, self.hb_rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.move_up and self.rect.top > 0:
            self.centery -= self.ymove
            self.hb_centery -= self.ymove

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ymove
            self.hb_centery += self.ymove

        if self.move_left and self.rect.left > 0:
            self.centerx -= self.xmove
            self.hb_centerx -= self.xmove

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.xmove
            self.hb_centerx += self.xmove

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx
        self.hb_rect.centerx = self.hb_centerx
        self.hb_rect.centery = self.hb_centery

    def update(self):
        self.move()
        self.blitme()
        self.update_hitbox()
