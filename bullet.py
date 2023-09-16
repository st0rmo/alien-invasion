import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage bulelts"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at 0,0 then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's pos as float
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up screen"""
        # update exact pos of bullet
        self.y -= self.settings.bullet_speed
        # update rec pos
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)