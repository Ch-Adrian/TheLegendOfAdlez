import pygame

class Sword:

    def __init__(self, path, power, price):
        self.image = pygame.image.load(path).convert_alpha()
        self.power = power
        self.price = price

    def render_graphics(self, surface, position):
        surface.blit(self.image, position)

    def get_power(self):
        return self.power

    def get_price(self):
        return self.price
