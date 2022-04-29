import math

import pygame


class Camera(pygame.sprite.Group):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.display_surface = pygame.display.get_surface()
        self.middle_x = self.display_surface.get_size()[0] // 2
        self.middle_y = self.display_surface.get_size()[1] // 2
        self.direction = pygame.math.Vector2()

    def draw(self, player):

        next_tile_size = self.settings.tile_size

        self.middle_x = self.display_surface.get_size()[0] // 2
        self.middle_y = self.display_surface.get_size()[1] // 2
        self.direction.x = player.rect.centerx - self.middle_x
        self.direction.y = player.rect.centery - self.middle_y
        for sprite in self.sprites():

            if self.settings.screen_change:
                next_tile_size = math.ceil(min(self.settings.screen_width, self.settings.screen_height)/20)
                before_topleft = sprite.rect.topleft
                next_topleft = ((before_topleft[0]/self.settings.tile_size) * next_tile_size, (before_topleft[1]/self.settings.tile_size) * next_tile_size)
                sprite.rect.topleft = next_topleft
                sprite.image = pygame.transform.scale(sprite.image, (next_tile_size, next_tile_size))

            position = sprite.rect.topleft - self.direction
            if -2*next_tile_size <= position[0] <= self.settings.screen_width+2*next_tile_size and -2*next_tile_size < position[1] <= self.settings.screen_height+2*next_tile_size:
                self.display_surface.blit(sprite.image, position)

        if self.settings.screen_change:
            self.settings.tile_size = next_tile_size
        self.settings.screen_change = False


