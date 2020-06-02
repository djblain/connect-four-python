# Module for Board Class

from try_type import *

class Board:
    def __init__(self, goal, width, height):
        self.goal = goal
        self.board = [[None for _ in range(height)] for _ in range(width)]
        self.column_top = [0 for _ in range(width)]

    def get_width(self):
        return len(self.board)

    def get_height(self):
        return len(self.board[0])

    def check_column(self, column):
        return (self.column_top[column] < self.get_height())

    def place_piece(self, column, piece):
        if not try_str(piece):
            print("ERROR: not a string value")
            return False
        if not self.check_column(column):
            print("Column full, cannot place here!")
            return False
        self.board[column][self.column_top[column]] = str(piece)[0]
        self.column_top[column] += 1
        return True

    def print_board(self):
        print("".join([(" " + str(i+1)) for i in range(self.get_width())]))
        for row in range(self.get_height()-1,-1,-1):
            print("".join(["+-" for _ in self.board]) + "+")
            print("".join(["|" + (" " if self.board[col][row] == None else
                self.board[col][row]) for col in
                range(self.get_width())]) + "|")
        print("".join(["+-" for _ in self.board]) + "+")

    def check_line_match(self, column, row, col_delta, row_delta, length):
        ci = 0
        ri = 0
        for _ in range(1,length):
            ci += col_delta
            ri += row_delta
            if (column + ci >= self.get_width() or column + ci < 0):
                return False
            if (row + ri >= self.get_width() or row + ri < 0):
                return False
            if (self.board[column][row] != self.board[column + ci][row + ri]):
                return False
        return True

    def detect_win(self):
        for c in range(self.get_width()):
            for r in range(self.get_height()):
                if self.board[c][r] == None:
                    continue
                # check horizontal
                if self.check_line_match(c,r,1,0,self.goal):
                    return self.board[c][r]
                # check vertical
                if self.check_line_match(c,r,0,1,self.goal):
                    return self.board[c][r]
                # check diagonal 1
                if self.check_line_match(c,r,1,1,self.goal):
                    return self.board[c][r]
                # check diagonal 2
                if self.check_line_match(c,r,1,-1,self.goal):
                    return self.board[c][r]
        return None

    def detect_end(self):
        for c in range(self.get_width()):
            if self.column_top[c] < self.get_height():
                return False
        return True
