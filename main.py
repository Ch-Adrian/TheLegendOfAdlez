import math
import pygame
import sys

from action import Action
from actionsystem import ActionSystem
from settings import Settings
from map import Map
from menu import Menu
from shop import Shop


class TheLegendOfAdlez:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("The Legend Of Adlez")

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)

        self.map = Map(self.settings)
        self.animation_sprites = self.map.get_animation_sprites()
        self.player = self.map.player
        self.shop = Shop(self)
        self.action_system = ActionSystem(self)
        self.menu = Menu(self)

        self.running = False
        self.start = False
        self.last_click = pygame.time.get_ticks()
        self.double_click = False
        self.debug_mode = False

    def start_game(self):
        self.menu.main_menu()

    def run_game(self):
        while self.running:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.fps_cap)

    def check_events(self):
        self.action_system.check_if_game_over()
        self.action_system.attack_system()

        for ani in self.animation_sprites:
            if not (ani.is_dead and ani.animation.animation_state == 3 and ani.animation.animation_progress == 5):
                ani.animation.next_animation()
                ani.move()

        self.player.animation.next_animation()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.shop.opened_shop_window:
                        self.shop.opened_shop_window = False
                        self.player.change_movement_status(Action.UNLOCKED_MOVEMENT)
                    else:
                        self.running = False
                elif event.key == pygame.K_b:
                    if self.distance(self.player.get_position(), self.map.shopkeeper.get_position()) < 50:
                        self.shop.opened_shop_window = True
                        self.player.change_movement_status(Action.LOCKED_MOVEMENT)
                elif event.key == pygame.K_c:
                    self.player.equipment.change_sword()
                else:
                    self.debug(event.key)

            if event.type == pygame.USEREVENT:
                self.running = False
                self.menu.score_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Double click check
                if pygame.time.get_ticks() - self.last_click <= 500:
                    self.double_click = True
                else:
                    self.double_click = False
                self.last_click = pygame.time.get_ticks()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.map.draw()
        self.shop.shop_management()
        pygame.display.update()

    def debug(self, key):
        # Testing
        # 1 - add 10 health
        # 2 - remove 10 health
        # 3 - add 10 strength
        # 4 - add 10 experience
        # 5 - add 10 gold
        if self.debug_mode:
            if key == pygame.K_1:
                self.player.change_health(10)
            if key == pygame.K_2:
                self.player.change_health(-10)
            if key == pygame.K_3:
                self.player.change_strength(10)
            if key == pygame.K_4:
                self.player.add_experience(10)
            if key == pygame.K_5:
                self.player.change_gold(10)


    @staticmethod
    def distance(a, b):
        return abs(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))


if __name__ == '__main__':
    game = TheLegendOfAdlez()
    game.start_game()
