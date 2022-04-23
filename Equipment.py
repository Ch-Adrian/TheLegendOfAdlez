import pygame


class Equipment(pygame.sprite.Sprite):

    def __init__(self, settings, position, groups, path):
        super().__init__(groups)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.settings = settings

        self.isSword1 = False
        self.sword_object1 = None

    def setElement(self, surface, screen_width, screen_height):
        surface.blit(self.image, (screen_width-64, screen_height//2 - 128))
        if self.isSword1:
            self.sword_object1.render_graphics(surface, (screen_width-64, screen_height//2 - 128))

    def add_sword1(self, sword_object):
        self.isSword1 = True
        self.sword_object1 = sword_object