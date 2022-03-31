import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, path_texture, groups):
        super().__init__(groups)
        self.image = pygame.image.load(path_texture).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


