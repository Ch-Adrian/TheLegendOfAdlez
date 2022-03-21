import pygame


class Player:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('resources/knight.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def move(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_UP:
                self.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_UP:
                self.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)