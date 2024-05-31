import pygame
import configuration

font = configuration.font

class Button:
    def __init__(self, text, x, y, width, height, callback=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = configuration.GRAY
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, configuration.BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()