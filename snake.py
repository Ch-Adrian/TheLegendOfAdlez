from enemy import Enemy


class Snake(Enemy):

    def __init__(self, settings, position, groups, obstacle_sprites):
        super().__init__(settings, position, groups, obstacle_sprites, "resources/map1/assets/snake.png",
                            [(0,8), (1,8), (2,6), (3,6)], "resources/map1/animation/character2")

        self.attack_damage = 10 * settings.difficulty_values[settings.difficulty]
        self.max_health_points = 40 * settings.difficulty_values[settings.difficulty]
        self.current_health_points = self.max_health_points