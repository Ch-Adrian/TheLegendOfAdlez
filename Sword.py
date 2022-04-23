import pygame


class Sword(pygame.sprite.Sprite):

    def __init__(self, path):
        self.image = pygame.image.load(path).convert_alpha()

    def render_graphics(self, surface, position):
        surface.blit(self.image, position)
