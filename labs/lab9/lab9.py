"""
Name: Dylan McTigue
lab9.py

"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    return str(board[position - 1]).isnumeric()


def fill_spot(board, position, character):
    character = character.rstrip()
    character = character.lstrip()
    character = character.lower()

    board[position - 1] = str(character)


def horizontal_win_o(board, row):
    return board[row] == 'o' and board[row + 1] == 'o' and board[row + 2] == 'o'


def horizontal_win_x(board, row):
    return board[row] == 'x' and board[row + 1] == 'x' and board[row + 2] == 'x'


def vertical_win_o(board, column):
    return board[column] == 'o' and board[column + 3] == 'o' and board[column + 6] == 'o'


def vertical_win_x(board, column):
    return board[column] == 'x' and board[column + 3] == 'x' and board[column + 6] == 'x'


def diagonal_win_o_one(board, diagonal):
    return board[diagonal] == 'o' and board[diagonal + 4] == 'o' and board[diagonal + 8] == 'o'


def diagonal_win_o_two(board, diagonal):
    return board[diagonal] == 'o' and board[diagonal + 2] == 'o' and board[diagonal + 4] == 'o'


def diagonal_win_x_one(board, diagonal):
    return board[diagonal] == 'x' and board[diagonal + 4] == 'x' and board[diagonal + 8] == 'x'


def diagonal_win_x_two(board, diagonal):
    return board[diagonal] == 'x' and board[diagonal + 2] == 'x' and board[diagonal + 4] == 'x'


def x_wins(board):
    return horizontal_win_x(board, 0) or horizontal_win_x(board, 3) or horizontal_win_x(board, 6) \
            or vertical_win_x(board, 0) or vertical_win_x(board, 1) or vertical_win_x(board, 2) \
            or diagonal_win_x_one(board, 0) or diagonal_win_x_two(board, 2)


def o_wins(board):
    return horizontal_win_o(board, 0) or horizontal_win_o(board, 3) or horizontal_win_o(board, 6) \
            or vertical_win_o(board, 0) or vertical_win_o(board, 1) or vertical_win_o(board, 2) \
            or diagonal_win_o_one(board, 0) or diagonal_win_o_two(board, 2)


def game_is_won(board):
    if horizontal_win_x(board, 0) or horizontal_win_x(board, 3) or horizontal_win_x(board, 6) \
            or vertical_win_x(board, 0) or vertical_win_x(board, 1) or vertical_win_x(board, 2) \
            or diagonal_win_x_one(board, 0) or diagonal_win_x_two(board, 2):
        return True
    elif horizontal_win_o(board, 0) or horizontal_win_o(board, 3) or horizontal_win_o(board, 6) \
            or vertical_win_o(board, 0) or vertical_win_o(board, 1) or vertical_win_o(board, 2) \
            or diagonal_win_o_one(board, 0) or diagonal_win_o_two(board, 2):
        return True
    else:
        return False


def is_board_filled(board):
    return (not str(board[0]).isnumeric()) and (not str(board[1]).isnumeric()) and (not str(board[2]).isnumeric()) and \
            (not str(board[3]).isnumeric()) and (not str(board[4]).isnumeric()) and (not str(board[5]).isnumeric()) \
            and (not str(board[6]).isnumeric()) and (not str(board[7]).isnumeric()) and (not str(board[8]).isnumeric())


def game_over(board):
    return game_is_won(board) or is_board_filled(board)


def get_winner(board):
    if x_wins(board):
        return 'x'
    if o_wins(board):
        return 'o'
    else:
        return None


def play(board):
    print("Hello! Welcome to TikTacToe.")
    print("To play, take turns entering an 'x' or an 'o' by entering a number corresponding to the squares.")

    playing = True
    current_game = True
    count = 0

    while playing:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while current_game:
            print_board(board)

            if (count % 2) == 0:
                character = 'x'
            else:
                character = 'o'
            count = count + 1

            position = eval(input("{}'s, choose a position: ".format(character)))

            if is_legal(board, position):
                fill_spot(board, position, character)
            else:
                while not is_legal(board, position):
                    position = eval(input("{}'s, choose a position: ".format(character)))
                fill_spot(board, position, character)

            if game_over(board):
                print_board(board)
                break

        winner = get_winner(board)

        if winner == None:
            print("Tie")
        else:
            print("{}'s win!".format(winner))

        again = input('play again?')
        if again[0] == 'y' or again[0] == 'Y':
            count = 0
            playing = True
        else:
            playing = False


def main():
    play(build_board())


if __name__ == '__main__':
    main()
