import string
import random

numbers = string.digits

empty = ['#', \
         ' ', ' ', ' ', \
         ' ', ' ', ' ', \
         ' ', ' ', ' ']


def display_board(moves):
    filler = "   |   |   "
    top = f" {moves[7]} | {moves[8]} | {moves[9]} "
    middle = f" {moves[4]} | {moves[5]} | {moves[6]} "
    bottom = f" {moves[1]} | {moves[2]} | {moves[3]} "
    lines = "___ ___ ___"
    board_list = [filler, top, filler, lines, filler, middle, filler, lines, filler, bottom, filler]

    for line in board_list:
        print(line)


welcome_string = ("Welcome to Tic-Tac-Toe!\n"
                  "created by Kyle Murray for the intro to Python course.")


def place_move(num, moves, player):
    moves[num] = player
    return moves


def check_win(moves):
    verify = ' '
    check = [[moves[1], moves[2], moves[3]],\
    [moves[1], moves[4], moves[7]],\
    [moves[1], moves[5], moves[9]],\
    [moves[4], moves[5], moves[6]],\
    [moves[7], moves[8], moves[9]],\
    [moves[7], moves[5], moves[3]],\
    [moves[8], moves[5], moves[2]],\
    [moves[9], moves[6], moves[3]]]
    i = 0
    while verify == ' ' and i < len(check):
        verify = check_set(check[i])
        i += 1
    return verify

def check_set(check):
    new_set = set(check)
    if len(new_set) == 1 and check[0] != ' ':
        return check[0]
    return ' '

def invalid_move(message):
    return "Invalid move: " + message

def clear_screen():
    print("\n" * 100)

def start_game(moves):
    print(welcome_string)
    input("Press 'Enter' or 'Return' to continue...")
    players = {"player1": 'X', "player2": 'O'}
    alt = random.randint(0,1)
    error = ""
    while True:
        print("\n" * 100)
        current_player = "player1" if alt % 2 else "player2"
        display_board(moves)
        selection = input(f"\n{error}\n\nPlease choose a location (1 - 9) on the board to place your piece: ")
        error = ""
        if selection.lower() == 'exit':
            break
        elif selection in numbers and not selection == '0':
            if moves[int(selection)] == ' ':
                moves = place_move(int(selection), moves, players[current_player])
                alt += 1
            else:
                error = invalid_move("board position is already occupied")
        win = check_win(moves)
        if win == 'X' or win == 'O':
            clear_screen()
            print(f"{current_player} wins!")
            display_board(moves)
            break
        elif not ' ' in moves:
            clear_screen()
            print("Cat's game!!!!")
            display_board(moves)
            break

start_game(empty)
