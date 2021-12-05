from typing import List, Tuple

def get_draws(topline: str) -> List[int]:
    return list(map(int, topline.split(",")))

class Card:
    nums: List[List[int]]
    picked: List[List[int]]

    def __init__(self, textblock: str):
        self.picked = []
        self.nums = []
        for i in range(5):
            self.nums.append(list(map(int, textblock[i].split())))
            self.picked.append([False]*5)


    def call_number(self, called_num: int):
        found_num = False
        for i, row in enumerate(self.nums):
            try:
                pos = row.index(called_num)
                found_num = True
                self.picked[i][pos] = True
                break
            except:
                pass

        return found_num

    def vertchecks(self):
        for i in range(len(self.picked)):
            all_true = True
            for j in range(len(self.picked[i])):
                if not all_true:
                    break
                if not self.picked[i][j]:
                    all_true = False
            if all_true:
                break

        return all_true

    def horizchecks(self):
        for i in range(len(self.picked)):
            all_true = True
            for j in range(len(self.picked[i])):
                if not all_true:
                    break
                if not self.picked[j][i]:
                    all_true = False
            if all_true:
                break

        return all_true

    def bingocheck(self):
        return self.horizchecks() or self.vertchecks()

    def unpicked_sum(self) -> int:
        upsum = 0
        for i in range(len(self.picked)):
            for j in range(len(self.picked[i])):
                if not self.picked[j][i]:
                    upsum += self.nums[j][i]

        return upsum

    def __str__(self):
        out=""
        for i in range(len(self.picked)):
            for j in range(len(self.picked[i])):
                num=self.nums[i][j]
                if self.picked[i][j]:
                    out = f'{out}({num}) '
                else:
                    out = f'{out} {num}  '
            out += '\n'

        return out


def get_cards(rawrows: List[str]) -> List[Card]:
    cards = []
    num_cards = int(len(rawrows)/6)
    for i in range(num_cards):
        card = Card(rawrows[6*i+1 : 6*(i+1)])
        cards.append(card)

    return cards


def get_answer(draw: int, card: Card) -> int:
    unselected_count = card.unpicked_sum()
    return draw * unselected_count


def part1(input: List[str]) -> str:
    draws = get_draws(input.pop(0))
    cards = get_cards(input)

    found_winner = False
    while not found_winner and len(draws)>0:
        draw = draws.pop(0)
        for card in cards:
            had_number = card.call_number(draw)

            if had_number and card.bingocheck():
                answer = get_answer(draw, card)
                return answer

    return None




def part2(input: str) -> str:
    draws = get_draws(input.pop(0))
    cards = get_cards(input)

    found_winner = False
    while not found_winner and len(draws)>0:
        draw = draws.pop(0)
        for card in cards.copy():
            had_number = card.call_number(draw)

            if had_number and card.bingocheck():
                cards.remove(card)
                if len(cards) == 0:
                    answer = get_answer(draw, card)
                    return answer

    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n')

    print("Part 1: {part1(input.copy())}")
    print("Part 2: {part2(input.copy())}")
