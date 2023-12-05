from enum import Enum, auto
from typing import List, Dict, Tuple, Set
import re

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

lines = test_input.split('\n')

class AssignmentPair:
    input: str
    elf1: Set[int]
    elf2: Set[int]

    def __init__(self, line):
        self.input=line
        line1a, line1b, line2a, line2b = re.split('[,-]', line)
        self.elf1 = set(range(int(line1a), int(line1b)+1))
        self.elf2 = set(range(int(line2a), int(line2b)+1))

    def one_contains_other(self) -> bool:
        return self.elf1.issubset(self.elf2) or self.elf2.issubset(self.elf1)

    def overlaps(self) -> bool:
        return bool(self.elf1.intersection(self.elf2))

print('test')
print(sum([AssignmentPair(line).one_contains_other() for line in lines]))
print(sum([AssignmentPair(line).overlaps() for line in lines]))
        
ap = AssignmentPair(lines[0])

with open('day04/input.txt', 'r') as f:
    final_input = f.read().split('\n')

lines = final_input
print('real')
print(sum([AssignmentPair(line).one_contains_other() for line in lines]))
print(sum([AssignmentPair(line).overlaps() for line in lines]))

