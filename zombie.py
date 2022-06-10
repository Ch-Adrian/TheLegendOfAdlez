from enemy import Enemy


class Zombie(Enemy):

    def __init__(self, settings, position, groups, obstacle_sprites):
        super().__init__(settings, position, groups, obstacle_sprites, "resources/map1/assets/zombie.png",
                         [(0, 4), (1, 8), (2, 6), (3, 6)], "resources/map1/animation/character1")

        self.attack_damage = 10
        self.max_health_points = 70
        self.current_health_points = self.max_health_points
