import math
import pygame
import sys

from actionsystem import ActionSystem
from settings import Settings
from map import Map
from mainmenu import MainMenu
from shop import Shop


class TheLegendOfAdlez:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # pygame.RESIZABLE)
        pygame.display.set_caption("The Legend Of Adlez")
        self.clock = pygame.time.Clock()
        self.last_click = pygame.time.get_ticks()
        self.map = Map(self.settings)
        self.font = pygame.font.SysFont("Arial", 24)
        self.running = False
        self.start = False
        self.animation_sprites = self.map.get_animation_sprites()
        self.player = self.map.player
        self.shop = Shop(self)
        self.double_click = False

        self.action_system = ActionSystem(self)

    def run_game(self):
        while self.running:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.frames_per_second)

    def check_events(self):
        self.action_system.game_is_end()
        self.action_system.attack_system()

        for ani in self.animation_sprites:
            if ani.is_dead and ani.animation.animation_state == 3 and ani.animation.animation_progress == 5:
                continue
            ani.animation.nextAnimation()
            ani.move()

        self.player.animation.nextAnimation()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.VIDEORESIZE:
            #     if event.w > 600 and event.h > 600:
            #         self.settings.screen_change = True
            #         self.settings.screen_width = event.w
            #         self.settings.screen_height = event.h
            #         self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.shop.opened_shop_window:
                        self.shop.opened_shop_window = False
                        self.player.change_movement_status("UNLOCKED")
                    else:
                        self.running = False
                elif event.key == pygame.K_b:
                    if self.distance(self.player.get_position(), self.map.shopkeeper.get_position()) < 50:
                        self.shop.opened_shop_window = True
                        self.player.change_movement_status("LOCKED")

                else:
                    self.map.player.debug(event.key)
            if event.type == pygame.USEREVENT:
                self.running = False
                self.action_system.game_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Double click check
                if pygame.time.get_ticks() - self.last_click <= 500:
                    self.double_click = True
                else:
                    self.double_click = False
                self.last_click = pygame.time.get_ticks()

    def distance(self, a, b):
        return abs(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.map.draw()
        self.shop.shop_management()
        pygame.display.update()


if __name__ == '__main__':
    tloa = TheLegendOfAdlez()
    mainmenu = MainMenu()
    mainmenu.main_menu(tloa)
