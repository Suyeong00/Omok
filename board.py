import pygame

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 바둑판 설정
board_size = 19  # 바둑판 크기 (19x19)

# status : 바둑 판 위 바둑알 상태
def draw_board(screen, screen_size, status):
    cell_size = screen_size[0] // (board_size + 1)  # 칸 크기
    margin = cell_size  # 테두리 여백

    # 화면을 흰색으로 채우기
    screen.fill(WHITE)

    # 가로선 그리기
    for row in range(board_size):
        y = margin + row * cell_size
        pygame.draw.line(screen, BLACK, (margin, y), (screen_size[0] - margin, y))

    # 세로선 그리기
    for col in range(board_size):
        x = margin + col * cell_size
        pygame.draw.line(screen, BLACK, (x, margin), (x, screen_size[1] - margin))
