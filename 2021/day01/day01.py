

def part1(input: str) -> str:
    input = map(int, input)

    last=None
    increases=0
    for i in input:
        if last is not None and i > last:
            increases += 1
        last=i

    return increases


def part2(input: str) -> str:
    input = list(map(int, input))

    windows = []
    for i in range(len(input)-2):
        windows.append(input[i]+input[i+1]+input[i+2])

    return part1(windows)


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print(part1(input))
    print(part2(input))
