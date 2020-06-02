# Simple Python command-line program for a game of connect four
# Can be played solo (vs. AI) or two-player

import try_type
from board_module import *
from player_module import *

NAME_LENGTH_MIN = 3
NAME_LENGTH_MAX = 16

GOAL_SIZE_MIN = 3
GOAL_SIZE_MAX = 7

BOARD_DIMENSION_MIN = { 3:5, 4:6, 5:7, 6:8, 7:9 }
BOARD_DIMENSION_MAX = { 3:7, 4:9, 5:11, 6:13, 7:15 }

PLAYER_SYMBOLS = { '1':'X', '2':'O' }

def main():
    print("Welcome to Konnect X, the X-in-a-row game!")
    #---player details---#
    players = init_players()
    #---board details---#
    board = init_board()
    play_game(players, board)
    return

def play_game(players, board):
    turn = 1
    print("Connect " + str(board.goal) + "-in-a-row to win!")
    board.print_board()
    winner = None
    while winner == None:
        for p in players.values():
            winner = board.detect_win()
            if winner != None:
                print(str(players['1'].name if winner == players['1'].symbol
                    else players['2'].name) + " wins!")
                break
            if board.detect_end():
                winner = 0
                print("It's a tie!")
                break
            print("".join(["-" for _ in range(board.get_width() * 2 + 1)]))
            print("Turn " + str(turn) + " for " + p.name)
            move = p.play_move(board)
            print(p.name + " put their piece in column " + str(move + 1) + ".")
            board.print_board()
        turn += 1
    return

def init_players():
    players = { '1': None, '2':None }
    for key in players:
        player_name = ""
        player_ai = None
        while len(player_name) == 0:
            input_name = input("Enter a name for player "
                + key + ": ")
            if (len(input_name) > NAME_LENGTH_MAX
                    or len(input_name) < NAME_LENGTH_MIN):
                print("Name must be between " + str(NAME_LENGTH_MIN) + " and "
                    + str(NAME_LENGTH_MAX) + " characters!")
            else:
                player_name = input_name
        while player_ai == None:
            input_ai = input("Is " + player_name
                + " an AI player? (y/n): ").upper()
            if input_ai == "Y":
                player_ai = True
            elif input_ai == "N":
                player_ai = False
            else:
                print("Please specify with 'y' or 'n'!")
        print("Player " + key + " is called " + player_name
            + " and is a " + ("computer" if player_ai else "human")
            + "!")
        if player_ai:
            players[key] = ComputerPlayer(player_name, PLAYER_SYMBOLS[key])
        else:
            players[key] = HumanPlayer(player_name, PLAYER_SYMBOLS[key])
    return players

def init_board():
    goal_length = None
    board_width = None
    board_height = None
    while goal_length == None:
        input_goal = input("Enter the winning row length ("
            + str(GOAL_SIZE_MIN) + " - " + str(GOAL_SIZE_MAX)
            + "): ")
        if try_type.try_int(input_goal):
            input_goal = int(input_goal)
            if input_goal < GOAL_SIZE_MIN or input_goal > GOAL_SIZE_MAX:
                print("Winning length must be between " + str(GOAL_SIZE_MIN)
                    + " and " + str(GOAL_SIZE_MAX) + "!")
            else:
                goal_length = input_goal
        else:
            print("Please enter an integer value!")
    while board_width == None:
        input_width = input("Enter the game board width ("
            + str(BOARD_DIMENSION_MIN[goal_length]) + " - "
            + str(BOARD_DIMENSION_MAX[goal_length]) + "): ")
        if try_type.try_int(input_width):
            input_width = int(input_width)
            if (input_width < BOARD_DIMENSION_MIN[goal_length]
                    or input_width > BOARD_DIMENSION_MAX[goal_length]):
                print("Board width must be between "
                    + str(BOARD_DIMENSION_MIN[goal_length]) + " and "
                    + str(BOARD_DIMENSION_MAX[goal_length]) + "!")
            else:
                board_width = input_width
        else:
            print("Please enter an integer value!")
    while board_height == None:
        input_height = input("Enter the game board height ("
            + str(BOARD_DIMENSION_MIN[goal_length]) + " - "
            + str(BOARD_DIMENSION_MAX[goal_length]) + "): ")
        if try_type.try_int(input_height):
            input_height = int(input_height)
            if (input_height < BOARD_DIMENSION_MIN[goal_length]
                    or input_height > BOARD_DIMENSION_MAX[goal_length]):
                print("Board width must be between "
                    + str(BOARD_DIMENSION_MIN[goal_length]) + " and "
                    + str(BOARD_DIMENSION_MAX[goal_length]) + "!")
            else:
                board_height = input_height
        else:
            print("Please enter an integer value!")
    return Board(goal_length, board_width, board_height)

if __name__ == '__main__':
    main()
