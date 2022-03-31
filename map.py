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

    # def create_map(self):
    #     for x, row in enumerate(self.settings.map):
    #         for y, column in enumerate(row):
    #             if column == 'o':
    #                 Tile((y * self.settings.tile_size, x * self.settings.tile_size), [self.visible_sprites, self.obstacle_sprites])
    #             if column == 'p':
    #                 self.player = Player((y * self.settings.tile_size, x * self.settings.tile_size), [self.visible_sprites], self.obstacle_sprites)

    def create_map_from_csv(self):
        find_player_x = 0
        find_player_y = 0
        with open('resources/first_map.csv', newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            idx = 0
            for row in reader:
                for id_col, col in enumerate(row):
                    print(idx, id_col)
                    if col == '0':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/grass.png",
                             [self.visible_sprites])
                    elif col == '1':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/grass2.png",
                             [self.visible_sprites])
                    elif col == '2':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/pavement.png",
                             [self.visible_sprites])
                    elif col == '3':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/stone_with_grass.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '4':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/water.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '5':
                        Tile((id_col * self.settings.tile_size, idx * self.settings.tile_size),
                             "resources/tree_wtih_grass.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == 'p':
                        find_player_x = idx
                        find_player_y = id_col
                idx += 1
        self.player = Player((find_player_y * self.settings.tile_size, find_player_x * self.settings.tile_size), [self.visible_sprites], self.obstacle_sprites)

    def draw(self):
        self.visible_sprites.draw(self.player)
        self.visible_sprites.update()


