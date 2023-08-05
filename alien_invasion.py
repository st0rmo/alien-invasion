import sys
import pygame

from settings import Settings


class AlienInvasion:
    # overall class to manage game assets and behavior #

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("alien invasion")

        # set bg color
        self.bg_color = (0, 80, 110)

    def run_game(self):
        """Start main loop"""
        while True:
            # watch for key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            
            # make most recent drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()