import pygame


class AnimateMe:

    def __init__(self, character, animation_params, path):
        self.character = character
        self.animation_state = 0
        self.animation_params = animation_params

        self.animation_list_sprites = []
        for i in range(4):
            animation_sprites = []
            for j in range(animation_params[i][1]):
                _str = '/animation'+str(i)+'/'+str(j)+'.png'
                animation_sprites.append(pygame.image.load(path+_str))
            self.animation_list_sprites.append(animation_sprites)

        self.animation_progress = 0
        self.delay = 0

    def nextAnimation(self):
        print("nextAnimation", self.animation_progress)
        # 0 - idle
        long = self.animation_params[self.animation_state][1]
        row = self.animation_params[self.animation_state][0]

        self.character.image = self.animation_list_sprites[row][self.animation_progress]
        if self.delay == 15:
            self.animation_progress = (self.animation_progress+1)%long
        self.delay = (self.delay+1)%16


    def change_animatin_state(self, state):
        self.animation_progress = 0
        self.animation_state = state