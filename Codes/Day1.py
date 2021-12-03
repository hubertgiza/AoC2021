from Library import *

with open(PATH_TO_INPUTS + "/input1.txt", "r") as f:
    data = f.readlines()
data = [int("".join([chr(number) for number in list(filter(lambda x: 48 <= x <= 57, line))])) for line in data]


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one(puzzle):
    increased_depth = [puzzle[i] > puzzle[i - 1] for i in range(1, len(puzzle))]
    print(sum(increased_depth))


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two(puzzle):
    sum_three = lambda x, y: sum((y[x], y[x + 1], y[x + 2]))
    increased_three_window_depth = [sum_three(i, puzzle) > sum_three(i - 1, puzzle) for i in range(1, len(puzzle) - 2)]
    print(sum(increased_three_window_depth))


part_two(data)
