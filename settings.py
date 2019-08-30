#! python3
# settings.py
"""Settings file for SideLined"""


class Settings:
    def __init__(self, width=1200, height=720, color=(40, 45, 69)):
        # Screen settings
        self.width = width
        self.height = height
        self.screen_dimensions = (self.width, self.height)
        self.bgcolor = color

        # Ship settings
        self.shipy_move = 8
        self.shipx_move = 6

        # Bullet settings
        self.sb_width = 15
        self.sb_height = 3
        # Auto-shoot intervals
        self.sb_interval = 50
        self.currentsb_interval = 50
        # Bullet speed
        self.sb_speed = 15

        # Rain settings
        self.rainx_move = -3
        self.rainy_move = 3
        # Creation intervals
        self.rain_interval = 7
        self.currentrain_interval = 0
