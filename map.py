import pygame

from snake import Snake
from spider import Spider
from tile import Tile
from player import Player
from camera import Camera
from shopkeeper import Shopkeeper
import csv
import random

from zombie import Zombie


class Map:
    def __init__(self, settings):
        self.settings = settings
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.camera = Camera(self.settings, self.visible_sprites)
        self.obstacle_sprites = pygame.sprite.Group()
        self.shopkeeper = None
        self.place_layer("resources/map1/layers/second_map.csv")
        self.font = pygame.font.SysFont("Arial", 14)
        self.amount_of_zombie = 3
        self.amount_of_spiders = 3
        self.amount_of_snakes = 7
        self.amount_of_enemies = self.amount_of_snakes + self.amount_of_spiders + self.amount_of_zombie
        self.animation_enemy_sprites = []

        self.player = Player(settings, (self.settings.player_init_pos[0] * self.settings.tile_size,
                                        self.settings.player_init_pos[1] * self.settings.tile_size),
                             [self.visible_sprites], self.obstacle_sprites, [(0, 6), (1, 6), (2, 4), (3, 3)],
                             "resources/map1/animation/character0")

        for i in range(self.amount_of_spiders):
            self.animation_enemy_sprites.append(Spider(settings, ((25 + random.randint(1, 160)),
                                                                  (1385 + random.randint(1, 140))),
                                                       [self.visible_sprites], self.obstacle_sprites))

        for i in range(self.amount_of_snakes):
            self.animation_enemy_sprites.append(Snake(settings,
                                                      ((994 + random.randint(1, 306)),
                                                       (802 + random.randint(1, 180))),
                                                      [self.visible_sprites], self.obstacle_sprites))

        for i in range(self.amount_of_zombie):
            self.animation_enemy_sprites.append(Zombie(settings,
                                                       ((792 + random.randint(30, 230)),
                                                        (1080 + random.randint(30, 140))),
                                                       [self.visible_sprites], self.obstacle_sprites))

    def place_layer(self, layer_path):
        with open(layer_path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for id_row, row in enumerate(reader):
                graph_row = []
                for id_col, col in enumerate(row):
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
                    elif col == '6':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/cave.png",
                             [self.visible_sprites])
                    elif col == '7':
                        Tile((id_col * self.settings.tile_size, id_row * self.settings.tile_size),
                             "resources/map1/assets/shopkeeper.png",
                             [self.visible_sprites, self.obstacle_sprites])
                        self.shopkeeper = Shopkeeper(id_col * self.settings.tile_size, id_row * self.settings.tile_size)

    def draw(self):
        self.player.update()
        self.camera.draw(self.player)
        self.player.equipment.display_current_equipment()
        self.draw_bars()

    def draw_bars(self):
        self.display_surface = pygame.display.get_surface()

        # health bar
        pygame.draw.rect(self.display_surface, (255, 0, 0), (15, 15, 150, 10))
        pygame.draw.rect(self.display_surface, (0, 255, 0),
                         (15, 15, self.player.current_health_points * 150 / self.player.max_health_points, 10))

        # experience bar
        pygame.draw.rect(self.display_surface, (128, 128, 128), (15, 30, 150, 10))
        previous_level_requirement = self.player.next_level_requirement // 2
        if self.player.current_level == 1:
            previous_level_requirement = 0
        pygame.draw.rect(self.display_surface, (255, 255, 0), (15, 30, 150 * (
                    self.player.experience - previous_level_requirement) / (self.player.next_level_requirement - previous_level_requirement), 10))

        # gold
        gold = self.font.render(f"Gold: {self.player.gold}", True, (0, 0, 0))
        self.display_surface.blit(gold, (15, 45))

        # level
        level = self.font.render(f"Level: {self.player.current_level}", True, (0, 0, 0))
        self.display_surface.blit(level, (15, 60))

        # strength
        strength = self.font.render(f"Strength: {self.player.strength + self.player.equipment.get_sword_power()}", True,
                                    (0, 0, 0))
        self.display_surface.blit(strength, (15, 75))

    def get_animation_sprites(self):
        return self.animation_enemy_sprites
