# %
import numpy as np

class bingo_lisener:
    def __init__(self):
        self.has_winner=False
        self.winner = None
        self.winning_number = 0
    def post_winner(self, winner):
        self.has_winner = True
        self.winner = winner

def parse_line(line):
    return [int(x) for x in line.split()]


class board:
    def __init__(self, lines, listener):
        self.listener = listener
        self.grid = np.array([parse_line(line) for line in lines])

    def check_num(self, num):
        for i in np.nditer(self.grid, op_flags = ['readwrite']):
            if i == num: i[...] = 0
        self.bingo()
        return self
    def bingo(self):
        cols = self.grid.sum(0)
        rows = self.grid.sum(1)
        print(cols)
        if not all(cols) or not all(rows):
             print("Winner!")
             self.listener.post_winner(self)
    def getscore(self):
        return self.grid.sum()

def get_boards(listener, lines):
    boards = []
    board_lines = []
    for line in lines[2:]:
        if len(line) <5:
            boards.append(board(board_lines, listener))
            board_lines = []
        else:
            board_lines.append(line)
    return boards


with open('1/data.txt') as f:
    lines = f.readlines()
listener = bingo_lisener()
balls = lines[0].split(",")
boards = get_boards(listener,lines)
for ball in balls:
    if(listener.has_winner): break
    boards = [b.check_num(int(ball)) for b in boards]
    if(listener.has_winner):
        listener.winning_number = int(ball)
        break
print(listener.winner.getscore() * listener.winning_number)
