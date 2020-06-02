# Module for Player classes

from board_module import Board
from try_type import *

#---Generic Player Class---#
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play_move(self,board):
        return 0

#---Human Player Class---#
class HumanPlayer(Player):
    def play_move(self,board):
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
class ComputerPlayer(Player):
    def play_move(self,board):
        for i in range(board.get_width()):
            if board.place_piece(i, self.symbol):
                return i
        return 0
