from termcolor import colored
from argparse import ArgumentParser

from typing import Tuple
from custom_types import Game_Field

from helpers import clear_leaderboard, is_player_new, print_leaderboard, update_leaderboard

parser = ArgumentParser()

parser.add_argument('-p', '--play', action='store_true', required=False)
parser.add_argument('-l', '--leaderboard', action='store_true', required=False)
parser.add_argument('-c', '--clear', action='store_true', required=False)

cmd_args = parser.parse_args()

first_player = 'X'
second_player = 'O'

game_field: Game_Field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# first player is first to make a move
current_player = first_player

def input_move() -> Tuple[int, int]:
    ALLOWED_COORDINATES = (1, 2, 3)

    while True:
        next_move = input(f'Enter your next move, {current_player_name} as {current_player}(row column): ')
        placement = next_move.split(' ')

        if len(placement) != 2:
            print('Invalid input. Please enter two numbers separated by a space.')
            continue

        if any(not p.isdigit() for p in placement):
            print('Invalid input. Please enter valid numerical values.')
            continue

        if any(int(p) not in ALLOWED_COORDINATES for p in placement):
            print('Invalid input. Please enter values within the range of 1 to 3.')
            continue

        row, column = map(lambda p: int(p) -1, placement)

        if game_field[row][column] != ' ':
            print('This cell is already occupied. Please choose an empty cell.')
            continue

        return (row, column)
    

def check_winner():
    for row in game_field:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    for col in zip(*game_field):
        if all(cell == col[0] and cell != ' ' for cell in col):
            return col[0]
            
    for player in 'XO':
        if all(game_field[row][row] == player for row in range(len(game_field))):
            return player
    
        if all(game_field[0 + row][(len(game_field) - 1) - row] == player for row in range(len(game_field))):
            return player

    if all(' ' not in row for row in game_field):
        return 'D'

    return None


def print_field():
    print('\n')
    print('-' * 9)

    for row in game_field:
        result = [col if col != ' ' else '_' for col in row]

        print(f'| {' '.join(result)} |')

    print('-' * 9)
    print('\n')


def congratulate_player(winner: str, name: str):
    print(colored(f'Congrats, {name}, you have won! 🥳🥳', 'magenta')) if winner in 'XO' else print(colored('It\'s a draw!', 'cyan'))


def clear_game_field():
    global game_field
    game_field = [[" ", " ", " "] for _ in game_field]


if cmd_args.play:
    names = input('Enter names of two players separated by a slash(/): ').title().split('/')
    if len(names) != 2:
        raise ValueError('Only 2 names allowed!')
    
    for name in names:
        print(f'Hi, {name}! Good luck!\n') if is_player_new(name) else print(f'Hi, {name}! Nice to see you again.\n')

    name_1, name_2 = names

    while True:
        current_player_name = name_1 if current_player == 'X' else name_2

        row, column = input_move()
        game_field[row][column] = current_player

        print_field()

        winner = check_winner()

        if winner is not None:
            winner_name = name_1 if winner == 'X' else name_2 if winner == 'O' else 'D'
            congratulate_player(winner, winner_name)

            update_leaderboard(names, winner_name)

            user_choice = input('Would you like to play another round?: ').lower()
            if user_choice != 'yes' and user_choice != 'y':
                break

            clear_game_field()

        current_player = first_player if current_player == second_player else second_player
        current_player_name = name_1 if current_player_name == name_2 else name_2
elif cmd_args.leaderboard:
    print_leaderboard()
elif cmd_args.clear:
    clear_leaderboard()
    print(colored('Leaderboard cleared.', 'green'))
else:
    print(colored('Invalid command!', 'light_red'))
    exit(1)