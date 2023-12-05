import re
from copy import copy
from typing import List, Tuple, Dict, Set
from itertools import chain, groupby, permutations, product


# m = re.search('.*', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),


class Cave:
    grid: List[List[str]]  # [y][x]
    distance_to_start: List[List[str]]  # [y][x]
    path: List[Tuple[int, int]]  # (x,y)
    visited_nodes: Set[Tuple[int, int]]
    peekahead: int
    peek_list: List[Tuple]

    def __init__(self, lines: List[str], peekahead=2):
        self.grid = [list(line) for line in lines]
        self.path = [(0, 0)]
        self.visited_nodes = set((0,0))
        self.distance_to_start = []
        for _ in range(len(lines)):
            self.distance_to_start.append([None for _ in range(len(lines[0]))])

    def travel(self, currnode=None):
        if currnode == None:
            currnode = (0,0)

        x = currnode[0]
        y = currnode[1]
        accum_cost = self.distance_to_start[y][x]

        cheapest_travel=accum_cost+10  # more than any one move could cost.
        cheapest_node=None
        if x > 0:
            x2, y2 = x-1, y
            cost = self.grid[y2][x2]
            if (x2, y2) not in self.visited_nodes and cost < cheapest_travel:
                cheapest_travel = cost
                cheapest_node = (x2, y2)
        if x < len(self.grid[0])-1:
            x2, y2 = x+1, y
            cost = self.grid[y2][x2]
            if (x2, y2) not in self.visited_nodes and cost < cheapest_travel:
                cheapest_travel = cost
                cheapest_node = (x2, y2)
        if y > 0:
            x2, y2 = x, y-1
            cost = self.grid[y2][x2]
            if (x2, y2) not in self.visited_nodes and cost < cheapest_travel:
                cheapest_travel = cost
                cheapest_node = (x2, y2)
        if y < len(self.grid)-1:
            x2, y2 = x, y+1
            cost = self.grid[y2][x2]
            if (x2, y2) not in self.visited_nodes and cost < cheapest_travel:
                cheapest_travel = cost
                cheapest_node = (x2, y2)






        cheapest_path = 9*self.peekahead+1

        possible_paths = product("LRUD", repeat=self.peekahead)
        for j in range(self.peekahead):
            this_path=0
            for i in range(self.peekahead):





def part1(input: List[str]) -> str:
    return None


def part2(input: List[str]) -> str:
    return None

test_input=\
"""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()

# PyCharm is a little weird with "test"s in the same file as the code..
def te_st_part1():
    test_result=1588
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=2188189693529
    out = part2(test_input)
    print(f'Test Part 2: {out}')
    assert(out == test_result)


if __name__ == '__main__':
    do_part1 = True
    do_part2 = True

    with open('input.txt') as f:
        input = f.read().split('\n')

    if do_part1:
        te_st_part1()
        print(f"* Part 1: {part1(input.copy())}")
        print()

    if do_part2:
        te_st_part2()
        print(f"* Part 2: {part2(input.copy())}")

