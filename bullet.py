#! python3
# bullet.py
"""Class file for the bullet sprite"""

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, settings, ship):
        Sprite.__init__(self)

        # Generic settings
        self.screen = screen
        self.settings = settings

        # Properties
