import pygame
import sys
from settings import Settings
from map import Map
import time

pygame.init()

class TheLegendOfAdlez:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("The Legend Of Adlez")

        self.clock = pygame.time.Clock()
        self.map = Map(self.settings)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.frames_per_second)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if event.w > 600 and event.h > 600:
                    self.settings.screen_change = True
                    self.settings.screen_width = event.w
                    self.settings.screen_height = event.h
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.map.draw()
        pygame.display.update()

if __name__ == '__main__':
    tloa = TheLegendOfAdlez()
    tloa.run_game()

