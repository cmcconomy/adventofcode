import re
from typing import List, Tuple, Dict

# m = re.search('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)', line)
# self.reference = [
#     "".join(sorted(list(m.group(1)))),

class HeightMap:
    geo: List[List[int]]
    low_pts: List[Tuple[int,int]]
    basins: List[List[Tuple[int,int]]]

    def __init__(self, lines):
        self.geo = [list(map(int, list(line))) for line in lines]
        self.find_lowpts()
        self.find_basins()


    def find_lowpts(self):
        self.low_pts = []
        for y, row in enumerate(self.geo):
            for x, val in enumerate(row):
                low_pt = True
                if x > 0:
                    if row[x-1] <= val:
                        low_pt = False
                if x < len(row)-1:
                    if row[x+1] <= val:
                        low_pt = False
                if y > 0:
                    if self.geo[y-1][x] <= val:
                        low_pt = False
                if y < len(self.geo)-1:
                    if self.geo[y+1][x] <= val:
                        low_pt = False

                if low_pt:
                    pt = (x,y)
                    self.low_pts.append(pt)


    def low_points(self):
        return [self.geo[c[1]][c[0]] for c in self.low_pts]

    def risks(self):
        return [val+1 for val in self.low_points()]

    def _explore_basin(self, x, y, prev_val=None, basin_members=None, visited_pts=None):
        if basin_members is None:
            basin_members = set()
        if visited_pts is None:
            visited_pts = set()

        currval = self.geo[y][x]
        if prev_val is not None:
            # is it the end of the road!?
            if currval <= prev_val or currval == 9 or (x,y) in basin_members:
                visited_pts.add((x, y))
                return basin_members, visited_pts

        visited_pts.add((x,y))
        basin_members.add((x,y))
        if x > 0:
            new_basin_members, new_visited_pts = self._explore_basin(x-1, y, currval, basin_members, visited_pts)
            basin_members = basin_members.union(new_basin_members)
            visited_pts = visited_pts.union(new_visited_pts)
        if x < len(self.geo[0])-1:
            new_basin_members, new_visited_pts = self._explore_basin(x+1, y, currval, basin_members, visited_pts)
            basin_members = basin_members.union(new_basin_members)
            visited_pts = visited_pts.union(new_visited_pts)
        if y > 0:
            new_basin_members, new_visited_pts = self._explore_basin(x, y-1, currval, basin_members, visited_pts)
            basin_members = basin_members.union(new_basin_members)
            visited_pts = visited_pts.union(new_visited_pts)
        if y < len(self.geo)-1:
            new_basin_members, new_visited_pts = self._explore_basin(x, y+1, currval, basin_members, visited_pts)
            basin_members = basin_members.union(new_basin_members)
            visited_pts = visited_pts.union(new_visited_pts)

        return basin_members, visited_pts


    def find_basins(self):
        self.basins = []
        for x, y in self.low_pts:
            self.basins.append(self._explore_basin(x, y)[0])

    def basin_score(self):
        basin_sizes = sorted([len(b) for b in self.basins], reverse=True)
        return basin_sizes[0]*basin_sizes[1]*basin_sizes[2]





def part1(input: List[str]) -> str:
    hmap = HeightMap(input)
    return sum(hmap.risks())

def part2(input: List[str]) -> str:
    hmap = HeightMap(input)
    return hmap.basin_score()

test_input=\
"""2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()


# PyCharm is a little weird with tests in the same file as the code..
def te_st_part1():
    test_result=15
    out = part1(test_input)
    print(f'Test Part 1: {out}')
    assert(out == test_result)


def te_st_part2():
    test_result=1134
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

