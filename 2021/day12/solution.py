import re
from copy import copy
from typing import List, Tuple, Dict
from itertools import chain, groupby

# m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),


class CaveSystem:
    Path = Tuple[List[str], bool]

    path_segs: Dict[str, List[str]]
    paths: List[Path]
    allowed_extra_visit: bool

    def __init__(self, paths_in, allowed_extra_visit=False):
        self.allowed_extra_visit = allowed_extra_visit
        self.path_segs = {}
        for path in paths_in:
            m = re.search('(\w+)-(\w+)', path)
            a = m.group(1)
            b = m.group(2)

            dests = self.path_segs.get(a, [])
            dests.append(b)
            self.path_segs[a] = dests

            dests = self.path_segs.get(b, [])
            dests.append(a)
            self.path_segs[b] = dests

        self.paths = self.travel()


    def travel(self, paths_so_far: List[Path] = None) -> List[Path]:
        if paths_so_far is None:
            paths_so_far = [(['start'], False)]

        went_further = False
        extended_paths = []
        for path, used_extra_visit in paths_so_far:
            last_visited = path[-1]
            if last_visited == 'end':
                extended_paths.append((path, used_extra_visit))
                continue

            for next_cave in self.path_segs[last_visited]:
                used_extra_visit_this_time = used_extra_visit
                if next_cave == 'start':
                    continue
                if next_cave.islower() and next_cave in path:
                    if not self.allowed_extra_visit or used_extra_visit:
                        continue  # can't visit a lowercase cave twice!
                    else:
                        used_extra_visit_this_time = True

                went_further = True
                extended_path = copy(path)
                extended_path.append(next_cave)
                extended_paths.append((extended_path, used_extra_visit_this_time))

        if went_further:
            return self.travel(extended_paths)
        else:
            return extended_paths


def part1(input: List[str]) -> str:
    caves = CaveSystem(input)
    return len(caves.paths)


def part2(input: List[str]) -> str:
    caves = CaveSystem(input, True)
    return len(caves.paths)

test_input=\
"""start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

# test_input = ["19", "11"]

# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=10
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=36
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

