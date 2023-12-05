from enum import Enum, auto
from typing import List, Dict, Tuple, Set
import re

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class File:
    name: str
    size: int

    def __init__(self, name: str, size: int, depth: int):
        self.name = name
        self.size = size
        self.depth = depth

    def __str__(self):
        return (" " * 2 * self.depth) + f"{self.size} {self.name}"

class Folder:
    parent: Dict = None# Folder
    name: str
    files: List[File]
    folders: Dict
    depth: int
    calc_size: int

    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.name = name
        self.files = []
        self.folders = {}
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.calc_size = 0

    def __str__(self):
        s = ""
        if self.parent == None:
            s += f"/ ({self.calc_size})\n"
        for fd in self.folders:
            s += (" " * 2 * self.depth) + f"Dir: {fd} ({self.folders.get(fd).calc_size})\n"
            s += f"{self.folders.get(fd)}\n"
        for f in self.files:
            s += f"{f}\n"
        return s


class FileSystem:
    root: Folder
    cwd: Folder
    flat_folder_list: List[Folder]

    def __init__(self, lines):
        self.root = Folder('/')
        self.cwd = self.root
        self.flat_folder_list = []

        nextline = self.process(lines, 0)
        while nextline:
            nextline = self.process(lines, nextline)
        calc_folder_sizes(self.root)

    def process(self, lines, pos: int) -> int:
        cmd = lines[pos].split(' ')
        if cmd[0] != '$':
            raise Exception('Not a command - ' + lines[pos])

        if cmd[1] == 'cd':
            path = cmd[2]
            if path == '/':
                self.cwd = self.root
            elif path == '..':
                self.cwd = self.cwd.parent
            else:
                if path not in self.cwd.folders:
                    folder = Folder(path, self.cwd)
                    self.cwd.folders[path] = folder
                    self.flat_folder_list.append(folder)
                self.cwd = self.cwd.folders[path]
            return pos + 1
        elif cmd[1] == 'ls':
            pos = pos + 1
            while True:
                if pos == len(lines):
                    return None  # out of input
                tokens = lines[pos].split(' ')
                if tokens[0] == '$':
                    return pos
                elif tokens[0] == 'dir':
                    path = tokens[1]
                    if path not in self.cwd.folders:
                        folder = Folder(path, self.cwd)
                        self.cwd.folders[path] = folder
                        self.flat_folder_list.append(folder)
                else:
                    self.cwd.files.append(File(tokens[1], int(tokens[0]), self.cwd.depth))
                pos = pos + 1

    def get_max_folder_sizes(self, max_size: int) -> List[Folder]:
        folders = filter(lambda f: f.calc_size <= max_size, self.flat_folder_list)
        return list(folders)

    def get_min_folder_sizes(self, min_size: int) -> List[Folder]:
        folders = filter(lambda f: f.calc_size >= min_size, self.flat_folder_list)
        return list(folders)


def calc_folder_sizes(folder: Folder):
    filesizes = sum([f.size for f in folder.files])
    folder.calc_size += filesizes
    parent = folder.parent
    while parent is not None:
        parent.calc_size += filesizes
        parent = parent.parent

    for fd in folder.folders:
        calc_folder_sizes(folder.folders.get(fd))

def solve(lines: List[str]):
    fs = FileSystem(lines)
    valid_folders = fs.get_max_folder_sizes(100000)
    print(f"  Part 1: {sum([vf.calc_size for vf in valid_folders])}")

    total_size = 70000000
    root_usage = fs.root.calc_size
    remaining = total_size - root_usage
    required = 30000000
    needed = required - remaining
    # print(f"Needed: {needed}")
    valid_folders = sorted(fs.get_min_folder_sizes(needed), key=lambda fd:fd.calc_size)

    print(f"  Part 2: {valid_folders[0].calc_size}")



print("TEST")
solve(test_input.split('\n'))

with open('day07/input.txt', 'r') as f:
    final_input = f.read()

print("REAL")
solve(final_input.split('\n'))
