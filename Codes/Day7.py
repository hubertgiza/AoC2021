import numpy as np

from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input7.txt", "r") as f:
    data = f.readlines()
data = list(map(int, data[0].split(',')))


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one(puzzle: list):
    puzzle.sort()
    # median
    if len(puzzle) % 2 == 1:
        optimal_place = puzzle[(len(puzzle) + 1) // 2]
    else:
        optimal_place = (puzzle[(len(puzzle) - 1) // 2] + puzzle[(len(puzzle) - 1) // 2 + 1]) // 2

    differences = [abs(element - optimal_place) for element in puzzle]
    print(sum(differences))


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two(puzzle):
    max_x = max(puzzle)
    fuels_spent = np.zeros(shape=(len(puzzle), max_x + 1), dtype='int32')

    def cost(i, j):
        delta = abs(i - j)
        res = delta * (delta + 1) // 2
        return res

    for i in range(len(puzzle)):
        for j in range(puzzle[i] - 1, -1, -1):
            fuels_spent[i][j] += cost(puzzle[i], j)
        for j in range(puzzle[i] + 1, max_x + 1):
            fuels_spent[i][j] += cost(puzzle[i], j)
    print(np.min(np.apply_over_axes(np.sum, fuels_spent, 0)))
