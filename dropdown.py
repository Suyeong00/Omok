import pygame
import configuration

font = configuration.font

class Dropdown:
    def __init__(self, text, x, y, width, height, options, callback=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = configuration.GRAY
        self.options = options
        self.is_open = False
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, configuration.BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        if self.is_open:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, self.color, option_rect)
                option_surface = font.render(option, True, configuration.BLACK)
                option_text_rect = option_surface.get_rect(center=option_rect.center)
                screen.blit(option_surface, option_text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open
            elif self.is_open:
                for i, option in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        if self.callback:
                            self.callback(option)
                        self.is_open = False
