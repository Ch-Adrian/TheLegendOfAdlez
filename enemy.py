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
        self.is_dead = False

        self.attack_damage = 20
        self.current_health_points = 40
        self.max_health_points = 100

        self.direction = pygame.math.Vector2()

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def change_health(self, value):
        self.current_health_points = max(self.current_health_points + value, 0)
        if self.current_health_points <= 0:
            self.animation.change_animation_state(3)
            self.is_dead = True
            # my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
            # pygame.event.post(my_event)
        # print(f"Current health: {self.current_health_points}")

    def move(self):
        if self.is_dead:
            return
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

        # self.collision(self.direction.x * self.settings.enemy_speed, self.direction.y * self.settings.enemy_speed)
        self.rect.x += self.direction.x * self.settings.enemy_speed
        # print("X: ",self.rect.x)
            # self.collision('x')
        self.rect.y += self.direction.y * self.settings.enemy_speed
        # print("Y: ",self.rect.y)
            # self.collision('y')

    def collision(self, direction_x, direction_y):
        self.rect.x += direction_x
        self.rect.y += direction_y

        # for sprite in self.obstacle_sprites:
        #     if sprite.rect.colliderect(self.rect):
        #         print("Collide")
        #         print(self.rect.x)
        #         self.rect.x -= direction_x
        #         self.rect.y -= direction_y
        #         return False
                # return False
        # return True


    def moving_state(self, top, bottom, right, left):
        if self.is_dead:
            return
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        if not self.is_moving and not self.is_attacking and not self.is_dead:
            if self.animation.animation_state >= 4:
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
            self.animation.change_animation_state(5)
        if right:
            self.moving_right = True
            self.is_moving = True
            self.animation.change_animation_state(1)

    def attack_state(self, right, left):
        if self.is_dead:
            return
        self.is_attacking = False
        if right:
            self.animation.change_animation_state(2)
            self.is_attacking = True
        elif left:
            self.animation.change_animation_state(6)
            self.is_attacking = True
        if not self.is_attacking:
            self.animation.change_animation_state(0)

    def get_position(self):
        return self.rect.topleft
