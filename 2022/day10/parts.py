from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Tuple, Set, Any
import re

test_input = """noop
addx 3
addx -5"""

test_input2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

DEBUG = False


class Cpu:
    x: int
    hist: List[int]
    cycle: int

    def __init__(self, lines: List[str]):
        self.x = 1
        self.hist = []

        for line in lines:
            self.run(line)

    def run(self, line:str):
        cmds = line.split(' ')
        if cmds[0] == 'noop':
            self.hist.append(self.x)
        elif cmds[0] == 'addx':
            # print(cmds)
            self.hist.append(self.x)
            self.hist.append(self.x)
            self.x = self.x + int(cmds[1])
        else:
            raise NotImplementedError(f"Don't know command {cmds[0]}")

    def signalsum(self, cycles: List[int]) -> int:
        return sum([cycle*self.hist[cycle-1] for cycle in cycles])

    def draw(self) -> str:
        screen = ""
        for row in range(6):
            for col in range(40):
                idx = row*40 + col
                x = self.hist[idx]
                # print(f"{col+1=} {col=} {idx=} {x=}")
                if x-1 <= col <= x+1:  # row+1 because of offset...
                    # print(f"{idx+1}>>> {col+1=} {col=} {idx=} {x=}")
                    screen = screen + '#'
                else:
                    # print(f"{idx+1}. {col+1=} {col=} {idx=} {x=}")
                    screen = screen + '.'
            screen = screen + "\n"
        
        return screen






def solve(lines: List[str]):
    if DEBUG:
        print(lines)

    cpu = Cpu(lines)
    # print(cpu.hist)
    print(f"Part 1: {cpu.signalsum([20,60,100,140,180,220])}")
    print("Part 2:")
    print(cpu.draw())
    # print(f"Part 1: {grid.unique_tail_visits()}")

    # grid2 = Grid(lines, 10)
    # print(f"Part 2: {grid2.unique_tail_visits()}")
    # print(grid2.ropes[0])
    # print(posmap(grid2.visited))
    pass

# print("TEST")
# solve(test_input.split('\n'))

print("TEST2")
solve(test_input2.split('\n'))



with open('day10/input.txt', 'r') as f:
    final_input = f.read()

print("REAL")
solve(final_input.split('\n'))