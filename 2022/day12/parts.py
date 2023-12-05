from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Tuple, Set, Any
import re

test_input="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

DEBUG = False

Pos = Tuple[int,int]

class Mountainscape:
    grid: List[List[int]]
    start: Pos
    end: Pos
    visited = List[Pos]
    best_path = List[Pos]

    def __init__(self, lines: List[str]):
        self.grid = []
        for row, line in enumerate(lines):
            contents = [ord(char)-ord('a') for char in line]
            try:
                col = contents.index(-14)
                self.start = (col, row)
                contents[col] = 0
            except ValueError:
                pass
            try:
                col = contents.index(-28)
                self.end = (col, row)
                contents[col] = 26
            except ValueError:
                pass
            self.grid.append(contents)

        self.visited = [self.start]
        self.best_path = [self.start]
        pos = self.start
        while pos != self.end:
            pos = self.journey(pos)
            
    def journey(self, pos: Pos) -> Pos:
        print(f'moving from {pos}')
        col = x = pos[0]
        row = y = pos[1]
        highest_allowed = self.grid[row][col] + 1

        north = (x,y-1)
        if y > 0 and \
            north not in self.visited and \
            self.grid[row-1][col] <= highest_allowed:
                print(f'North!')
                self.visited.append(north)
                self.best_path.append(north)
                return north

        south = (x,y+1)
        if y < len(self.grid)-1 and \
            south not in self.visited and \
            self.grid[row+1][col] <= highest_allowed:
                print(f'South!')
                self.visited.append(south)
                self.best_path.append(south)
                return south

        east = (x+1,y)
        if x < len(self.grid[0])-1 and \
            east not in self.visited and \
            self.grid[row][col+1] <= highest_allowed:
                print(f'East!')
                self.visited.append(east)
                self.best_path.append(east)
                return east

        west = (x-1,y)
        if x > 0 and \
            west not in self.visited and \
            self.grid[row][col-1] <= highest_allowed:
                print(f'West!')
                self.visited.append(west)
                self.best_path.append(west)
                return west

        # If we get this far we are out of legal solutions. Back up.
        print(f'Going back.')
        return self.best_path.pop()







def solve(lines: List[str]):
    if DEBUG:
        print(lines)

    ms = Mountainscape(lines)
    print(f"Part 1: {len(ms.best_path)}")

    

    pass

print("TEST")
solve(test_input.split('\n'))



# with open('day12/input.txt', 'r') as f:
#     final_input = f.read()

# print("REAL")
# solve(final_input.split('\n'))