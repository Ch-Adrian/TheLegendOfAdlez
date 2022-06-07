import sys

import pygame


class MainMenu:

    def __init__(self):
        pass

    def main_menu(self, game):
        mouse_click = False
        while True:
            game.screen.fill((0, 0, 0))
            menu = game.font.render("Menu", True, (0, 120, 120))
            width, height = game.screen.get_size()
            game.screen.blit(menu, (width / 2 - 30, 100))

            continue_button = pygame.Rect(width / 2 - 100, 200, 200, 50)
            options_button = pygame.Rect(width / 2 - 100, 300, 200, 50)
            exit_button = pygame.Rect(width / 2 - 100, 400, 200, 50)

            pygame.draw.rect(game.screen, (0, 120, 120), continue_button)
            pygame.draw.rect(game.screen, (0, 120, 120), options_button)
            pygame.draw.rect(game.screen, (0, 120, 120), exit_button)

            continue_text = game.font.render("Continue", True, (0, 0, 0))
            if not game.start:
                continue_text = game.font.render( "Start", True, (0, 0, 0))
            options_text = game.font.render("Options", True, (0, 0, 0))
            exit_text = game.font.render("Exit", True, (0, 0, 0))

            if game.start:
                game.screen.blit(continue_text, (width / 2 - 45, 210))
            else:
                game.screen.blit(continue_text, (width / 2 - 25, 210))
            game.screen.blit(options_text, (width / 2 - 40, 310))
            game.screen.blit(exit_text, (width / 2 - 20, 410))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if continue_button.collidepoint((mouse_x, mouse_y)):
                    game.running = True
                    game.start = True
                    game.run_game()
                elif options_button.collidepoint((mouse_x, mouse_y)):
                    game.running = True
                    self.options(game)
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
            game.clock.tick(game.settings.frames_per_second)

    def options(self, game):
        mouse_click = False
        while game.running:
            game.screen.fill((0, 0, 0))
            menu = game.font.render("Difficulty", True, (0, 120, 120))
            width, height = game.screen.get_size()
            game.screen.blit(menu, (width / 2 - 42, 100))

            easy_button = pygame.Rect(width / 2 - 100, 200, 200, 50)
            medium_button = pygame.Rect(width / 2 - 100, 300, 200, 50)
            hard_button = pygame.Rect(width / 2 - 100, 400, 200, 50)
            return_button = pygame.Rect(width / 2 - 100, 500, 200, 50)

            if game.settings.difficulty == 'easy':
                pygame.draw.rect(game.screen, (0, 255, 0), pygame.Rect.inflate(easy_button, 10, 10))
            elif game.settings.difficulty == 'medium':
                pygame.draw.rect(game.screen, (255, 255, 0), pygame.Rect.inflate(medium_button, 10, 10))
            elif game.settings.difficulty == 'hard':
                pygame.draw.rect(game.screen, (255, 0, 0), pygame.Rect.inflate(hard_button, 10, 10))

            pygame.draw.rect(game.screen, (0, 120, 120), easy_button)
            pygame.draw.rect(game.screen, (0, 120, 120), medium_button)
            pygame.draw.rect(game.screen, (0, 120, 120), hard_button)
            pygame.draw.rect(game.screen, (0, 120, 120), return_button)

            easy_text = game.font.render("Easy", True, (0, 0, 0))
            medium_text = game.font.render("Medium", True, (0, 0, 0))
            hard_text = game.font.render("Hard", True, (0, 0, 0))
            return_text = game.font.render("Return", True, (0, 0, 0))

            game.screen.blit(easy_text, (width / 2 - 25, 210))
            game.screen.blit(medium_text, (width / 2 - 40, 310))
            game.screen.blit(hard_text, (width / 2 - 25, 410))
            game.screen.blit(return_text, (width / 2 - 35, 510))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if easy_button.collidepoint((mouse_x, mouse_y)):
                    game.settings.difficulty = 'easy'
                elif medium_button.collidepoint((mouse_x, mouse_y)):
                    game.settings.difficulty = 'medium'
                elif hard_button.collidepoint((mouse_x, mouse_y)):
                    game.settings.difficulty = 'hard'
                elif return_button.collidepoint((mouse_x, mouse_y)):
                    game.running = False
            mouse_click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True
            pygame.display.update()
            game.clock.tick(game.settings.frames_per_second)
