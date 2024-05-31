class Arrangement:
    def __init__(self):
        self.board_size = 19
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1

    def reset_board(self):
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1

    def place_black(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = 1  # black
            self.current_player = 0

    def place_white(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = 2  # white
            self.current_player = 1

    def get_board_status(self):
        return self.board

    def get_unit(self, x, y):
        return self.board[x][y]
    
    def set_unit(self, x, y, value):
        self.board[x][y] = value
