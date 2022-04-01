import pygame
from settings import Settings
from tile import Tile
from player import Player
from camera import Camera
import csv

class Map:
    def __init__(self):
        self.settings = Settings()
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map_from_csv()
        self.player = Player((self.settings.player_init_pos[0] * self.settings.tile_size,
                              self.settings.player_init_pos[1] * self.settings.tile_size),
                             [self.visible_sprites], self.obstacle_sprites)


    def create_map_from_csv(self):
        with open('resources/first_map.csv', newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for id_row, row in enumerate(reader):
                for id_col, col in enumerate(row):
                    print(id_row, id_col)
                    if col == '0':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/grass.png",
                             [self.visible_sprites])
                    elif col == '1':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/grass2.png",
                             [self.visible_sprites])
                    elif col == '2':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/pavement.png",
                             [self.visible_sprites])
                    elif col == '3':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/stone_with_grass.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '4':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/water.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '5':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/tree_wtih_grass.png",
                             [self.visible_sprites, self.obstacle_sprites])


    def draw(self):
        self.player.update()
        self.visible_sprites.draw(self.player)



