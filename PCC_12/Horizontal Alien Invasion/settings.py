class Settings():
    """Store all the classes of the Alien_Invasion's settings"""

    def __init__(self):
        """ initialize the game's setting"""
        # Screen Settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
        
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        