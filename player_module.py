# Module for Player classes

from board_module import Board, board_clone
from try_type import *
import random
import time

#---Generic Player Class---#
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play_move(self, board, opponent):
        return 0

#---Human Player Class---#
class HumanPlayer(Player):
    def play_move(self, board, opponent):
        while True:
            column = input("Select a column to place your piece (1 - "
                + str(board.get_width()) + "): ")
            if not try_int(column):
                print("Please enter a valid integer!")
            column = int(column) - 1
            if column < 0 or column >= board.get_width():
                print("Value must be between 1 and "
                    + str(board.get_width()) + "!")
                continue
            if not board.place_piece(column, self.symbol):
                continue
            return column
        return 0


#---Computer Player Class---#
SEARCH_DEPTH = 6

class ComputerPlayer(Player):

    def play_move(self, board, opponent):
        move = self.alphabeta(board, opponent)
        board.place_piece(move, self.symbol)
        return move

    def alphabeta(self, board, opponent):
        alpha = -SEARCH_DEPTH - 10
        beta = SEARCH_DEPTH + 10
        best_score = -SEARCH_DEPTH - 10
        best_option = 0
        check_range = list(range(board.get_width()))
        random.shuffle(check_range)
        for i in check_range:
            if not board.check_column(i):
                continue
            new_board = board_clone(board)
            new_board.place_piece(i,self.symbol)
            value = self.alphabeta_recursive(new_board, opponent, alpha,
                beta, SEARCH_DEPTH, False)
            if value > best_score:
                best_score = value
                best_option = i
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_option

    def alphabeta_recursive(self, board, opponent,
            alpha, beta, depth, player_turn):
        a = alpha
        b = beta
        if board.detect_win() != None:
            if player_turn:
                return -depth - 5
            return depth + 5
        if board.detect_end():
            return 0
        if depth == 0:
            return 0
        check_range = list(range(board.get_width()))
        random.shuffle(check_range)
        if player_turn:
            value = -SEARCH_DEPTH - 10
            for i in check_range:
                if not board.check_column(i):
                    continue
                new_board = board_clone(board)
                new_board.place_piece(i,self.symbol)
                value = max(value, self.alphabeta_recursive(new_board,
                    opponent, a, b, depth - 1, False))
                a = max(a, value)
                if a >= b:
                    break
            return value
        else:
            value = SEARCH_DEPTH + 10
            for i in check_range:
                if not board.check_column(i):
                    continue
                new_board = board_clone(board)
                new_board.place_piece(i,opponent.symbol)
                value = min(value, self.alphabeta_recursive(new_board,
                    opponent, a, b, depth - 1, True))
                b = min(b, value)
                if a >= b:
                    break
            return value

    def heuristic(self, board):
        pass
