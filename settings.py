import pygame.font


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (47, 129, 54)
        self.frames_per_second = 60
        self.tile_size = 32
        self.screen_change = False

        self.player_speed = 5
        self.enemy_speed = 2
        self.player_init_pos = (10, 10)
