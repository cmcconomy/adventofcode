from enum import Enum, auto
from typing import List, Dict, Tuple

class Move(int, Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Strategy(str, Enum):
    WIN = "Z"
    TIE = "Y"
    LOSE = "X"

def lose_against(move: Move) -> Move:
    if move == Move.ROCK:
        return Move.SCISSORS
    elif move == Move.PAPER:
        return Move.ROCK
    elif move == Move.SCISSORS:
        return Move.PAPER

def win_against(move: Move) -> Move:
    if move == Move.ROCK:
        return Move.PAPER
    elif move == Move.PAPER:
        return Move.SCISSORS
    elif move == Move.SCISSORS:
        return Move.ROCK

class BotMode(Enum):
    MAP = auto()
    OUTCOME = auto()

class RpsGame:
    move_map: Dict[str,Move]
    score: int
    mode: BotMode

    def __init__(self, movelist: List[str], mode: BotMode):
        self.move_map = {
            "A": Move.ROCK,
            "B": Move.PAPER,
            "C": Move.SCISSORS,
            "X": Move.ROCK,
            "Y": Move.PAPER,
            "Z": Move.SCISSORS,
        }
        self.score = 0
        self.movelist = movelist
        self.mode = mode

    def get_moves(self, moveline) -> Tuple[Move, Move]:
        enemy_move = self.move_map.get(moveline[0])
        if self.mode == BotMode.MAP:
            return (enemy_move, self.move_map.get(moveline[2]))
        elif self.mode == BotMode.OUTCOME:
            strategy = Strategy(moveline[2])
            if strategy == Strategy.WIN:
                return (enemy_move, win_against(enemy_move))
            if strategy == Strategy.TIE:
                return (enemy_move, enemy_move)
            if strategy == Strategy.LOSE:
                return (enemy_move, lose_against(enemy_move))

    def play(self):
        enemy_move, self_move = self.get_moves(self.movelist.pop(0))
        diff = (enemy_move.value - self_move.value) % 3
        if self_move == Move.ROCK:
            self.score += 1
        elif self_move == Move.PAPER:
            self.score += 2
        elif self_move == Move.SCISSORS:
            self.score += 3

        if diff == 2:
            self.score = self.score + 6
            # print(f"{enemy_move.name} vs {self_move.name}: Win")
        elif diff == 1:
            # print(f"{enemy_move.name} vs {self_move.name}: Loss")
            pass
        else:
            self.score = self.score + 3
            # print(f"{enemy_move.name} vs {self_move.name}: Tie")

    def play_all(self):
        while self.movelist:
            self.play()
        # print(f"-- Final Score: {self.score}")


test_input = """A Y
B X
C Z"""

RpsGame(test_input.split("\n"), BotMode.MAP).play_all()
RpsGame(test_input.split("\n"), BotMode.OUTCOME).play_all()

with open('input.txt', 'r') as f:
    final_input = f.read().split('\n')

game1 = RpsGame(final_input, BotMode.MAP)
game1.play_all()
print(f"Part 1: {game1.score}")

game2 = RpsGame(final_input, BotMode.OUTCOME)
game2.play_all()
print(f"Part 2: {game2.score}")
