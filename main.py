import pygame, sys
from settings import Settings
from map import Map

pygame.init()

class TheLegendOfAdlez:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("The Legend Of Adlez")

        self.clock = pygame.time.Clock()
        self.map = Map()

    def run_game(self):
        while True:
            self._check_events()
            self.do_some_stuff()
            self._update_screen()
            self.clock.tick(self.settings.frames_per_second)

    def do_some_stuff(self):
        self.screen.fill(self.settings.bg_color)
        self.map.draw()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        pygame.display.update()

if __name__ == '__main__':
    tloa = TheLegendOfAdlez()
    tloa.run_game()

