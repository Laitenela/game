class Board(object):

    def __init__(self, board_range):
        self.boardRange = board_range
        self.board = [['0' * self.boardRange] * self.boardRange]

    def clr(self):
        self.board = [['0' * self.boardRange] * self.boardRange]

    def start_print(self):
        self.clr()

    def print(self, monster):
        self.board[monster.y][monster.x] = monster.symbol

    def end_print(self):
        print(self.board)