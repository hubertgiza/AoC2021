import string
from itertools import combinations

import numpy as np

DEMO_PATH_1 = "../Inputs/demo_input8_1.txt"
DEMO_PATH_2 = "../Inputs/demo_input8_2.txt"
DEMO_PATH_3 = "../Inputs/demo_input8_3.txt"
DEMO_PATH_4 = "../Inputs/demo_input8_4.txt"
INPUT_PATH = "../Inputs/input8.txt"

digits = string.digits
letters = string.ascii_letters
characters = letters + digits


def part_one():
    with open(INPUT_PATH, "r") as f:
        data = np.array(list(map(list, f.read().split("\n"))))
        antinodes = np.zeros(data.shape)
        shape = np.array(data.shape)
        for char in characters:
            chars_idx = list(zip(*np.where(data == char)))
            all_pairs = list(combinations(chars_idx, 2))
            for (x1, y1), (x2, y2) in all_pairs:
                x_diff = x2 - x1
                y_diff = y2 - y1
                antinode_1 = (x1 - x_diff, y1 - y_diff)
                antinode_2 = (x2 + x_diff, y2 + y_diff)
                begin = np.array((0, 0))
                if all(begin <= antinode_1) and all(antinode_1 < shape):
                    antinodes[antinode_1] = 1
                if all(begin <= antinode_2) and all(antinode_2 < shape):
                    antinodes[antinode_2] = 1
        print(np.sum(antinodes))


def part_two():
    with open(INPUT_PATH, "r") as f:
        data = np.array(list(map(list, f.read().split("\n"))))
        antinodes = np.zeros(data.shape)
        shape = np.array(data.shape)
        for char in characters:
            chars_idx = list(zip(*np.where(data == char)))
            all_pairs = list(combinations(chars_idx, 2))
            for (x1, y1), (x2, y2) in all_pairs:
                x_diff = x2 - x1
                y_diff = y2 - y1
                antinodes[x1, y1] = 1
                antinodes[x2, y2] = 1
                p1 = np.array((x1, y1))
                p2 = np.array((x2, y2))
                diff = np.array((x_diff, y_diff))

                while in_bounds(p1 - diff, shape):
                    p1 = p1 - diff
                    antinodes[p1[0], p1[1]] = 1
                while in_bounds(p2 + diff, shape):
                    p2 = p2 + diff
                    antinodes[p2[0], p2[1]] = 1
        print(np.sum(antinodes))


def in_bounds(point, arr_shape):
    return all(np.array((0, 0)) <= point) and all(point < arr_shape)


if __name__ == '__main__':
    part_one()
    part_two()
