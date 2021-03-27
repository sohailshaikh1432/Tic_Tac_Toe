import random


def draw_board(board):
    """
    This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0)
    :param board:
    :return:
    """
    print(' 7' + board[7] + ' | 8' + board[8] + ' | 9' + board[9])
    print('-------------')
    print(' 4' + board[4] + ' | 5' + board[5] + ' | 6' + board[6])
    print('-------------')
    print(' 1' + board[1] + ' | 2' + board[2] + ' | 3' + board[3])


def input_payer_letter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second
    :return:
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for index in range(1, 10):
        if is_space_free(board, index):
            return False
    return True


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for index in moves_list:
        if is_space_free(board, index):
            possible_moves.append(index)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for index in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, index):
            make_move(copy, computer_letter, index)
            if is_winner(copy, computer_letter):
                return index

    # Check if the player could win on their next move, and block them.
    for index in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, index):
            make_move(copy, player_letter, index)
            if is_winner(copy, player_letter):
                return index

    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def get_board_copy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupe_board = []
    for index in board:
        dupe_board.append(index)

    return dupe_board


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


while True:
    print('Welcome to Tic Tac Toe!')
    # Reset the board
    the_board = [' '] * 10
    player_letter, computer_letter = input_payer_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    game_is_playing = True
    while game_is_playing:
        if turn == 'player':
            # Player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)
            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)
            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
