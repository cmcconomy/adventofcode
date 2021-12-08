import re
from typing import List, Tuple
from functools import lru_cache


# @lru_cache(maxsize=None)
def get_distance(positions: List[int], center: int, flat: bool = True) -> int:
    total_dist = 0
    for pos in positions:
        if flat:
            dist = abs(center - pos)
        else:
            dist=0
            for i in range(abs(pos-center)+1):
                dist += i
        # print(f'For {pos}->{center}, distance was {dist} (Flat? {flat})')
        total_dist += dist

    # print(f'For {center}, total distance was {total_dist} (Flat? {flat})')
    return total_dist


def part1(input: List[str], flat: bool = True) -> str:
    positions = list(map(int, input[0].split(',')))
    first_pos = round(sum(positions) / len(positions))

    best_pos = first_pos
    best_dist = get_distance(positions, first_pos, flat)
    if get_distance(positions, first_pos+1, flat) < best_dist:
        best_pos = first_pos+1
        best_dist = get_distance(positions, best_pos, flat)
        while get_distance(positions, best_pos+1, flat) < best_dist:
            best_pos = best_pos + 1
            best_dist = get_distance(positions, best_pos, flat)
    elif get_distance(positions, first_pos-1, flat) < best_dist:
        best_pos = first_pos-1
        best_dist = get_distance(positions, best_pos, flat)
        while get_distance(positions, best_pos-1, flat) < best_dist:
            best_pos = best_pos - 1
            best_dist = get_distance(positions, best_pos, flat)

    # print(f'Finally - got {best_dist} for pos {best_pos}')
    return best_dist

def part2(input: List[str]) -> str:
    return part1(input, False)


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n')

    print(f"Part 1: {part1(input.copy())}")
    print(f"Part 2: {part2(input.copy())}")
