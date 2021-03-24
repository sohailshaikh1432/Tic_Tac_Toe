import random


def draw_board(board):
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
            if isBoardFull(the_board):
                draw_board(the_board)
                print('The game is a tie!')
                break
            else:
                turn = 'computer'
    else:
        # Computer’s turn.
        move = getComputerMove(the_board, computerLetter)
        makeMove(the_board, computerLetter, move)
        if is_winner(the_board, computerLetter):
            draw_board(the_board)
            print('The computer has beaten you! You lose.')
            game_is_playing = False
        else:
            if isBoardFull(the_board):
                draw_board(the_board)
                print('The game is a tie!')
                break
            else:
                turn = 'player'
