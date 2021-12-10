import re
from typing import List, Tuple, Dict

# m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),

def syntax_score(line):
    symbols = []
    for i, c in enumerate(line):
        if c in '{[(<':
            symbols.append(c)
        elif c == ')':
            last_symbol = symbols.pop()
            if last_symbol != '(':
                return 3
        elif c == ']':
            last_symbol = symbols.pop()
            if last_symbol != '[':
                return 57
        elif c == '}':
            last_symbol = symbols.pop()
            if last_symbol != '{':
                return 1197
        elif c == '>':
            last_symbol = symbols.pop()
            if last_symbol != '<':
                return 25137
        else:
            raise Exception('huh?')
    return 0

def get_closing(open_bracket):
    if open_bracket == '{':
        return '}'
    elif open_bracket == '(':
        return ')'
    elif open_bracket == '<':
        return '>'
    elif open_bracket == '[':
        return ']'


def get_correction_score(added_brackets):
    score = 0
    for b in added_brackets:
        if b == ')':
            bs = 1
        elif b == ']':
            bs = 2
        elif b == '}':
            bs = 3
        elif b == '>':
            bs = 4
        score = score*5 + bs

    return score

def correct_line(line):
    symbols = []
    # Clear out extra brackets
    for i, c in enumerate(line):
        if c in '{[(<':
            symbols.append(c)
        elif c in '>)]}':
            symbols.pop()
        else:
            raise Exception('huh?')

    symbols.reverse()
    complement = list(map(get_closing, symbols))
    return get_correction_score(complement)


def part1(input: List[str]) -> str:
    lines = [list(i) for i in input]

    return sum(list(map(syntax_score, lines)))

def part2(input: List[str]) -> str:
    lines = [list(i) for i in input]

    syntax_scoremap = [(syntax_score(line), line) for line in lines]
    incomplete_lines = [l[1] for l in list(filter(lambda item:item[0]==0, syntax_scoremap))]
    scores = sorted(list(map(correct_line, incomplete_lines)))
    return scores[int(len(scores)/2)]

test_input=\
"""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()


# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=26397
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=288957
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

