import re
from typing import List, Tuple

Point = Tuple[int,int]
Line = Tuple[Point,Point]

class Board:
    ignore_diagonals: bool
    width: int
    height: int
    layout: List[List[List[int]]]  # y, x, list-of-linenums

    def __init__(self, lines: List[Line], ignore_diagonals: bool):
        self.ignore_diagonals = ignore_diagonals
        self.width = max([max(line[0][0], line[1][0]) for line in lines]) + 1
        self.height = max([max(line[0][1], line[1][1]) for line in lines]) + 1

        self.layout = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append([])
            self.layout.append(row)

        for i, line in enumerate(lines):
            x1,y1 = line[0]
            x2,y2 = line[1]
            xmin = min(x1,x2)
            xmax = max(x1,x2)
            ymin = min(y1,y2)
            ymax = max(y1,y2)
            if x1==x2:
                # Vertical
                x = x1
                for y in range(ymin,ymax+1):
                    self.layout[y][x].append(i)
            elif y1==y2:
                # Horizontal
                y = y1
                for x in range(xmin,xmax+1):
                    self.layout[y][x].append(i)
            else:
                if not self.ignore_diagonals:
                    if x2>x1 and y2>y1 or x2<x1 and y2<y1:
                        # upleft -> downright
                        for j, y in enumerate(range(ymin, ymax+1)):
                            x = xmin+j
                            self.layout[y][x].append(i)
                    else:
                        # upright -> downleft
                        for j, y in enumerate(range(ymin, ymax+1)):
                            x = xmax-j
                            self.layout[y][x].append(i)


    def num_intersections(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if len(self.layout[y][x]) > 1:
                    count += 1

        return count


def part1(input: List[str]) -> str:
    lines=[]
    for entry in input:
        m = re.search('(\d+),(\d+) -> (\d+),(\d+)', entry)
        lines.append((((int(m.group(1)),int(m.group(2))),(int(m.group(3)),int(m.group(4))))))

    board = Board(lines, True)
    return board.num_intersections()


def part2(input: List[str]) -> str:
    lines=[]
    for entry in input:
        m = re.search('(\d+),(\d+) -> (\d+),(\d+)', entry)
        lines.append((((int(m.group(1)),int(m.group(2))),(int(m.group(3)),int(m.group(4))))))

    board = Board(lines, False)
    return board.num_intersections()


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n')

    print(f"Part 1: {part1(input.copy())}")
    print(f"Part 2: {part2(input.copy())}")
