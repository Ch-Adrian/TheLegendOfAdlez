import pygame

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