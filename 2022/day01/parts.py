from typing import List

class Elf:
    calories: List[int]

    def __init__(self, calories: List[int]):
        self.calories = calories

    def __str__(self):
        return f"Elf with {sum(self.calories)} calories in {len(self.calories)} items."

    @property
    def total_calories(self):
        return sum(self.calories)



def read_input(input) -> List[Elf]:
    elves = []
    lines = input.split("\n")
    calories = []
    for line in lines:
        if line:
            calories.append(int(line))
        else:
            new_elf = Elf(calories)
            elves.append(new_elf)
            calories = []
    
    if calories:
        elves.append(Elf(calories))

    return elves

test_input = \
"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        real_input = f.read()
    elves = read_input(real_input)
    total_cals = sorted([e.total_calories for e in elves], reverse=True)
    print(f'Part 1: {total_cals[0]}')
    print(f'Part 2: {sum(total_cals[0:3])}')
