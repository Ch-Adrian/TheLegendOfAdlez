import sys
import pygame
from button import Button
from difficulty import Difficulty


class Menu:

    def __init__(self, game):
        self.game = game

    def main_menu(self):
        mouse_click = False
        while True:
            self.game.screen.fill((0, 0, 0))
            menu_label = Button(self.game.screen, 200, 50, (0, 0, 0), (0, 120, 120), 24, 100, "Menu")
            continue_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 200,
                                     "Continue" if self.game.start else "Start")
            options_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 300, "Options")
            debug_mode_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 400,
                                       "Debug mode ON" if self.game.debug_mode else "Debug mode OFF")
            exit_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 500, "Exit")

            menu_label.draw()
            continue_button.draw()
            options_button.draw()
            debug_mode_button.draw()
            exit_button.draw()

            mouse_position = pygame.mouse.get_pos()

            if mouse_click:
                if continue_button.collidepoint(mouse_position):
                    self.game.running = True
                    self.game.start = True
                    self.game.run_game()
                elif options_button.collidepoint(mouse_position):
                    self.game.running = True
                    self.options_menu()
                elif debug_mode_button.collidepoint(mouse_position):
                    self.game.debug_mode = not self.game.debug_mode
                elif exit_button.collidepoint(mouse_position):
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
            self.game.clock.tick(self.game.settings.fps_cap)

    def options_menu(self):
        mouse_click = False
        while self.game.running:
            self.game.screen.fill((0, 0, 0))
            difficulty_button = Button(self.game.screen, 200, 50, (0, 0, 0), (0, 120, 120), 24, 100, "Difficulty")
            easy_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 200, "Easy")
            medium_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 300, "Medium")
            hard_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 400, "Hard")
            return_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 500, "Return")

            difficulty_color = None
            selected_button = None

            if self.game.settings.difficulty == Difficulty.EASY:
                difficulty_color = (0, 255, 0)
                selected_button = easy_button
            elif self.game.settings.difficulty == Difficulty.MEDIUM:
                difficulty_color = (255, 255, 0)
                selected_button = medium_button
            elif self.game.settings.difficulty == Difficulty.HARD:
                difficulty_color = (255, 0, 0)
                selected_button = hard_button

            difficulty_frame = Button(self.game.screen, 210, 60, difficulty_color, (0, 0, 0), 24, 0)
            difficulty_frame.button_rect.center = selected_button.button_rect.center

            difficulty_frame.draw()
            difficulty_button.draw()
            easy_button.draw()
            medium_button.draw()
            hard_button.draw()
            return_button.draw()

            mouse_position = pygame.mouse.get_pos()

            if mouse_click:
                if easy_button.collidepoint(mouse_position):
                    self.game.settings.difficulty = Difficulty.EASY
                elif medium_button.collidepoint(mouse_position):
                    self.game.settings.difficulty = Difficulty.MEDIUM
                elif hard_button.collidepoint(mouse_position):
                    self.game.settings.difficulty = Difficulty.HARD
                elif return_button.collidepoint(mouse_position):
                    self.game.running = False

            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True

            pygame.display.update()
            self.game.clock.tick(self.game.settings.fps_cap)

    def score_menu(self):
        mouse_click = False
        while True:
            self.game.screen.fill((0, 0, 0))
            title = Button(self.game.screen, 200, 50, (0, 0, 0), (0, 120, 120), 24, 100, "Game over")
            score = Button(self.game.screen, 200, 50, (0, 0, 0), (0, 120, 120), 24, 150,
                           f"Score: {self.game.player.experience}")
            exit_button = Button(self.game.screen, 200, 50, (0, 120, 120), (0, 0, 0), 24, 250, "Exit")

            title.draw()
            score.draw()
            exit_button.draw()

            mouse_position = pygame.mouse.get_pos()
            if mouse_click:
                if exit_button.collidepoint(mouse_position):
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
            self.game.clock.tick(self.game.settings.fps_cap)
