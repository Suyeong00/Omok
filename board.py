import pygame
import sys
import configuration
from button import Button
from state import Status

# 바둑판 설정
board_size = 19  # 바둑판 크기 (19x19)

# units : 바둑 판 위 바둑알 상태
def draw_board(screen, screen_size, state, units):
    cell_size = screen_size[0] // (board_size + 1)  # 칸 크기
    margin = cell_size  # 테두리 여백

    # 화면을 흰색으로 채우기
    screen.fill(configuration.WHITE)

    # 뒤로가기 버튼 생성
    def go_back():
        state.status = Status.Main

    back_button = Button("뒤로가기", screen_size[0] // 2 - 50, 20, 100, 50, go_back)
    back_button.draw(screen)

    # 가로선 그리기
    for row in range(board_size):
        y = margin + row * cell_size + 100
        pygame.draw.line(screen, configuration.BLACK, (margin, y), (screen_size[0] - margin, y))

    # 세로선 그리기
    for col in range(board_size):
        x = margin + col * cell_size
        pygame.draw.line(screen, configuration.BLACK, (x, margin + 100), (x, screen_size[0] - margin + 100))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        back_button.is_clicked(event)