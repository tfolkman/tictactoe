from random import shuffle
from typing import Tuple

board = {'7': '7', '8': '8', '9': '9', '4': '4', '5': '5', '6': '6', '1': '1', '2': '2', '3': '3'}
all_positions = list(board.keys())


class BColors:
    """
    Class to add colors when printing out the Board
    """
    ENDC = '\033[0m'
    RED = '\033[31m'
    BLUE = '\033[34m'


def color_print(value: str) -> str:
    """
    Given a string value, adds the appropriate color
    :param value: The string value you want to add color to
    :return: String value with colors added
    """
    if value == "X":
        return f"{BColors.RED}{value}{BColors.ENDC}"
    if value == "O":
        return f"{BColors.BLUE}{value}{BColors.ENDC}"
    else:
        return value


def print_board(game_board: dict) -> None:
    """
    Prints the Tic Tac Toe board
    :param game_board: The board to print in dict form
    :return: None
    """
    print(color_print(game_board['7']) + '|' + color_print(game_board['8']) + '|' + color_print(game_board['9']))
    print('-+-+-')
    print(color_print(game_board['4']) + '|' + color_print(game_board['5']) + '|' + color_print(game_board['6']))
    print('-+-+-')
    print(color_print(game_board['1']) + '|' + color_print(game_board['2']) + '|' + color_print(game_board['3']))
    print("----------")


def move(shape: str, position: str, board: dict) -> Tuple[dict, str]:
    """
    Moves the given shape to the appropriate position on the given board
    :param shape: 
    :param position: 
    :param board: 
    :return: The updated board and the shape that needs to move next
    """
    board[position] = shape
    if shape == "X":
        next_shape = "O"
    elif shape == "O":
        next_shape = "X"
    return board, next_shape


def check_valid_move(position: str, board: dict) -> bool:
    """
    Checks if a move is valid
    :param position: Position you want to move to
    :param board: The board state
    :return: Bool if valid
    """
    if position not in all_positions:
        return False
    elif board[position] in ["X", "O"]:
        return False
    else:
        return True


def check_if_person_won(board: dict) -> Tuple[bool, str]:
    """
    Check if someone has won
    :param board: 
    :return: Bool if won, shape that won if won else None
    """
    for shape in ["O", "X"]:
        if (board['1'] == shape and board['4'] == shape and board['7'] == shape) or \
                (board['2'] == shape and board['5'] == shape and board['8'] == shape) or \
                (board['3'] == shape and board['6'] == shape and board['9'] == shape) or \
                (board['9'] == shape and board['5'] == shape and board['1'] == shape) or \
                (board['7'] == shape and board['5'] == shape and board['3'] == shape) or \
                (board['6'] == shape and board['5'] == shape and board['4'] == shape) or \
                (board['7'] == shape and board['8'] == shape and board['9'] == shape) or \
                (board['1'] == shape and board['2'] == shape and board['3'] == shape):
            return True, shape
    return False, None


def check_if_tie(board: dict) -> bool:
    """
    Check if the game is a tie
    :param board: 
    :return: Bool if tie
    """
    sum_valid_moves = 0
    for position in all_positions:
        is_valid = check_valid_move(position, board)
        sum_valid_moves += is_valid
    if sum_valid_moves == 0:
        return True
    else:
        return False


