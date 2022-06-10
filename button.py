import pygame


class Button:

    def __init__(self, screen, width, height, button_color, text_color, text_size, y, text=None, x=None):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.button_color = button_color
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.SysFont("Arial", text_size)
        self._prepare_button()

    def _prepare_button(self):
        self.button_rect = pygame.Rect(0, self.y, self.width, self.height)
        self.button_rect.centerx = self.screen.get_rect().centerx
        if self.x is not None:
            self.button_rect.x = self.x
        self.text_label = self.font.render(self.text, True, self.text_color, self.button_color)
        self.text_rect = self.text_label.get_rect()
        self.text_rect.center = self.button_rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.text_label, self.text_rect)

    def collidepoint(self, mouse_position):
        return self.button_rect.collidepoint(mouse_position)
