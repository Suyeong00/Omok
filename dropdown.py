import pygame
from button import Button  # 버튼 클래스 import
from configuration import BLACK, GRAY, font  # 색상 및 폰트 import

class Dropdown:
    def __init__(self, text, x, y, width, height, options):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.options = [option['text'] for option in options]
        self.is_open = False
        self.buttons = [
            Button(option['text'], x, y + (i + 1) * height, width, height, option['callback'])
            for i, option in enumerate(options)
        ]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        if self.is_open:
            for button in self.buttons:
                button.draw(screen)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open
            elif self.is_open:
                for button in self.buttons:
                    button.is_clicked(event)
