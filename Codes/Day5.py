import numpy as np

from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input5.txt", "r") as f:
    data = f.readlines()
data = [list(map(int, element.replace('\n', '').replace(' -> ', ',').split(','))) for element in data]


class Map:
    def __init__(self, puzzle):
        self.data = puzzle
        self.size_y = max(max(puzzle, key=lambda x: max(x[0], x[2]))[::2]) + 1
        self.size_x = max(max(puzzle, key=lambda x: max(x[1], x[3]))[1::2]) + 1
        self.map = np.zeros(shape=(self.size_x, self.size_y), dtype='int16')

    def add_horizontal_line(self, coordinates):
        x1, y1, x2, y2 = coordinates

        delta_x = abs(x1 - x2)
        delta_y = abs(y1 - y2)

        min_x = min(x1, x2)
        min_y = min(y1, y2)

        if y1 == y2:
            for i in range(delta_x + 1):
                self.map[y1, min_x + i] += 1
        elif x1 == x2:
            for i in range(delta_y + 1):
                self.map[min_y + i, x1] += 1

    def add_line(self, coordinates):
        x1, y1, x2, y2 = coordinates

        delta_x = x2 - x1
        delta_y = y2 - y1

        if abs(delta_x) == abs(delta_y):
            if delta_y >= 0:
                if delta_x >= 0:
                    for i in range(abs(delta_x) + 1):
                        self.map[y1 + i, x1 + i] += 1
                else:
                    for i in range(abs(delta_x) + 1):
                        self.map[y1 + i, x1 - i] += 1
            else:
                if delta_x >= 0:
                    for i in range(abs(delta_x) + 1):
                        self.map[y1 - i, x1 + i] += 1
                else:
                    for i in range(abs(delta_x) + 1):
                        self.map[y1 - i, x1 - i] += 1
        else:
            self.add_horizontal_line(coordinates)

    def draw_full_horizontal_map(self):
        for coordinates in self.data:
            self.add_horizontal_line(coordinates)

    def draw_full_map(self):
        for coordinates in self.data:
            self.add_line(coordinates)

    def get_score(self):
        return np.where(self.map >= 2)[0].shape[0]


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one(puzzle):
    x = Map(puzzle)
    x.draw_full_horizontal_map()
    print(x.get_score())


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two(puzzle):
    x = Map(data)
    x.draw_full_map()
    print(x.get_score())
