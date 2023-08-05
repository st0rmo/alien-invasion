import pygame

class Ship:
    """ class to manage ship """

    def __init__(self, ai_game):
        """initiliaze ship and starting pos"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship img and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for ships horiz pos
        self.x = float(self.rect.x)


        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ update ships pos """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)