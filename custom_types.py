from typing import Literal, TypedDict


class Statistics(TypedDict):
  w: int
  l: int
  d: int

type Leaderboard = dict[str, Statistics]

type Game_Field = list[list[Literal['X', 'O', ' ']]]