from enum import Enum, auto
from typing import List, Dict, Tuple, Set
import re

test_input = """30373
25512
65332
33549
35390"""

class Dir(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


class Forest:
    trees: List[List[int]]

    def __init__(self, lines):
        self.trees = []
        for line in lines:
            self.trees.append(list(map(int, list(line))))

    def visible_trees(self) -> int:
        visible_trees = 0
        for y in range(len(self.trees)):
            for x in range(len(self.trees[y])):
                if self.visible(x,y):
                    visible_trees = visible_trees + 1

        return visible_trees

    def visible(self, x: int, y: int) -> bool:
        if x == 0 or y == 0 or y == len(self.trees)-1 or x == len(self.trees[y])-1:
            return True

        # West View
        vis = True
        last_height = self.trees[y][x]
        for xx in range(x-1, -1, -1):
            if self.trees[y][xx] >= last_height:
                vis = False
                break
            else:
                last_height = max(last_height, self.trees[y][xx])
        if vis:
            return True

        # East View
        vis = True
        last_height = self.trees[y][x]
        for xx in range(x+1, len(self.trees[y])):
            if self.trees[y][xx] >= last_height:
                vis = False
                break
            else:
                last_height = max(last_height, self.trees[y][xx])
        if vis:
            return True
        
        # North View
        vis = True
        last_height = self.trees[y][x]
        for yy in range(y-1, -1, -1):
            if self.trees[yy][x] >= last_height:
                vis = False
                break
            else:
                last_height = max(last_height, self.trees[yy][x])
        if vis:
            return True

        # South View
        vis = True
        last_height = self.trees[y][x]
        for yy in range(y+1, len(self.trees)):
            if self.trees[yy][x] >= last_height:
                vis = False
                break
            else:
                last_height = max(last_height, self.trees[yy][x])
        if vis:
            return True

        return False
        
    def best_view_score(self) -> int:
        best_view_score = 0
        for y in range(len(self.trees)):
            for x in range(len(self.trees[y])):
                best_view_score = max(best_view_score, self.view_score(x,y))

        return best_view_score

    def view_score(self, x: int, y: int) -> bool:

        # West View
        west = 0
        last_height = self.trees[y][x]
        for xx in range(x-1, -1, -1):
            west += 1
            if self.trees[y][xx] >= last_height:
                break

        # East View
        east = 0
        last_height = self.trees[y][x]
        for xx in range(x+1, len(self.trees[y])):
            east += 1
            if self.trees[y][xx] >= last_height:
                break
        
        # North View
        north = 0
        last_height = self.trees[y][x]
        for yy in range(y-1, -1, -1):
            north += 1
            if self.trees[yy][x] >= last_height:
                break

        # South View
        south = 0
        last_height = self.trees[y][x]
        for yy in range(y+1, len(self.trees)):
            south += 1
            if self.trees[yy][x] >= last_height:
                break

        return west * east * north * south

def solve(lines: List[str]):
    f = Forest(lines)
    print(f"Part 1: {f.visible_trees()}")
    print(f"Part 2: {f.best_view_score()}")

print("TEST")
solve(test_input.split('\n'))

with open('day08/input.txt', 'r') as f:
    final_input = f.read()

print("REAL")
solve(final_input.split('\n'))
