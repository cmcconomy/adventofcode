from .solution import part1, part2

test_input=\
"""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()

def test_part1():
    test_result=198
    out = part1(test_input)
    print(out)
    assert(out == test_result)


def test_part2():
    test_result=230
    out = part2(test_input)
    print(out)
    assert(out == test_result)
