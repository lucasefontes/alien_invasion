import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and sets its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship's exact horizontal position.
        self.right = float(self.rect.right)

        #Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        #update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.right += self.settings.ship_speed
        if self.moving_left and self.rect.left:
            self.right -= self.settings.ship_speed
        
        #Update rect object from self.x.
        self.rect.right = self.right

    def blitme(self):
        """Drawn the ship at its current location."""
        self.screen.blit(self.image,self.rect)