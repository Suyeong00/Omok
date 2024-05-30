import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen_size = (800, 800)  # 화면 크기
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Baduk Board")

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 바둑판 설정
board_size = 19  # 바둑판 크기 (19x19)
cell_size = screen_size[0] // (board_size + 1)  # 칸 크기
margin = cell_size  # 테두리 여백

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
