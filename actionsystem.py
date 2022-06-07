import random
import sys

import pygame


class ActionSystem:

    def __init__(self, game):
        self.game = game

    def attack_system(self):

        for char in self.game.animation_sprites:
            if char.is_dead:
                continue
            c_x, c_y = char.get_position()
            p_x, p_y = self.game.player.get_position()
            d = self.game.distance((c_x, c_y), (p_x, p_y))
            if d > 200:
                self.patrol(char)

            elif 35 < d <= 200:
                char.action = 1
                # print(d)
                top = False
                bottom = False
                right = False
                left = False
                if p_x+10 < c_x:
                    left = True
                elif p_x-10 > c_x:
                    right = True
                else:
                    top = char.moving_up
                    bottom = char.moving_down
                if p_y+10 < c_y:
                    top = True
                elif p_y-10 > c_y:
                    bottom = True
                else:
                    left = char.moving_left
                    right = char.moving_right

                char.moving_state(top, bottom, right, left)
            elif d <= 35:
                if self.game.player.is_attacking:
                    # print("Player is attacking")
                    # print(self.player.animation.animation_state,self.player.animation.animation_progress )
                    if (self.game.player.animation.animation_state == 2 or self.game.player.animation.animation_state == 6) and self.game.player.animation.animation_progress == 2:
                        # print("almost hit")
                        if abs(p_y - c_y) < 40:
                            # print("HIT!!!!")
                            if char.change_health(-self.game.player.get_total_power()):
                                self.game.player.add_experience(200//len(self.game.animation_sprites))
                                self.game.player.change_gold(random.randint(1, 15))
                            self.game.player.animation.change_animation_state(0)

                right = False
                left = False
                if p_x < c_x:
                    left = True
                else:
                    right = True
                char.attack_state(right, left)
                char.moving_state(False, False, False, False)
                if char.animation.animation_progress == 5:
                    self.game.player.change_health(-char.attack_damage * self.game.settings.difficulty_values[self.game.settings.difficulty])
                    char.attack_state(False, False)
            else:
                char.attack_state(False, False)
                char.moving_state(False, False, False, False)

    def patrol(self, char):
        if char.action != 0 and abs(char.initial_x_position - char.get_position()[0]) <= self.game.settings.enemy_speed:
            char.rect.x = char.initial_x_position
        if char.action != 0 and abs(char.initial_y_position - char.get_position()[1]) <= self.game.settings.enemy_speed:
            char.rect.y = char.initial_y_position

        # if char.initial_x_position == 770 and char.initial_y_position == 820:
        #   pass  # Zombie testing
        # Actions: 0 - patrolling, 1 - attacking, 2 - returning to initial position
        if char.action == 1:
            char.action = 2
        if char.action == 2 and char.initial_x_position == char.get_position()[0] and char.initial_y_position == \
                char.get_position()[1]:
            char.action = 0
        elif char.action == 2:
            top, bottom, right, left = False, False, False, False
            if char.initial_x_position - char.get_position()[0] > 0: right = True
            if char.initial_x_position - char.get_position()[0] < 0: left = True
            if char.initial_y_position - char.get_position()[1] > 0: bottom = True
            if char.initial_y_position - char.get_position()[1] < 0: top = True
            char.moving_state(top, bottom, right, left)
        if char.action == 0:
            if (not char.patrol_state and char.get_position()[0] - char.initial_x_position <= -100) or (char.patrol_state and char.get_position()[0] - char.initial_x_position >= 100):
                char.patrol_state = not char.patrol_state
            if char.patrol_state:
                char.moving_state(False, False, True, False)
            else:
                char.moving_state(False, False, False, True)

    def game_over(self):
        mouse_click = False
        while True:
            self.game.screen.fill((0, 0, 0))
            title = self.game.font.render("Game over", True, (0, 120, 120))
            score = self.game.font.render(f"Score: {self.game.map.player.experience}", True, (0, 120, 120))
            width, height = self.game.screen.get_size()
            self.game.screen.blit(title, (width / 2 - 60, 100))
            self.game.screen.blit(score, (width / 2 - 53, 150))

            exit_button = pygame.Rect(width / 2 - 50, 250, 100, 50)
            pygame.draw.rect(self.game.screen, (0, 120, 120), exit_button)
            exit_text = self.game.font.render("Exit", True, (0, 0, 0))
            self.game.screen.blit(exit_text, (width / 2 - 20, 260))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_click:
                if exit_button.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_click = True
            pygame.display.update()
            self.game.clock.tick(self.game.settings.frames_per_second)

    def game_is_end(self):
        # print(self.player.animation.animation_progress, self.player.animation.animation_state)
        if self.game.player.current_health_points <= 0 or self.game.player.animation.animation_progress == 2 and self.game.player.animation.animation_state == 3:
            my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
            pygame.event.post(my_event)
        if self.game.player.rect.x >= 1216 and self.game.player.rect.x <= 1248 and self.game.player.rect.y >= 1344 and self.game.player.rect.y <= 1410:
            # print("cave")
            is_alive = True

            for i in range(len(self.game.animation_sprites)):
                if not self.game.animation_sprites[i].is_dead:
                    is_alive = False

            if is_alive:
                my_event = pygame.event.Event(pygame.USEREVENT, message="Game over")
                pygame.event.post(my_event)

