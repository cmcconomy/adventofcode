from day01 import part1, part2

test_input=\
"""199
200
208
210
200
207
240
269
260
263""".splitlines()

def test_part1():
    test_result1=7
    out = part1(test_input)
    print(out)
    assert(out == test_result1)


def test_part2():
    test_result2=5
    out = part2(test_input)
    print(out)
    assert(out == test_result2)

test_part1()
test_part2()
