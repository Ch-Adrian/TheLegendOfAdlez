import pygame

class Spritesheet:

    def __init__(self, path):
        self.path = path;
        self.image = pygame.image.load(path).convert_alpha();

    def get_sprite(self, x, y, w , h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.image, (0,0), (x,y,w,h))
        return sprite