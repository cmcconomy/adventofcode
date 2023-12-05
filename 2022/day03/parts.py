from enum import Enum, auto
from typing import List, Dict, Tuple, Set

def priority(item: str) -> int:
    p = ord(item)
    if ord('a') <= p <= ord('z'):
        return p-96
    else:
        return p-64+26

class Backpack:
    pockets: Tuple[str, str]
    common_item: str

    def __init__(self, line: str):
        division = int(len(line)/2)
        self.pockets = line[0:division], line[division:]
        self.common_item = set(self.pockets[0]).intersection(set(self.pockets[1])).pop()

class ElfGroup:
    common_item: str

    def __init__(self, lines: List[str]):
        items_per_elf: List[Set] = list(map(set, lines))
        self.common_item = items_per_elf[0].intersection(items_per_elf[1]).intersection(items_per_elf[2]).pop()


test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


lines = test_input.split('\n')
s = sum([priority(Backpack(line).common_item) for 
    line in lines])
print(s)


with open('day03/input.txt', 'r') as f:
    final_input = f.read().split('\n')

lines = final_input
s = sum([priority(Backpack(line).common_item) for 
    line in lines])
print(f"Part 1: {s}")

common_items = []
for i in range(0, int(len(lines)/3)):
    common_items.append(ElfGroup(lines[3*i:3*i+3]).common_item)
print(f"Part 2: {sum(map(priority, common_items))}")


