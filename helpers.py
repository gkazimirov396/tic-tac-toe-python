from json import dumps, loads

from typing import Literal
from custom_types import Leaderboard

def get_key_to_update(winner: str, player: str) -> Literal['w', 'd', 'l']:
  return 'w' if winner == player else 'd' if winner == 'D' else 'l'

def parse_leaderboard() -> Leaderboard:
  with open('./src/data/leaderboard.json') as file:
    return loads(file.read())
  

def clear_leaderboard():
  with open('./src/data/leaderboard.json', 'w') as file:
    file.write(dumps({}))
  

def is_player_new(name: str):
  leaderboard = parse_leaderboard()
  
  return all(player != name for player in leaderboard.keys())


def update_leaderboard(names: list[str], winner: str):
  leaderboard = parse_leaderboard()

  for name in names:
    if is_player_new(name):
      leaderboard[name] = { 'w': 0, 'l': 0, 'd': 0 }

    leaderboard[name][get_key_to_update(winner, name)] += 1

  with open('./src/data/leaderboard.json', 'w') as file:
    file.write(dumps(leaderboard, indent=2))


def print_leaderboard():
  leaderboard = parse_leaderboard()
  ids = range(1, len(leaderboard.keys()) + 1)

  print('\n')
  print(f'{'player':>10} {'w':>20} {'d':>8} {'l':>8}\n')
  print('-' * 50 + '\n')
    
  for (name, stats), id in zip(sorted(leaderboard.items(), key=lambda player: player[1]['w'], reverse=True), ids):
    print(f'{f'{id}.':<4} {name:<24} {stats['w']:<8} {stats['d']:<8} {stats['l']:<8}\n')

  print('\n')