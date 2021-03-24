import random


def drawBoard(board):
    """
    This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0)
    :param board:
    :return:
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


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
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def make_move(board, letter, move):
    board[move] = letter


# Reset the board
the_board = [' '] * 10
player_letter, computer_letter = input_payer_letter()
turn = who_goes_first()
print('The ' + turn + ' will go first.')
game_is_playing = True
while game_is_playing:
    if turn == 'player':
        # player's turn
        drawBoard(the_board)
        move = get_player_move(the_board)
        make_move(the_board, player_letter, move)