def check_win_next_move(shape: str, opponent_shape: str, board: dict) -> Tuple[bool, str]:
    """
    Checks if the shape can win on next move
    :param shape: The shape making a move
    :param opponent_shape: The opponent shape
    :param board: Current board
    :return: Bool if shape can win on next move, and the move to make to win
    """
    if board['1'] == shape and board['4'] == shape and board['7'] != opponent_shape:
        return True, '7'
    elif board['4'] == shape and board['7'] == shape and board['1'] != opponent_shape:
        return True, '1'
    elif board['1'] == shape and board['7'] == shape and board['4'] != opponent_shape:
        return True, '4'
    elif board['8'] == shape and board['5'] == shape and board['2'] != opponent_shape:
        return True, '2'
    elif board['8'] == shape and board['2'] == shape and board['5'] != opponent_shape:
        return True, '5'
    elif board['2'] == shape and board['5'] == shape and board['8'] != opponent_shape:
        return True, '8'
    elif board['9'] == shape and board['6'] == shape and board['3'] != opponent_shape:
        return True, '3'
    elif board['3'] == shape and board['6'] == shape and board['9'] != opponent_shape:
        return True, '9'
    elif board['9'] == shape and board['3'] == shape and board['6'] != opponent_shape:
        return True, '6'
    elif board['7'] == shape and board['8'] == shape and board['9'] != opponent_shape:
        return True, '9'
    elif board['9'] == shape and board['8'] == shape and board['7'] != opponent_shape:
        return True, '7'
    elif board['9'] == shape and board['7'] == shape and board['8'] != opponent_shape:
        return True, '8'
    elif board['4'] == shape and board['5'] == shape and board['6'] != opponent_shape:
        return True, '6'
    elif board['6'] == shape and board['5'] == shape and board['4'] != opponent_shape:
        return True, '4'
    elif board['4'] == shape and board['6'] == shape and board['5'] != opponent_shape:
        return True, '5'
    elif board['1'] == shape and board['2'] == shape and board['3'] != opponent_shape:
        return True, '3'
    elif board['3'] == shape and board['2'] == shape and board['1'] != opponent_shape:
        return True, '1'
    elif board['3'] == shape and board['1'] == shape and board['2'] != opponent_shape:
        return True, '2'
    elif board['7'] == shape and board['5'] == shape and board['3'] != opponent_shape:
        return True, '3'
    elif board['3'] == shape and board['5'] == shape and board['7'] != opponent_shape:
        return True, '7'
    elif board['7'] == shape and board['3'] == shape and board['5'] != opponent_shape:
        return True, '5'
    elif board['1'] == shape and board['5'] == shape and board['9'] != opponent_shape:
        return True, '9'
    elif board['9'] == shape and board['5'] == shape and board['1'] != opponent_shape:
        return True, '1'
    elif board['9'] == shape and board['1'] == shape and board['5'] != opponent_shape:
        return True, '5'
    else:
        return False, None


def make_ai_move(shape: str, board: dict) -> Tuple[dict, str]:
    """
    Simple implementation of an "AI" to play against
    First, checks if can make a game winning move and if so makes that move
    If not, checks if can make a move to block opponent from winning, and then makes that move
    If not, moves to the middle spot if can
    Otherwise, randomly moves to an available position
    :param shape: The shape moving
    :param board: The current board
    :return: The updated board and the shape that needs to move next
    """
    if shape == "X":
        opponent_shape = "O"
    else:
        opponent_shape = "X"
    opp_can_win, opp_win_position = check_win_next_move(opponent_shape, shape, board)
    can_win, win_position = check_win_next_move(shape, opponent_shape, board)
    if can_win:
        return move(shape, win_position, board)
    elif opp_can_win:
        return move(shape, opp_win_position, board)
    elif check_valid_move('5', board):
        return move(shape, '5', board)
    else:
        shuffle(all_positions)
        for position_x in all_positions:
            if check_valid_move(position_x, board):
                return move(shape, position_x, board)


def check_game_state(board: dict) -> Tuple[bool, str]:
    """
    Checks if the game is over or there is a tie
    :param board: Current board
    :return: If game over, str explaining why game over
    """
    print_board(board)
    game_over, winning_shape = check_if_person_won(board)
    if game_over:
        return True, f"{winning_shape} won!!!!!!!"
    is_tie = check_if_tie(board)
    if is_tie and not game_over:
        return True, "It is a tie!!!!"
    return False, "Game not over"


def check_cheat_code(position: str) -> bool:
    """
    Cheat code position. If you enter the cheat code as your move, you automatically win
    :param position:
    :return: Bool if valid cheat code
    """
    if position == '544':
        return True
    else:
        return False


def print_cheater_won() -> None:
    """
    Prints out a board with all squares marked for the person who used the cheat code
    :return:
    """
    for pos_x in all_positions:
        board[pos_x] = shape
    print_board(board)
    print(f"{shape} won!!! :x")


if __name__ == '__main__':
    print("[1] or [2] Players?")
    n_players = input()
    print_board(board)
    # Set starting game state. X always starts.
    game_over = False
    shape = "X"
    while not game_over:
        print(f"Which position do you want to move to {shape}?")
        position = input()
        # Check if entered valid cheat and if so, they win and print out a board with all spaces for winning shape!
        cheat_valid = check_cheat_code(position)
        if cheat_valid:
            print_cheater_won()
            break
        is_valid = check_valid_move(position, board)
        # If not a valid move, keep asking for a new position until valid
        while not is_valid:
            print("Someone has already moved there or this isnt a valid move. Pick a different spot")
            position = input()
            cheat_valid = check_cheat_code(position)
            if cheat_valid:
                print_cheater_won()
                break
            is_valid = check_valid_move(position, board)
        board, shape = move(shape, position, board)
        game_over, status = check_game_state(board)
        if game_over:
            print(status)
        # If single player, have AI make a move
        if n_players == "1" and not game_over:
            board, shape = make_ai_move(shape, board)
            game_over, status = check_game_state(board)
            if game_over:
                print(status)
                if status == "O won!!!!!!!":
                    print("A robot beat you! :)")

