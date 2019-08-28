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
        self.ship_ymove = 1
