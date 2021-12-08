from . import part1, part2

test_input=\
"""16,1,2,0,4,2,7,1,2,14""".splitlines()

def test_7part1():
    test_result = 37
    out = part1(test_input)
    print(out)
    assert(out == test_result)


def test_7part2():
    test_result=168
    out = part2(test_input)
    print(out)
    assert(out == test_result)

test_7part2()