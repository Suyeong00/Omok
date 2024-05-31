import arrangement
from collections import deque

MIN = -100000000
MAX = 100000000

def evaluate(state):
    size = 19  # 오목판 크기
    score = 0

    board = state.get_board_status()
    player = state.get_player()

    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size

    def count_opponent_nearby(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and board[nx][ny] == (3 - player):
                count += 1
        return count

    def check_pattern(pattern, base_score, penalty_per_opponent, locations):
        nonlocal score
        found = True
        for dx, dy in locations:
            nx, ny = x + dx, y + dy
            if not (is_valid(nx, ny) and board[nx][ny] == pattern):
                found = False
                break
        if found:
            opponent_nearby = sum(count_opponent_nearby(x + dx, y + dy) for dx, dy in locations) 
            score += base_score - opponent_nearby * penalty_per_opponent

    for x in range(size):
        for y in range(size):
            if board[x][y] == player:
                # 같은 색의 돌이 근처에 하나도 없는 경우
                if count_opponent_nearby(x, y) == 0:
                    score += 5
                else:
                    score += 5 - count_opponent_nearby(x, y)

                # 같은 색의 두 돌이 상하좌우로 인접한 경우
                check_pattern(player, 100, 10, [(0, 0), (0, 1)])
                check_pattern(player, 100, 10, [(0, 0), (1, 0)])

                # 같은 색의 두 돌이 대각선으로 인접한 경우
                check_pattern(player, 500, 70, [(0, 0), (1, 1)])
                check_pattern(player, 500, 70, [(0, 0), (1, -1)])

                # 같은 색의 세 돌이 가로 혹은 세로로 일자로 붙어있는 경우
                check_pattern(player, 5000, 400, [(0, 0), (0, 1), (0, 2)])
                check_pattern(player, 5000, 400, [(0, 0), (1, 0), (2, 0)])

                # 같은 색의 세 돌이 대각선으로 일자로 붙어있는 경우
                check_pattern(player, 10000, 600, [(0, 0), (1, 1), (2, 2)])
                check_pattern(player, 10000, 600, [(0, 0), (1, -1), (2, -2)])

                # 같은 색의 세 돌이 특정 모양으로 존재하는 경우
                check_pattern(player, 15000, 600, [(0, 0), (-1, -1), (-1, 1)])
                check_pattern(player, 15000, 600, [(0, 0), (-1, -1), (1, -1)])
                check_pattern(player, 15000, 600, [(0, 0), (1, -1), (1, 1)])
                check_pattern(player, 15000, 600, [(0, 0), (1, 1), (-1, 1)])

                # 같은 색의 네 돌이 특정 모양으로 존재하는 경우
                check_pattern(player, 100000, 8000, [(0, 0), (0, -1), (0, 1), (1, 0)])
                check_pattern(player, 100000, 8000, [(0, 0), (0, -1), (0, 1), (-1, 0)])
                check_pattern(player, 100000, 8000, [(0, 0), (0, -1), (-1, 0), (1, 0)])
                check_pattern(player, 100000, 8000, [(0, 0), (0, 1), (-1, 0), (1, 0)])

                # 같은 색의 네 돌이 특정 모양으로 존재하는 경우
                check_pattern(player, 500000, 15000, [(0, 0), (-1, -1), (1, -1), (-1, 1)])
                check_pattern(player, 500000, 15000, [(0, 0), (-1, -1), (1, 1), (-1, 1)])
                check_pattern(player, 500000, 15000, [(0, 0), (-1, -1), (1, -1), (1, 1)])
                check_pattern(player, 500000, 15000, [(0, 0), (-1, 1), (1, -1), (1, 1)])
 

                # 같은 색의 네 돌이 특정 모양으로 존재하는 경우
                check_pattern(player, 50000, 40000, [(0, 0), (1, 1), (2, 2), (2, 2)])

                # 같은 색의 다섯 돌이 특정 모양으로 존재하는 경우
                check_pattern(player, MAX, 0, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
                check_pattern(player, MAX, 0, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
                check_pattern(player, MAX, 0, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])

    return score

def player(state):
    return state.get_player

def action(state):
    board = state.get_board_status()
    player = state.get_player()
    size = 19  # 오목판 크기
    actions = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size

    visited = [[False for _ in range(size)] for _ in range(size)]

    queue = deque()

    # 플레이어의 돌 위치를 큐에 추가
    for x in range(size):
        for y in range(size):
            if board[x][y] == player:
                queue.append((x, y, 0))  # (x, y, 거리)
                visited[x][y] = True

    while queue:
        x, y, dist = queue.popleft()

        if dist > 2:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    actions.append((nx, ny))
                queue.append((nx, ny, dist + 1))

    # 중복된 좌표를 제거하기 위해 set을 사용
    actions = list(set(actions))

    return actions

def utility(state):
    return evaluate(state)

def result(state, action):
    state.place_white

def terminal(state):
    if state.get_player == 1 and evaluate(state) == MAX: 
        return True
    if state.get_player == 2 and evaluate(state) == MIN: 
        return True
    return False
    
def print_board_with_actions(board, actions):
    size = 19
    display_board = [['.' for _ in range(size)] for _ in range(size)]

    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                display_board[x][y] = 'B'
            elif board[x][y] == 2:
                display_board[x][y] = 'W'

    for (x, y) in actions:
        display_board[x][y] = '*'

    for row in display_board:
        print(' '.join(row))

# 예시 보드 (19x19)와 플레이어 설정
state = arrangement.Arrangement()
state.set_unit(8, 8, 1)
state.set_unit(9, 9, 1)

# 함수 호출 예시
score = evaluate(state)
print("Score:", score)

board = state.get_board_status()
actions = action(state)

print_board_with_actions(board, actions)

def max_value(state):
    if terminal(state):
        return utility(state)
    v = MIN
    for action in actions(state):
        v = max(v, min_value(result(action, state)))
    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    v = MAX
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v



    