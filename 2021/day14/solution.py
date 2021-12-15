import re
from copy import copy
from typing import List, Tuple, Dict
from itertools import chain, groupby

# m = re.search('.*', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),

def increment_key(dct, key, amt=1):
    count = dct.get(key, 0)
    count += amt
    dct[key] = count

class PairPolymerizer:
    template: str
    pairs: Dict[str, int]
    rules: Dict[str, str]


    def __init__(self, lines: List[str]):
        self.pairs = {}
        self.template = lines.pop(0)

        for i in range(len(self.template)-1):
            pair = self.template[i:i+2]
            increment_key(self.pairs, pair)

        lines.pop(0)
        self.rules = {}
        for line in lines:
            self.rules[line[0:2]] = line[-1]

    def polymerize(self):
        new_pairs = {}

        for pair, count in self.pairs.items():
            new_left_pair = pair[0] + self.rules[pair]
            new_right_pair = self.rules[pair] + pair[1]
            increment_key(new_pairs, new_left_pair, count)
            increment_key(new_pairs, new_right_pair, count)

        self.pairs = new_pairs

    def score(self):
        char_counts = {}
        for pair, count in self.pairs.items():
            # All chars are double-counted except the ones on the very front/back..
            increment_key(char_counts, pair[0], count/2)
            increment_key(char_counts, pair[1], count/2)

        # add back on the count for front/back..
        increment_key(char_counts, self.template[0], .5)
        increment_key(char_counts, self.template[-1], .5)

        counts = sorted(char_counts.values())
        return int(counts[-1] - counts[0])


class Polymerizer:
    """
    This was my naive approach.. worked fine for 10 iterations but completely exploded when I tried to do 40!
    I have to admit I looked at the subreddit and caught a clue on producing new pairs to count/keep track of instead of the whole string.
    """
    template: str
    polymers: List[str]
    rules: List[Tuple[str, str]]

    def __init__(self, lines: List[str]):
        self.template = lines.pop(0)
        self.polymers = [self.template]
        lines.pop(0)
        self.rules = [(line[0:2], line[-1]) for line in lines]

    def polymerize(self):
        last_polymer = self.polymers[-1]
        insertions = []
        for rule in self.rules:
            pos = last_polymer.find(rule[0])
            while pos >= 0:
                insertions.append((pos+1, rule[1]))
                pos = last_polymer.find(rule[0], pos+1)

        new_polymer = last_polymer
        for insertion in sorted(insertions, key=lambda r:r[0], reverse=True):
            new_polymer = new_polymer[0:insertion[0]] + insertion[1] + new_polymer[insertion[0]:]

        self.polymers.append(new_polymer)
        return new_polymer

    def score(self):
        last_polymer = self.polymers[-1]
        counts=[]
        for char in set(list(last_polymer)):
            counts.append(last_polymer.count(char))

        counts = sorted(counts)
        return counts[-1] - counts[0]


def part1(input: List[str]) -> str:

    p = PairPolymerizer(input)
    for _ in range(10):
        p.polymerize()

    return p.score()


def part2(input: List[str]) -> str:

    p = PairPolymerizer(input)
    for _ in range(40):
        p.polymerize()

    return p.score()

test_input=\
"""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()

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

