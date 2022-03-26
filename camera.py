import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.middle_x = self.display_surface.get_size()[0] // 2
        self.middle_y = self.display_surface.get_size()[1] // 2
        self.direction = pygame.math.Vector2()

    def draw(self, player):
        self.direction.x = player.rect.centerx - self.middle_x
        self.direction.y = player.rect.centery - self.middle_y
        for sprite in self.sprites():
            position = sprite.rect.topleft - self.direction
            self.display_surface.blit(sprite.image, position)
