import pygame
import sys
import configuration
from button import Button
from state import Status

font = configuration.font


def draw_description(screen, screen_size, state):
    screen.fill((255, 255, 255))  # 흰색 배경

    def go_back():
        state.status = Status.Main

    back_button = Button("뒤로가기", screen_size[0] // 2 - 50, 20, 100, 50, go_back)
    back_button.draw(screen)

    rule_lines = [
        "뉴목 룰:",
        "미완성"
    ]

    for i, line in enumerate(rule_lines):
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (50, 100 + i * 40))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        back_button.is_clicked(event)
