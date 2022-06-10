import random
import pygame
from action import Action


class ActionSystem:

    def __init__(self, game):
        self.game = game

    def attack_system(self):
        for enemy in self.game.animation_sprites:
            if not enemy.is_dead:
                enemy_x, enemy_y = enemy.get_position()
                player_x, player_y = self.game.player.get_position()
                distance = self.game.distance((enemy_x, enemy_y), (player_x, player_y))

                if distance > 200:
                    self.patrol(enemy)
                elif 35 < distance <= 200:
                    enemy.action = Action.CHASE
                    # enemy movement
                    top, bottom, right, left = False, False, False, False

                    if player_x + 10 < enemy_x:
                        left = True
                    elif player_x - 10 > enemy_x:
                        right = True
                    else:
                        top = enemy.moving_up
                        bottom = enemy.moving_down

                    if player_y + 10 < enemy_y:
                        top = True
                    elif player_y - 10 > enemy_y:
                        bottom = True
                    else:
                        left = enemy.moving_left
                        right = enemy.moving_right

                    enemy.moving_state(top, bottom, right, left)

                elif distance <= 35:
                    if self.game.player.is_attacking:
                        if (self.game.player.animation.animation_state == 2 or
                            self.game.player.animation.animation_state == 6) and \
                                self.game.player.animation.animation_progress == 2:
                            if abs(player_y - enemy_y) < 40:
                                if enemy.change_health(-self.game.player.get_total_power()):
                                    self.game.player.add_experience(200 // len(self.game.animation_sprites))
                                    self.game.player.change_gold(random.randint(1, 15))
                                self.game.player.animation.change_animation_state(0)

                    right, left = False, False

                    if player_x < enemy_x:
                        left = True
                    else:
                        right = True

                    enemy.attack_state(right, left)
                    enemy.moving_state(False, False, False, False)

                    if enemy.animation.animation_progress == 5:
                        self.game.player.change_health(-enemy.attack_damage * self.game.settings.difficulty)
                        enemy.attack_state(False, False)
                else:
                    enemy.attack_state(False, False)
                    enemy.moving_state(False, False, False, False)

    def patrol(self, enemy):
        if enemy.action != Action.PATROL \
                and abs(enemy.initial_x_position - enemy.get_position()[0]) <= self.game.settings.enemy_speed:
            enemy.rect.x = enemy.initial_x_position
        if enemy.action != Action.PATROL \
                and abs(enemy.initial_y_position - enemy.get_position()[1]) <= self.game.settings.enemy_speed:
            enemy.rect.y = enemy.initial_y_position

        if enemy.action == Action.CHASE:
            enemy.action = Action.RETURN

        if enemy.action == Action.RETURN\
                and enemy.initial_x_position == enemy.get_position()[0] \
                and enemy.initial_y_position == enemy.get_position()[1]:
            enemy.action = Action.PATROL
        elif enemy.action == Action.RETURN:
            top, bottom, right, left = False, False, False, False
            if enemy.initial_x_position - enemy.get_position()[0] > 0:
                right = True
            if enemy.initial_x_position - enemy.get_position()[0] < 0:
                left = True
            if enemy.initial_y_position - enemy.get_position()[1] > 0:
                bottom = True
            if enemy.initial_y_position - enemy.get_position()[1] < 0:
                top = True
            enemy.moving_state(top, bottom, right, left)

        if enemy.action == Action.PATROL:
            if (not enemy.patrol_state and enemy.get_position()[0] - enemy.initial_x_position <= -100) or \
                    (enemy.patrol_state and enemy.get_position()[0] - enemy.initial_x_position >= 100):
                enemy.patrol_state = not enemy.patrol_state
            if enemy.patrol_state:
                enemy.moving_state(False, False, True, False)
            else:
                enemy.moving_state(False, False, False, True)

    def check_if_game_over(self):
        if self.game.player.current_health_points <= 0 or self.game.player.animation.animation_progress == 2 and \
                self.game.player.animation.animation_state == 3:
            my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
            pygame.event.post(my_event)
        if 1216 <= self.game.player.rect.x <= 1248 and 1344 <= self.game.player.rect.y <= 1410:
            # print("cave")
            player_alive = True

            for i in range(len(self.game.animation_sprites)):
                if not self.game.animation_sprites[i].is_dead:
                    player_alive = False

            if player_alive:
                my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
                pygame.event.post(my_event)
