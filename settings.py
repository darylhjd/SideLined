#! python3
# settings.py
"""Settings file for SideLined"""


# General Settings
class Settings:
    def __init__(self, width=1200, height=720, color=(40, 45, 69)):
        # Screen settings
        self.width = width
        self.height = height
        self.screen_dimensions = (self.width, self.height)
        self.alienscreen_dimensions = (self.width + 500, self.height + 500)
        self.bgcolor = color

        # Ship settings
        self.shipy_move = 4
        self.shipx_move = 4
        self.shipspeed_factor = 3

        # Bullet settings
        self.sb_width = 15
        self.sb_height = 3
        # Auto-shoot intervals
        self.max_sb_interval = 7
        self.sb_interval = 50
        self.currentsb_interval = 50
        # Bullet speed
        self.sb_speed = 15

        # Rain settings
        self.rainx_move = -20
        self.rainy_move = 20
        # Creation intervals
        self.rain_interval = 7
        self.currentrain_interval = 0

        # BGImage settings
        self.bgx_move = -0.8

        # Alien settings
        self.aliengroup_spawnchance = 0.0007

        # Powerup settings
        self.powerup_spawnchance = 0.2
        self.pincrease_power = 1


# Settings for AlienGroup
class AlienGroupSettings:
    def __init__(self, hspawn_d, vspawn_d, start_coor):
        # Group settings
        self.aliengroup_size = 5

        # Spawn directions and properties
        self.hspawn_d = hspawn_d
        self.vspawn_d = vspawn_d
        self.xstart = start_coor[0]
        self.ystart = start_coor[1]
        self.start_coor = start_coor

        # Movement directions
        self.h_d = -self.hspawn_d
        self.v_d = -self.vspawn_d

        # Group movement settings
        self.alien_speed = 1
