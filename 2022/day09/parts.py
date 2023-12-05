from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Tuple, Set, Any
import re

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

DEBUG = False



@dataclass(unsafe_hash=True)
class Pos:
    x: int = 0
    y: int = 0

def posmap(pos: Set[Pos]) -> str:
        xx = [p.x for p in list(pos)]
        yy = [p.y for p in list(pos)]
        xmin = min(xx)
        xmax = max(xx)
        ymin = min(yy)
        ymax = max(yy)

        s = ""
        for y in range(ymax+1, ymin-2, -1):
            for x in range(xmin-1, xmax+2):
                if Pos(x,y) in pos:
                    s += 'x'
                else:
                    s += '.'
            s += '\n'

        return s

@dataclass
class Rope:
    tag: int
    head: Pos
    tail: Pos
    parent: Any = None
    child: Any = None

    def __init__(self, tag: int):
        self.head = Pos()
        self.tail = Pos()
        self.tag = tag

    def adjust_tail(self):
        if self.parent is not None:
            if DEBUG:
                print(f"For rope {self.tag}, moved head from {self.head} to {self.parent.tail}.")
            self.head = self.parent.tail
            if DEBUG:
                print(f"\t now H:{self.head}, T:{self.tail}... Problem??")

        hx, hy = self.head.x, self.head.y
        tx, ty = self.tail.x, self.tail.y
        
        # Same column..
        if hy == ty and hx-tx == 2:
            tx = tx+1
        elif hy == ty and hx-tx == -2:
            tx = tx-1
        # Same Row..
        elif hx == tx and hy-ty == 2:
            ty = ty+1
        elif hx == tx and hy-ty == -2:
            ty = ty-1
        # Diagonal moves
        elif hx > tx and hy > ty:
            tx = tx+1
            ty = ty+1
        elif hx > tx and hy < ty:
            tx = tx+1
            ty = ty-1
        elif hx < tx and hy > ty:
            tx = tx-1
            ty = ty+1
        elif hx < tx and hy < ty:
            tx = tx-1
            ty = ty-1
        elif hy == ty and abs(hx-tx) < 2:
            pass
        elif hx == tx and abs(hy-ty) < 2:
            pass
        else:
            raise NotImplementedError(f"{hx,tx}, {hy,ty}")
            
        if DEBUG:# and self.child is None:
            print(f"  {self.tail} -> {Pos(tx,ty)}")
        self.tail = Pos(tx,ty)
        if self.child is None:
            return self.tail
        else:
            return self.child.adjust_tail()


    def move(self, dir: str, amt: int) -> Set[Pos]:
        positions = set()
        if DEBUG:
            print(f"{dir} {amt}")
        for _ in range(amt):
            if dir == 'R':
                self.head = Pos(self.head.x+1, self.head.y)
            elif dir == 'L':
                self.head = Pos(self.head.x-1, self.head.y)
            elif dir == 'U':
                self.head = Pos(self.head.x, self.head.y+1)
            elif dir == 'D':
                self.head = Pos(self.head.x, self.head.y-1)

            if DEBUG:
                print(f"Moved HEAD to {self.head}")
                print(self)
            tail_pos = self.adjust_tail()
            if DEBUG:
                print(self)

            positions.add(tail_pos)


        # if DEBUG:
        #     print(self)
        #     print("----------")
        #     knot = self
        #     while knot is not None:
        #         print(knot.tail)
        #         knot = knot.child
        #     print("----------")

        return positions

    def __str__(self):
        pos = set()
        knot = self
        while knot is not None:
            pos.add(knot.tail)
            knot = knot.child

        return posmap(pos)

@dataclass
class Grid:
    ropes: List[Rope]
    visited: Set[Pos]

    def __init__(self, lines: List[str], num_ropes: int = 1):
        self.ropes = []
        prev = None
        for i in range(num_ropes):
            rope = Rope(i)
            rope.parent = prev
            if prev is not None:
                prev.child = rope
            prev = rope
            self.ropes.append(rope)

        self.visited = set((Pos(),Pos())) # start at 0,0
        for line in lines:
            self.visited =  self.visited.union(self.move(line))

    def move(self, line: str) -> List[Tuple[Pos,Pos]]:
        dir, amt = line.split(' ')
        amt = int(amt)
        return self.ropes[0].move(dir, amt)

    def unique_tail_visits(self) -> int:
        # return '\n'.join(sorted(map(str,list(set([p[1] for p in self.visited])))))
        return len(list(self.visited))









def solve(lines: List[str]):
    if DEBUG:
        print(lines)
    grid = Grid(lines)
    if DEBUG:
        print(grid.visited)

    print(f"Part 1: {grid.unique_tail_visits()}")

    grid2 = Grid(lines, 10)
    print(f"Part 2: {grid2.unique_tail_visits()}")
    print(grid2.ropes[0])
    print(posmap(grid2.visited))
    pass

print("TEST")
solve(test_input.split('\n'))

print("TEST2")
solve(test_input_2.split('\n'))



with open('day09/input.txt', 'r') as f:
    final_input = f.read()

print("REAL")
# solve(final_input.split('\n'))
print("2359 too low")