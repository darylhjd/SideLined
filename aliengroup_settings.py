#! python3
# aliengroup_settings.py
"""Class file for settings for an alien group"""


class AGroupS:
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
