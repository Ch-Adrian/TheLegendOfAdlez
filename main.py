import math

import pygame
import sys
from settings import Settings
from map import Map


class TheLegendOfAdlez:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              pygame.RESIZABLE)
        pygame.display.set_caption("The Legend Of Adlez")

        self.clock = pygame.time.Clock()
        self.map = Map(self.settings)
        self.font = pygame.font.SysFont("Arial", 24)
        self.running = False
        self.start = False
        self.difficulty = 'easy'
        self.animation_sprites = self.map.getAnimationSprites()
        self.player = self.map.player

    def run_game(self):
        while self.running:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.frames_per_second)

    def check_events(self):

        self.attack_system()

        for ani in self.animation_sprites:
            ani.animation.nextAnimation()
            ani.move()

        self.player.animation.nextAnimation()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if event.w > 600 and event.h > 600:
                    self.settings.screen_change = True
                    self.settings.screen_width = event.w
                    self.settings.screen_height = event.h
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                self.map.player.debug(event.key)
            if event.type == pygame.USEREVENT:
                self.running = False
                self.game_over()

    def distance(self, a, b):
        return math.sqrt( (b[0]-a[0])**2 + (b[1]-a[1])**2 )

    def attack_system(self):
        for char in self.animation_sprites:
            c_x, c_y = char.get_position()
            p_x, p_y = self.player.get_position()
            d = self.distance((c_x, c_y), (p_x, p_y))
            # print(d)
            if 30 < d < 200:
                top = False
                bottom = False
                right = False
                left = False
                if p_x < c_x:
                    right = True
                else:
                    left = True
                if p_y < c_y:
                    bottom = True
                else:
                    top = True
                char.moving_state(top, bottom, right, left)
            elif d < 30:
                right = False
                left = False
                if p_x < c_x:
                    left = True
                else:
                    right = True
                char.attack_state(right, left)
                char.moving_state(False, False, False, False)
            else:
                char.attack_state(False, False)
                char.moving_state(False, False, False, False)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.map.draw()
        pygame.display.update()

    def main_menu(self):
        mouse_click = False
        while True:
            self.screen.fill((0, 0, 0))
            menu = self.font.render("Menu", True, (0, 120, 120))
            width, height = self.screen.get_size()
            self.screen.blit(menu, (width / 2 - 30, 100))

            continue_button = pygame.Rect(width / 2 - 100, 200, 200, 50)
            options_button = pygame.Rect(width / 2 - 100, 300, 200, 50)
            exit_button = pygame.Rect(width / 2 - 100, 400, 200, 50)

            pygame.draw.rect(self.screen, (0, 120, 120), continue_button)
            pygame.draw.rect(self.screen, (0, 120, 120), options_button)
            pygame.draw.rect(self.screen, (0, 120, 120), exit_button)

            continue_text = self.font.render("Continue", True, (0, 0, 0))
            if not self.start:
                continue_text = self.font.render("Start", True, (0, 0, 0))
            options_text = self.font.render("Options", True, (0, 0, 0))
            exit_text = self.font.render("Exit", True, (0, 0, 0))

            if self.start:
                self.screen.blit(continue_text, (width / 2 - 45, 210))
            else:
                self.screen.blit(continue_text, (width / 2 - 25, 210))
            self.screen.blit(options_text, (width / 2 - 40, 310))
            self.screen.blit(exit_text, (width / 2 - 20, 410))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if continue_button.collidepoint((mouse_x, mouse_y)):
                    self.running = True
                    self.start = True
                    self.run_game()
                elif options_button.collidepoint((mouse_x, mouse_y)):
                    self.running = True
                    self.options()
                elif exit_button.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True
            pygame.display.update()
            self.clock.tick(self.settings.frames_per_second)

    def options(self):
        mouse_click = False
        while self.running:
            self.screen.fill((0, 0, 0))
            menu = self.font.render("Difficulty", True, (0, 120, 120))
            width, height = self.screen.get_size()
            self.screen.blit(menu, (width / 2 - 42, 100))

            easy_button = pygame.Rect(width / 2 - 100, 200, 200, 50)
            medium_button = pygame.Rect(width / 2 - 100, 300, 200, 50)
            hard_button = pygame.Rect(width / 2 - 100, 400, 200, 50)
            return_button = pygame.Rect(width / 2 - 100, 500, 200, 50)

            if self.difficulty == 'easy':
                pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect.inflate(easy_button, 10, 10))
            elif self.difficulty == 'medium':
                pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect.inflate(medium_button, 10, 10))
            elif self.difficulty == 'hard':
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect.inflate(hard_button, 10, 10))

            pygame.draw.rect(self.screen, (0, 120, 120), easy_button)
            pygame.draw.rect(self.screen, (0, 120, 120), medium_button)
            pygame.draw.rect(self.screen, (0, 120, 120), hard_button)
            pygame.draw.rect(self.screen, (0, 120, 120), return_button)

            easy_text = self.font.render("Easy", True, (0, 0, 0))
            medium_text = self.font.render("Medium", True, (0, 0, 0))
            hard_text = self.font.render("Hard", True, (0, 0, 0))
            return_text = self.font.render("Return", True, (0, 0, 0))

            self.screen.blit(easy_text, (width / 2 - 25, 210))
            self.screen.blit(medium_text, (width / 2 - 40, 310))
            self.screen.blit(hard_text, (width / 2 - 25, 410))
            self.screen.blit(return_text, (width / 2 - 35, 510))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if easy_button.collidepoint((mouse_x, mouse_y)):
                    self.difficulty = 'easy'
                elif medium_button.collidepoint((mouse_x, mouse_y)):
                    self.difficulty = 'medium'
                elif hard_button.collidepoint((mouse_x, mouse_y)):
                    self.difficulty = 'hard'
                elif return_button.collidepoint((mouse_x, mouse_y)):
                    self.running = False
            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True
            pygame.display.update()
            self.clock.tick(self.settings.frames_per_second)

    def game_over(self):
        mouse_click = False
        while True:
            self.screen.fill((0, 0, 0))
            title = self.font.render("Game over", True, (0, 120, 120))
            score = self.font.render(f"Score: {self.map.player.experience}", True, (0, 120, 120))
            width, height = self.screen.get_size()
            self.screen.blit(title, (width / 2 - 60, 100))
            self.screen.blit(score, (width / 2 - 53, 150))

            exit_button = pygame.Rect(width / 2 - 50, 250, 100, 50)
            pygame.draw.rect(self.screen, (0, 120, 120), exit_button)
            exit_text = self.font.render("Exit", True, (0, 0, 0))
            self.screen.blit(exit_text, (width / 2 - 20, 260))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if exit_button.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True
            pygame.display.update()
            self.clock.tick(self.settings.frames_per_second)



if __name__ == '__main__':
    tloa = TheLegendOfAdlez()
    tloa.main_menu()
