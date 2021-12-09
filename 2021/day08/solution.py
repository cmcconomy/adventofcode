import re
from typing import List, Tuple, Dict

# Unique num segments: 1(2), 7(3), 4(4), 8(7)
unscrambled_digits = [
    'abcefg',   # 0: 6
    'cf',       # 1: 2
    'acdeg',    # 2: 5
    'acdfg',    # 3: 5
    'bcdf',     # 4: 4
    'abdfg',    # 5: 5
    'abdefg',   # 6: 6
    'acf',      # 7: 3
    'abcdefg',  # 8: 7
    'abcdfg'    # 9: 6
]

class FourDigits:
    reference: List[str]
    digits: List[str]
    segments: Dict[set,int]

    def __init__(self, line):
        # print(f'.. {line}')
        m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
        self.reference = [
            "".join(sorted(list(m.group(1)))),
            "".join(sorted(list(m.group(2)))),
            "".join(sorted(list(m.group(3)))),
            "".join(sorted(list(m.group(4)))),
            "".join(sorted(list(m.group(5)))),
            "".join(sorted(list(m.group(6)))),
            "".join(sorted(list(m.group(7)))),
            "".join(sorted(list(m.group(8)))),
            "".join(sorted(list(m.group(9)))),
            "".join(sorted(list(m.group(10))))
        ]
        self.digits = [
            "".join(sorted(list(m.group(11)))),
            "".join(sorted(list(m.group(12)))),
            "".join(sorted(list(m.group(13)))),
            "".join(sorted(list(m.group(14))))
        ]
        self.segments = {}

        self.parse_references()

    def parse_references(self):
        ref_lens = list(map(len, self.reference))
        ref_sets = list(map(set, self.reference))

        digits = {
            'one' : ref_sets[ref_lens.index(2)],
            'seven': ref_sets[ref_lens.index(3)],
            'four': ref_sets[ref_lens.index(4)],
            'eight': ref_sets[ref_lens.index(7)],
        }

        bars = {}

        parts = {
            'full_right_line': digits['one']
        }

        bars['top'] = list(digits['seven'].difference(parts['full_right_line']))[0]
        parts['upper_l'] = digits['four'].difference(parts['full_right_line'])  # "L" at the top left of the four.
        parts['lower_l'] = digits['eight'].difference(digits['four'].union(bars['top']))  # "L" at the bottom left of the eight.

        # Zero hunt...
        # one of the two "upper L" characters represents the center bar. Let's find which.
        l_items = list(parts['upper_l'])

        maybe_zero = digits['eight'].difference(l_items[0])
        if maybe_zero in ref_sets:
            bars['center'] = l_items[0]
            bars['topleft'] = l_items[1]
        else:
            bars['center'] = l_items[1]
            bars['topleft'] = l_items[0]

        digits['zero'] = digits['eight'].difference(bars['center'])

        # Two hunt... the only char with bottom-right!
        segment_counts = {'a':0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for d in ref_sets:
            for letter in list('abcdefg'):
                if letter in d:
                    segment_counts[letter] += 1

        for letter in list('abcdefg'):
            if segment_counts[letter] == 4:
                bars['bottomleft'] = letter
            if segment_counts[letter] == 9:
                bars['bottomright'] = letter

        for d in ref_sets:
            if not bars['bottomright'] in d:
                digits['two'] = d
                break

        bars['topright'] = list(digits['one'].difference(bars['bottomright']))[0]
        bars['bottom'] = list(digits['two']
                              .difference(bars['top'])
                              .difference(bars['topright'])
                              .difference(bars['center'])
                              .difference(bars['bottomleft']))[0]

        digits['three'] = set([bars['top'],bars['topright'],bars['center'],bars['bottomright'],bars['bottom']])
        digits['five'] = set([bars['top'],bars['topleft'],bars['center'],bars['bottomright'],bars['bottom']])
        digits['six'] = set([bars['top'],bars['topleft'],bars['center'],bars['bottomright'],bars['bottom'],bars['bottomleft']])
        digits['nine'] = set([bars['top'],bars['topleft'],bars['topright'],bars['center'],bars['bottomright'],bars['bottom']])

        self.segments["".join(sorted(list(digits['zero'])))] = 0
        self.segments["".join(sorted(list(digits['one'])))] = 1
        self.segments["".join(sorted(list(digits['two'])))] = 2
        self.segments["".join(sorted(list(digits['three'])))] = 3
        self.segments["".join(sorted(list(digits['four'])))] = 4
        self.segments["".join(sorted(list(digits['five'])))] = 5
        self.segments["".join(sorted(list(digits['six'])))] = 6
        self.segments["".join(sorted(list(digits['seven'])))] = 7
        self.segments["".join(sorted(list(digits['eight'])))] = 8
        self.segments["".join(sorted(list(digits['nine'])))] = 9

    def value(self):
        val =  1000 * self.segments[self.digits[0]] + \
                100 * self.segments[self.digits[1]] + \
                 10 * self.segments[self.digits[2]] + \
                  1 * self.segments[self.digits[3]]
        # print(val)
        return val

    def unique_digits(self):
        num=0
        for i in range(4):
            if len(self.digits[i]) != 5 and len(self.digits[i]) != 6:
                num += 1

        return num


def part1(input: List[str]) -> str:
    print(f'Processing {len(input)} lines..')

    fourdigs = [FourDigits(line) for line in input]
    unique_digits = sum([fd.unique_digits() for fd in fourdigs])
    return unique_digits

def part2(input: List[str]) -> str:
    fourdigs = [FourDigits(line) for line in input]
    value = sum([fd.value() for fd in fourdigs])
    return value

test_input=\
"""acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf""".splitlines()

test_input=\
"""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()

# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=26
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=61229
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

