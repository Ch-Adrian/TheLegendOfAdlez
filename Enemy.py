import pygame

from Spritesheet import Spritesheet


class Enemy(pygame.sprite.Sprite):

    def __init__(self,settings, position, groups, obstacle_sprites, path_to_image):
        super().__init__(groups)
        self.sheet = Spritesheet(path_to_image)
        self.image = self.sheet.get_sprite(0, 0, 32, 32);
        self.rect = self.image.get_rect(topleft=position)
        self.obstacle_sprites = obstacle_sprites
        self.settings = settings