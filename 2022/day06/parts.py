from enum import Enum, auto
from typing import List, Dict, Tuple, Set
import re

test_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

def parse_input(line: str, size: int = 4):
    for i in range(0,len(line)-size+1):
        if len(list(set(line[i:i+size]))) == size:
            print(line[i:i+size])
            return i+size

lines = test_input.split('\n')

print(parse_input(test_input))

with open('day06/input.txt', 'r') as f:
    final_input = f.read()

final_input
print(parse_input(final_input, 14))
