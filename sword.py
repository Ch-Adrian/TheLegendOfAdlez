import pygame

class Sword:

    def __init__(self, path, power):
        self.image = pygame.image.load(path).convert_alpha()
        self.power = power

    def render_graphics(self, surface, position):
        surface.blit(self.image, position)
