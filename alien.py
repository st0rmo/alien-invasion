import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """ initiliaze the alien and set its starting pos"""
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizonal pos
        self.x = float(self.rect.x)