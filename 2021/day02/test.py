from solution import part1, part2

test_input=\
"""forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()

def test_part1():
    test_result=150
    out = part1(test_input)
    print(out)
    assert(out == test_result)


def test_part2():
    test_result=900
    out = part2(test_input)
    print(out)
    assert(out == test_result)
