import pygame
import random

from AnimateMe import AnimateMe
from spritesheet import Spritesheet

class Enemy(pygame.sprite.Sprite):

    def __init__(self,settings, position, groups, obstacle_sprites, path_to_image, animation_params, path_to_animation):
        super().__init__(groups)
        self.sheet = Spritesheet(path_to_image)
        self.image = self.sheet.get_sprite(0, 0, 32, 32);
        self.animation = AnimateMe(self, animation_params, path_to_animation)
        self.rect = self.image.get_rect(topleft=position)
        self.obstacle_sprites = obstacle_sprites
        self.settings = settings

        self.overlapx = settings.tile_size // 4
        self.overlapy = settings.tile_size // 4

        self.is_moving = False
        self.is_attacking = False
        self.is_idle = False

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

        if random.randint(0, 10) == 2:
            self.rect.x += self.direction.x
            self.collision('x')
            self.rect.y += self.direction.y
            self.collision('y')

    def collision(self, direction):
        self.rect.inflate_ip(-self.overlapx, -self.overlapy)
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                sprite.rect.inflate_ip(-self.overlapx, -self.overlapy)
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                sprite.rect.inflate_ip(self.overlapx, self.overlapy)
        if direction == 'y':
            for sprite in self.obstacle_sprites:
                sprite.rect.inflate_ip(-self.overlapx, -self.overlapy)
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                sprite.rect.inflate_ip(self.overlapx, self.overlapy)
        self.rect.inflate_ip(self.overlapx, self.overlapy)

    def moving_state(self, top, bottom, right, left):
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        if not self.is_moving and not self.is_attacking:
            if self.animation.animation_state >=4:
                self.animation.change_animation_state(4)
            else:
                self.animation.change_animation_state(0)

        self.is_moving = False
        if top:
            self.moving_up = True
            self.animation.change_animation_state(1)
            self.is_moving = True
        if bottom:
            self.moving_down = True
            self.is_moving = True
            self.animation.change_animation_state(5)
        if left:
            self.moving_left = True
            self.is_moving = True
            self.animation.change_animation_state(1)
        if right:
            self.moving_right = True
            self.is_moving = True
            self.animation.change_animation_state(5)

    def attack_state(self, right, left):
        self.is_attacking = False
        if right:
            self.animation.change_animation_state(2)
            self.is_attacking = True
        elif left:
            self.animation.change_animation_state(6)
            self.is_attacking = True

    def get_position(self):
        return self.rect.topleft
