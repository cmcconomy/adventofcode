

def part1(input: str) -> str:
    input = [txt.split(' ') for txt in input]
    input = [(t[0], int(t[1])) for t in input]

    hor = 0
    depth = 0

    for command, amt in input:
        if command == 'forward':
            hor += amt
        elif command == 'up':
            depth -= amt
        elif command == 'down':
            depth += amt

    return hor*depth


def part2(input: str) -> str:
    input = [txt.split(' ') for txt in input]
    input = [(t[0], int(t[1])) for t in input]

    hor = 0
    depth = 0
    aim = 0

    for command, amt in input:
        if command == 'forward':
            hor += amt
            depth += aim * amt
        elif command == 'up':
            aim -= amt
        elif command == 'down':
            aim += amt

    return hor*depth


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print(part1(input))
    print(part2(input))
