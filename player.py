import pygame
from settings import Settings


class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('resources/character.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.obstacle_sprites = obstacle_sprites
        self.settings = Settings()

        self.direction = pygame.math.Vector2()

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def move(self):
        self.direction.x, self.direction.y = 0, 0
        if self.moving_right:
            self.direction.x = 1
        if self.moving_left:
            self.direction.x = -1
        if self.moving_up:
            self.direction.y = -1
        if self.moving_down:
            self.direction.y = 1

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.settings.player_speed
        self.collision('x')
        self.rect.y += self.direction.y * self.settings.player_speed
        self.collision('y')

    def collision(self, direction):
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'y':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top

    def handle_keys(self):
        event = pygame.key.get_pressed()
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        if event[pygame.K_UP]:
            self.moving_up = True
        if event[pygame.K_DOWN]:
            self.moving_down = True
        if event[pygame.K_LEFT]:
            self.moving_left = True
        if event[pygame.K_RIGHT]:
            self.moving_right = True

    def update(self):
        self.handle_keys()
        self.move()