import pygame
from sword import Sword

class Equipment:

    def __init__(self):
        self.swords = []
        self.current_sword_index = 0
        self.swords.append(Sword("resources/map1/assets/weapons/wooden_sword.png", 10))

    def add_new_sword(self, path, power):
        self.swords.append(Sword(path, power))

    def display_current_equipment(self):
        width, height = pygame.display.get_surface().get_size()
        self.swords[self.current_sword_index].render_graphics(pygame.display.get_surface(), (width - 64, height - 64))

    def change_sword(self):
        self.current_sword_index = (self.current_sword_index + 1) % len(self.swords)

    def get_sword_power(self):
        return self.swords[self.current_sword_index].power



