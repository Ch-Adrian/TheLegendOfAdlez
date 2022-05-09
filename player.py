import pygame

from AnimateMe import AnimateMe
from spritesheet import Spritesheet
from equipment import Equipment


class Player(pygame.sprite.Sprite):

    def __init__(self, settings, position, groups, obstacle_sprites, animation_params, path_to_animation):
        super().__init__(groups)
        self.sheet = Spritesheet('resources/map1/assets/player.png')
        self.image = self.sheet.get_sprite(10,18,32,32)
        self.animation = AnimateMe(self, animation_params, path_to_animation)
        self.rect = self.image.get_rect(topleft=position)
        self.obstacle_sprites = obstacle_sprites
        self.settings = settings
        self.overlapx = settings.tile_size // 4
        self.overlapy = settings.tile_size // 4


        self.direction = pygame.math.Vector2()

        self.is_moving = False
        self.is_attacking = False
        self.is_idle = False

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        self.max_health_points = 100
        self.current_health_points = 100
        self.strength = 20
        self.experience = 0
        self.next_level_requirement = 100
        self.current_level = 1
        self.gold = 0
        self.equipment = Equipment()


    def move(self):
        self.direction.x, self.direction.y = 0, 0
        if self.moving_right:
            self.direction.x = 1
        if self.moving_left:
            self.direction.x = -1
        if self.moving_up:
            self.direction.y = -1
        if self.moving_down:
            self.direction.y = 1

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.settings.player_speed
        self.collision('x')
        self.rect.y += self.direction.y * self.settings.player_speed
        self.collision('y')

    def collision(self, direction):
        self.rect.inflate_ip(-self.overlapx, -self.overlapy)
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                sprite.rect.inflate_ip(-self.overlapx, -self.overlapy)
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                sprite.rect.inflate_ip(self.overlapx, self.overlapy)
        if direction == 'y':
            for sprite in self.obstacle_sprites:
                sprite.rect.inflate_ip(-self.overlapx, -self.overlapy)
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                sprite.rect.inflate_ip(self.overlapx, self.overlapy)
        self.rect.inflate_ip(self.overlapx, self.overlapy)

    def handle_keys(self):
        event = pygame.key.get_pressed()
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        if not self.is_moving:
            if self.animation.animation_state >=4:
                self.animation.change_animation_state(4)
            else:
                self.animation.change_animation_state(0)
        self.is_moving = False
        if event[pygame.K_UP] or event[pygame.K_w]:
            self.moving_up = True
            self.is_moving = True
            self.animation.change_animation_state(1)
        if event[pygame.K_DOWN] or event[pygame.K_s]:
            self.moving_down = True
            self.is_moving = True
            self.animation.change_animation_state(5)
        if event[pygame.K_LEFT] or event[pygame.K_a]:
            self.moving_left = True
            self.is_moving = True
            self.animation.change_animation_state(5)
        if event[pygame.K_RIGHT] or event[pygame.K_d]:
            self.moving_right = True
            self.is_moving = True
            self.animation.change_animation_state(1)

    def update(self):
        self.handle_keys()
        self.move()



    def change_health(self, value):
        self.current_health_points = min(self.current_health_points + value, self.max_health_points)
        if self.current_health_points <= 0:
            my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
            pygame.event.post(my_event)
        print(f"Current health: {self.current_health_points}")

    def change_strength(self, value):
        self.strength += value
        print(f"Current strength: {self.strength}")

    def add_experience(self, value):
        self.experience += value
        while self.experience >= self.next_level_requirement:
            self.current_level += 1
            self.next_level_requirement *= 2
        print(f"Current level: {self.current_level}\nTotal experience: {self.experience}")

    def change_gold(self, value):
        self.gold += value
        print(f"Total gold: {self.gold}")

    def debug(self, key):
        # Testing
        # 1 - add 10 health
        # 2 - remove 10 health
        # 3 - add 10 strength
        # 4 - add 10 experience
        # 5 - add 10 gold
        if key == pygame.K_1:
            self.change_health(10)
        if key == pygame.K_2:
            self.change_health(-10)
        if key == pygame.K_3:
            self.change_strength(10)
        if key == pygame.K_4:
            self.add_experience(10)
        if key == pygame.K_5:
            self.change_gold(10)
        if key == pygame.K_6:
            self.equipment.change_sword()

    def get_position(self):
        return self.rect.topleft
