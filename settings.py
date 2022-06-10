from difficulty import Difficulty


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (47, 129, 54)
        self.fps_cap = 60
        self.tile_size = 32

        self.player_speed = 5
        self.enemy_speed = 2
        self.player_init_pos = (10, 10)

        self.difficulty = Difficulty.EASY
