import pygame, sys
from player import Player
from settings import Settings

pygame.init()

class TheLegendOfAdlez:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("The Legend Of Adlez")

        self.player = Player(self)


    def run_game(self):
        while True:
            self._check_events()
            self.do_some_stuff()
            self._update_screen()

    def do_some_stuff(self):
        self.player.move()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
            self.player.handle_event(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = TheLegendOfAdlez()
    ai.run_game()
