import pygame
from button import Button
from dropdown import Dropdown
from state import Status

def draw_title(screen, screen_size, state):
    screen.fill((255, 255, 255))  # 흰색 배경

    def set_state_description():
        state.status = Status.Description

    def set_state_pvp():
        state.status = Status.PvP

    def set_state_ai(level):
        state.status = Status.Ai

    # 버튼 생성
    description_button = Button("설명서", screen_size[0] // 2 - 100, 200, 200, 50, set_state_description)
    pvp_button = Button("2인 플레이", screen_size[0] // 2 - 100, 300, 200, 50, set_state_pvp)
    ai_dropdown = Dropdown("인공지능과 플레이", screen_size[0] // 2 - 100, 400, 200, 50, ["하", "중", "상"], set_state_ai)

    # 버튼 그리기
    description_button.draw(screen)
    pvp_button.draw(screen)
    ai_dropdown.draw(screen)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        description_button.is_clicked(event)
        pvp_button.is_clicked(event)
        ai_dropdown.is_clicked(event)
        if ai_dropdown.is_open:
            for i, option in enumerate(ai_dropdown.options):
                option_rect = pygame.Rect(ai_dropdown.rect.x, ai_dropdown.rect.y + (i + 1) * ai_dropdown.rect.height, ai_dropdown.rect.width, ai_dropdown.rect.height)
                if event.type == pygame.MOUSEBUTTONDOWN and option_rect.collidepoint(event.pos):
                    set_state_ai(option)
                    ai_dropdown.is_open = False
