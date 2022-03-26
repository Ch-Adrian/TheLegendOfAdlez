import pygame
from settings import Settings
from tile import Tile
from player import Player
from camera import Camera

class Map:
    def __init__(self):
        self.settings = Settings()
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for x, row in enumerate(self.settings.map):
            for y, column in enumerate(row):
                if column == 'o':
                    Tile((y * self.settings.tile_size, x * self.settings.tile_size), [self.visible_sprites, self.obstacle_sprites])
                if column == 'p':
                    self.player = Player((y * self.settings.tile_size, x * self.settings.tile_size), [self.visible_sprites], self.obstacle_sprites)

    def draw(self):
        self.visible_sprites.draw(self.player)
        self.visible_sprites.update()


