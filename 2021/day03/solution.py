from typing import List, Tuple


def part1(input: str) -> str:
    input = [tuple(list(map(int, list(t)))) for t in input]

    num_digits = len(input[0])
    vals = [0]*num_digits
    for val in input:
        for i, digit in enumerate(val):
            vals[i] += digit

    for i in range(num_digits):
        vals[i] = vals[i] - len(input)/2

    gamma = 0
    epsilon = 0

    val = 2**(num_digits-1)
    for i in range(num_digits):
        if vals[i] >= 0:
            gamma += val
        else:
            epsilon += val
        val = val / 2

    return int(gamma * epsilon)


Bits = Tuple[int,int,int,int,int]
BitList = List[Bits]


def oxy_filter(bitlist:BitList, pos: int) -> BitList:
    bitcount = sum([b[pos] for b in bitlist])
    most_common = 1 if bitcount >= len(bitlist)/2 else 0

    return list(filter(lambda b: b[pos] == most_common, bitlist))


def co2_filter(bitlist:BitList, pos: int) -> BitList:
    bitcount = sum([b[pos] for b in bitlist])
    least_common = 0 if bitcount >= len(bitlist)/2 else 1

    return list(filter(lambda b: b[pos] == least_common, bitlist))


def to_decimal(bits: Bits) -> int:
    num_digits = len(bits)
    decimal = 0

    val = 2**(num_digits-1)
    for i in range(num_digits):
        if bits[i] == 1:
            decimal += val
        val = val / 2

    return decimal


def part2(input: str) -> str:
    input = [tuple(list(map(int, list(t)))) for t in input]

    num_digits = len(input[0])
    oxy_list = input.copy()
    co2_list = input.copy()
    for i in range(num_digits):
        if len(oxy_list) > 1:
            oxy_list = oxy_filter(oxy_list, i)
        if len(co2_list) > 1:
            co2_list = co2_filter(co2_list, i)

        if len(oxy_list) == len(co2_list) == 1:
            break

    if not(len(oxy_list) == len(co2_list) == 1):
        raise Exception('Should have exactly one of oxy and co2..')

    oxy = to_decimal(oxy_list[0])
    co2 = to_decimal(co2_list[0])

    return int(oxy*co2)


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n')

    print(part1(input))
    print(part2(input))
