import re
from copy import copy
from typing import List, Tuple, Dict
from itertools import chain, groupby

# m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),

class Point:
    x: int
    y: int

    def __init__(self, x, y, fold_instructions):
        self.x = int(x)
        self.y = int(y)

        for fi in fold_instructions:
            self.fold(fi)
        # map(self.fold, fold_instructions)

    def fold(self, fold_instruction: Tuple[str, int]):
        dir = fold_instruction[0]
        crease = int(fold_instruction[1])

        if dir == 'x':
            diff = self.x - crease
            if diff > 0:
                self.x -= 2*diff
        elif dir == 'y':
            diff = self.y - crease
            if diff > 0:
                self.y -= 2*diff


    def coords(self):
        return self.x, self.y


class Origami:

    grid: List[Point]

    def __init__(self, input, first_fold_only = True):
        fold_instructions = []

        coords = []
        end_of_coords = False
        for line in input:
            if len(line) == 0:
                end_of_coords = True
                continue

            if end_of_coords:
                m = re.search('fold along (\w)=(\d+)', line)
                fold_instructions.append((m.group(1), m.group(2)))

                if m.group(1) == 'x':
                    self.x_fold = int(m.group(2))
                elif m.group(1) == 'y':
                    self.y_fold = int(m.group(2))
            else:
                m = re.search('(\d+),(\d+)', line)
                coords.append((m.group(1), m.group(2)))

        if first_fold_only:
            self.grid = [Point(x, y, fold_instructions[0:1]) for x, y in coords]
        else:
            self.grid = [Point(x, y, fold_instructions) for x, y in coords]

    def __str__(self):
        tuples = [p.coords() for p in self.grid]
        # sorted_tuples = sorted(sorted(tuples, key=lambda t:t[0]), key=lambda t:t[1])

        xs = [t[0] for t in tuples]
        ys = [t[1] for t in tuples]

        board = ""
        for y in range(min(ys), max(ys)+1):
            for x in range(min(xs), max(xs) + 1):
                if (x,y) in tuples:
                    board += "#"
                else:
                    board += "."
            board += "\n"

        return board


def part1(input: List[str]) -> str:
    origami = Origami(input)
    return len(set(p.coords() for p in origami.grid))


def part2(input: List[str]) -> str:
    origami = Origami(input, False)
    print(origami)
    return len(set(p.coords() for p in origami.grid))

test_input=\
"""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()

# test_input = ["19", "11"]

# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=17
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=16
    out = part2(test_input)
    print(f'Test Part 2: {out}')
    assert(out == test_result)


if __name__ == '__main__':
    te_st_part1()
    with open('input.txt') as f:
        input = f.read().split('\n')

    print(f"* Part 1: {part1(input.copy())}")

    te_st_part2()
    print(f"* Part 2: {part2(input.copy())}")

