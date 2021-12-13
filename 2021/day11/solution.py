import re
from typing import List, Tuple, Dict
from itertools import chain, groupby

# m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),


class Octopus:
    total_flashes:int = 0
    p:int = 0
    is_flashing:bool = False
    in_turn:bool = False
    def __init__(self, powerlevel: int):
        self.p = powerlevel

    def increase_powerlevel(self):
        self.p += 1
        if self.p == 10:
            self.is_flashing = True

        return self.is_flashing

    def start_turn(self) -> bool:
        self.in_turn = True
        return self.increase_powerlevel()

    def acknowledge_flash(self):
        self.total_flashes += 1
        self.is_flashing = False

    def end_turn(self):
        if self.p > 9:
            self.p = 0
        self.in_turn = False

    def __str__(self):
        if self.is_flashing:
            return f'({self.p})'
        else:
            return f' {self.p} '


class Ocean:
    grid: List[List[Octopus]]

    def __init__(self, initstrs: List[str]):
        self.grid = []
        for row in initstrs:
            self.grid.append([Octopus(int(p)) for p in row])

    def run_turn(self):
        new_flash = False
        for y, row in enumerate(self.grid):
            for x, octo in enumerate(row):
                old_p = octo.p
                new_flash = octo.start_turn() or new_flash

        while new_flash:
            new_flash = False
            for y, row in enumerate(self.grid):
                for x, octo in enumerate(row):
                    if octo.is_flashing:
                        new_flash = self.process_flash(x,y) or new_flash

        for y, row in enumerate(self.grid):
            for x, octo in enumerate(row):
                octo.end_turn()

    def process_flash(self, x: int, y:int) -> bool:
        new_flash = False

        self.grid[y][x].acknowledge_flash()
        left_edge   = x == 0
        right_edge  = x == len(self.grid[0])-1
        top_edge    = y == 0
        bottom_edge = y == len(self.grid)-1
        if not left_edge:
            new_flash = self.grid[y][x-1].increase_powerlevel() or new_flash

            if not top_edge:
                new_flash = self.grid[y-1][x-1].increase_powerlevel() or new_flash
            if not bottom_edge:
                new_flash = self.grid[y+1][x-1].increase_powerlevel() or new_flash
        if not right_edge:
            new_flash = self.grid[y][x+1].increase_powerlevel() or new_flash

            if not top_edge:
                new_flash = self.grid[y-1][x+1].increase_powerlevel() or new_flash
            if not bottom_edge:
                new_flash = self.grid[y+1][x+1].increase_powerlevel() or new_flash

        if not top_edge:
            new_flash = self.grid[y-1][x].increase_powerlevel() or new_flash
        if not bottom_edge:
            new_flash = self.grid[y+1][x].increase_powerlevel() or new_flash

        return new_flash

    def get_total_flashes(self) -> int:
        return sum([octo.total_flashes for octo in chain.from_iterable(self.grid)])

    def all_flashed(self):
        flat_list = [octo.p for octo in chain.from_iterable(self.grid)]
        return flat_list.count(0) == len(flat_list)

    def __str__(self):
        sg = ""
        for row in self.grid:
            sg += str([str(octo) for octo in row]) + "\n"

        return sg

def part1(input: List[str]) -> str:
    ocean = Ocean(input)
    for _ in range(100):
        ocean.run_turn()

    return ocean.get_total_flashes()

def part2(input: List[str]) -> str:
    ocean = Ocean(input)

    run_count = 0
    while not ocean.all_flashed():
        run_count += 1
        ocean.run_turn()

    return run_count

test_input=\
"""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()

# test_input = ["19", "11"]

# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=1656
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=195
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

