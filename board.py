import pygame
import sys
import configuration
from button import Button
from state import Status

def draw_board(screen, screen_size, state, arrangement):
    # 바둑판 설정
    board_size = 19  # 바둑판 크기 (19x19)

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

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 마우스가 위치한 셀 찾기
    col = (mouse_x - margin + cell_size // 2) // cell_size
    row = (mouse_y - 100 - margin + cell_size // 2) // cell_size

    # 바둑판 안에 있는지 확인
    if 0 <= col < board_size and 0 <= row < board_size:
        x = margin + col * cell_size
        y = margin + row * cell_size + 100
        # 반투명한 돌 그리기
        pygame.draw.circle(screen, configuration.GRAY, (x, y), cell_size // 3, width=1)

    # 실제 돌 놓기
    for r in range(board_size):
        for c in range(board_size):
            if arrangement.board[r][c] == 1:
                x = margin + c * cell_size
                y = margin + r * cell_size + 100
                pygame.draw.circle(screen, configuration.BLACK, (x, y), cell_size // 3)
            elif arrangement.board[r][c] == 2:
                x = margin + c * cell_size
                y = margin + r * cell_size + 100
                pygame.draw.circle(screen, configuration.WHITE, (x, y), cell_size // 3)

    def place_unit(event, col, row, board_size, arrangement):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= col < board_size and 0 <= row < board_size:
                    if arrangement.board[row][col] == 0:  # 빈 칸에만 돌을 놓음
                        if arrangement.current_player == 1: # current_player가 1이면 흑돌의 차례
                            arrangement.place_black(row, col)  # 흑돌을 놓음
                            print(row, col, "black")
                        else:
                            arrangement.place_white(row, col)  # 백돌을 놓음
                            print(row, col, "white")

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        back_button.is_clicked(event)
        place_unit(event, col, row, board_size, arrangement)