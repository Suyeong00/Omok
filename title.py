import pygame
from button import Button
from dropdown import Dropdown
from state import Status

# def set_level(state, ai_arrangement, level):
#     state.status = Status.Ai
#     ai_arrangement.set_level(level)
#     print("level =", level)

# def get_dropdown(screen_size, state, ai_arrangement):
#     dropdown_options = [
#         {"text": "하 (3수)", "callback": set_level(state, ai_arrangement, 3)},
#         {"text": "중 (5수)", "callback": set_level(state, ai_arrangement, 5)},
#         {"text": "상 (7수)", "callback": set_level(state, ai_arrangement, 7)}
#     ]

#     return Dropdown("인공지능과 플레이", screen_size[0] // 2 - 100, 400, 200, 50, dropdown_options)

def get_dropdown(screen_size):
    def handle_option_click(option_text):
        print(f"{option_text} 버튼 눌렀음")

    dropdown_options = [
        {"text": "하 (3수)", "callback": lambda: handle_option_click("하 (3수)")},
        {"text": "중 (5수)", "callback": lambda: handle_option_click("중 (5수)")},
        {"text": "상 (7수)", "callback": lambda: handle_option_click("상 (7수)")}
    ]

    return Dropdown("인공지능과 플레이", screen_size[0] // 2 - 100, 400, 200, 50, dropdown_options)

def draw_title(screen, screen_size, state, dropdown, ai_arrangement):
    screen.fill((255, 255, 255))  # 흰색 배경

    def set_state_description():
        state.status = Status.Description

    def set_state_pvp():
        state.status = Status.PvP

    def set_state_ai(level):
        state.status = Status.Ai
        print(f"AI Level selected: {level}")

    # 버튼 생성
    description_button = Button("설명서", screen_size[0] // 2 - 100, 200, 200, 50, set_state_description)
    pvp_button = Button("2인 플레이", screen_size[0] // 2 - 100, 300, 200, 50, set_state_pvp)

        # 버튼 그리기
    description_button.draw(screen)
    pvp_button.draw(screen)
    dropdown.draw(screen)

    # 이벤트 처리
    for event in pygame.event.get():
        description_button.is_clicked(event)
        pvp_button.is_clicked(event)
        dropdown.is_clicked(event)
