import pygame

from Enemy import Enemy
from Equipment import Equipment
from Sword import Sword
from settings import Settings
from tile import Tile
from player import Player
from camera import Camera
import csv

class Map:
    def __init__(self, settings):
        self.settings = settings
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera(settings)
        self.obstacle_sprites = pygame.sprite.Group()
        self.place_layer("resources/map1/layers/second_map.csv")
        self.player = Player(settings, (self.settings.player_init_pos[0] * self.settings.tile_size,
                              self.settings.player_init_pos[1] * self.settings.tile_size),
                              [self.visible_sprites], self.obstacle_sprites)
        self.enemy1 = Enemy(settings, (self.settings.player_init_pos[0] * self.settings.tile_size-100,
                                        self.settings.player_init_pos[1] * self.settings.tile_size+1100),
                             [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, "resources/map1/assets/spider.png")
        self.enemy2 = Enemy(settings, (self.settings.player_init_pos[0] * self.settings.tile_size+1100,
                                       self.settings.player_init_pos[1] * self.settings.tile_size+50),
                            [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, "resources/map1/assets/snake.png")
        self.enemy3 = Enemy(settings, (self.settings.player_init_pos[0] * self.settings.tile_size+450,
                                       self.settings.player_init_pos[1] * self.settings.tile_size+500),
                            [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, "resources/map1/assets/zombie.png")
        self.equipment = Equipment(settings, (self.settings.screen_width-128, self.settings.screen_height//2 - 128), [], "resources/map1/assets/equip.png")
        self.equipment.add_sword1(Sword("resources/map1/assets/wooden_sword.png"))

    def place_layer(self, layer_path):
        with open(layer_path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for id_row, row in enumerate(reader):
                for id_col, col in enumerate(row):
                    # print(id_row, id_col)
                    if col == '0':
                        pass
                    elif col == '1':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/grass2_x32.png",
                             [self.visible_sprites])
                    elif col == '2':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/pavement_x32.png",
                             [self.visible_sprites])
                    elif col == '3':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/stone_with_grass_x32.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '4':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/water_x32.png",
                             [self.visible_sprites, self.obstacle_sprites])
                    elif col == '5':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/tree_with_grass_x32.png",
                             [self.visible_sprites, self.obstacle_sprites])
    def draw(self):
        self.player.update()
        self.visible_sprites.draw(self.player)
        self.visible_sprites.draw_UI([self.equipment])



