class Settings:
    """A class to store all settings for Alien invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (0,0,0)

        #Ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3