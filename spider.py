from enemy import Enemy


class Spider(Enemy):

    def __init__(self, settings, position, groups, obstacle_sprites):
        super().__init__(settings, position, groups, obstacle_sprites, "resources/map1/assets/spider.png",
                         [(0, 5), (1, 5), (2, 9), (3, 9)], "resources/map1/animation/character3")

        self.attack_damage = 10
        self.max_health_points = 50
        self.current_health_points = self.max_health_points
