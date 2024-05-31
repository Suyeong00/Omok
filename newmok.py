import pygame
import sys
from title import draw_title, get_dropdown
from pvp_board import draw_pvp_board
from description import draw_description
from state import State, Status
from arrangement import Arrangement

# Pygame 초기화
pygame.init()

# 화면 설정
screen_size = (600, 700)  # 화면 크기
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Newmok")

units = "구현예정"
state = State()

# 게임 루프
running = True
pvp_arrangement = Arrangement()
ai_arrangement = Arrangement()
#ai_dropdown = get_dropdown(screen_size, state, ai_arrangement)
ai_dropdown = get_dropdown(screen_size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not running : break

    if state.status == Status.Main:
        pvp_arrangement.reset_board()
        ai_arrangement.reset_board()
        draw_title(screen, screen_size, state, ai_dropdown, ai_arrangement)
    elif state.status == Status.PvP:
        draw_pvp_board(screen, screen_size, state, pvp_arrangement)
    elif state.status == Status.Description:
        draw_description(screen, screen_size, state)
    elif state.status == Status.Ai:
        # AI 대전 화면 구현
        pass

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
