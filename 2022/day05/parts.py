from enum import Enum, auto
from typing import List, Dict, Tuple, Set
import re

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def tuple_to_int(tup: Tuple[str,str,str]):
    return (int(tup[0]), int(tup[1]), int(tup[2]))

class Problem:
    crates: List[List[str]]
    instructions: List[Tuple[int,int,int]]
    pat = re.compile('move (\d+) from (\d+) to (\d+)')

    def __init__(self, lines: List[str]):
        for i, line in enumerate(lines):
            if line[1] == '1':
                end_of_crates = i;
                break

        self._load_crates(lines[0:end_of_crates])
        self._load_instructions(lines[end_of_crates+2:])

    def _load_crates(self, lines: List[str]):
        count = int((len(lines[0])+1)/4)
        self.crates = []
        for _ in range(count):
            self.crates.append([])
        
        for col in range(count):
            for row in range(len(lines)):
                char = lines[row][4*col+1]
                if char != ' ':
                    self.crates[col].append(char)

    def _load_instructions(self, lines: List[str]):
        self.instructions = [tuple_to_int(self.pat.search(line).groups()) for line in lines]

    def run(self, mode: int = 1):
        if mode == 1:
            for instruction in self.instructions:
                for _ in range(instruction[0]):
                    crate = self.crates[instruction[1]-1].pop(0)
                    self.crates[instruction[2]-1].insert(0, crate)
        elif mode == 2:
            for instruction in self.instructions:
                crates = self.crates[instruction[1]-1][0:instruction[0]]
                self.crates[instruction[1]-1] = self.crates[instruction[1]-1][instruction[0]:]
                self.crates[instruction[2]-1] = crates + self.crates[instruction[2]-1]

    def stack_top_report(self):
        report = ""
        for cratestack in self.crates:
            report += cratestack[0]

        return report




lines = test_input.split('\n')
p = Problem(lines)
p.run()
print(p.stack_top_report())

p = Problem(lines)
p.run(2)
print(p.stack_top_report())



with open('day05/input.txt', 'r') as f:
    final_input = f.read().split('\n')

lines = final_input
p = Problem(lines)
p.run()
print(p.stack_top_report())

lines = final_input
p = Problem(lines)
p.run(2)
print(p.stack_top_report())
