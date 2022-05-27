import pygame
from sword import Sword

class Equipment:

    def __init__(self, items_limit):
        self.items = []
        self.items_limit = items_limit
        self.current_sword_index = 0
        self.items.append(Sword("resources/map1/assets/weapons/wooden_sword.png", 10, 0))

    def add_new_sword(self, path, power, price):
        self.items.append(Sword(path, power, price))
        self.current_sword_index = len(self.items) - 1

    def display_current_equipment(self):
        if self.current_sword_index is not None:
            width, height = pygame.display.get_surface().get_size()
            self.items[self.current_sword_index].render_graphics(pygame.display.get_surface(), (width - 64, height - 64))

    def change_sword(self):
        if self.current_sword_index is not None:
            self.current_sword_index = (self.current_sword_index + 1) % len(self.items)

    def get_sword_power(self):
        if self.current_sword_index is not None:
            return self.items[self.current_sword_index].power
        return 0

    def get_items(self):
        return self.items

    def attach_sword(self, sword):
        if sword is not None:
           self.items.append(sword)
        self.current_sword_index = len(self.items) - 1

    def remove_at_index(self, index):
        value = self.items[index].get_price()
        del self.items[index]
        self.current_sword_index = len(self.items) - 1 if len(self.items) > 1 else None
        return value



