import numpy as np

DEMO_PATH = "../Inputs/demo_input14.txt"
INPUT_PATH = "../Inputs/input14.txt"
EMPTY = 0
ROCK = 1
SAND = 2
SOURCE = 3
SOURCE_COORDINATES = (500, 0)


class SandUnit:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map

    def __repr__(self):
        return f"{self.x}, {self.y}"

    def fall_down(self):
        while True:
            possible_moves = [(self.x, self.y + 1), (self.x - 1, self.y + 1), (self.x + 1, self.y + 1)]
            in_map = [check_if_in_map(move, MAP.shape) for move in possible_moves]
            if sum(in_map) != len(possible_moves):
                return False
            if MAP[possible_moves[0]] == EMPTY:
                self.x, self.y = possible_moves[0]
            elif MAP[possible_moves[1]] == EMPTY:
                self.x, self.y = possible_moves[1]
            elif MAP[possible_moves[2]] == EMPTY:
                self.x, self.y = possible_moves[2]
            else:
                MAP[(self.x, self.y)] = SAND
                if (self.x, self.y) == SOURCE_COORDINATES:
                    return False
                return True


def check_if_in_map(coordinates, map_shape):
    if 0 < coordinates[0] < map_shape[0] and 0 < coordinates[1] < map_shape[1]:
        return True
    return False


def part_one(array):
    sand_units = 0
    while True:
        was_placed = SandUnit(*SOURCE_COORDINATES, array).fall_down()
        if was_placed:
            sand_units += 1
        else:
            print(sand_units)
            break


def part_two(array):
    sand_units = 0
    while True:
        was_placed = SandUnit(*SOURCE_COORDINATES, array).fall_down()
        if was_placed:
            sand_units += 1
        else:
            print(sand_units + 1)
            break


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [list(map(lambda x: (int(x[0]), int(x[1])), map(lambda x: x.split(","), element.split(" -> ")))) for
                element in data]
    max_y = max([element[1] for row in data for element in row])
    MAP = np.zeros(shape=(700, max_y + 3))
    MAP[:, max_y + 2] = ROCK
    for path in data:
        for i in range(1, len(path)):
            diff_x = path[i][0] - path[i - 1][0]
            diff_y = path[i][1] - path[i - 1][1]
            if abs(diff_y) > 0 and abs(diff_x) > 0:
                print("kupsko")
                break
            if abs(diff_y) > 0:
                if diff_y > 0:
                    for j in range(diff_y + 1):
                        x, y = path[i][0], path[i - 1][1] + j
                        MAP[path[i][0], path[i - 1][1] + j] = ROCK
                else:
                    for j in range(abs(diff_y) + 1):
                        MAP[path[i][0], path[i][1] + j] = ROCK
            else:
                if diff_x > 0:
                    for j in range(diff_x + 1):
                        MAP[path[i - 1][0] + j, path[i][1]] = ROCK
                else:
                    for j in range(abs(diff_x) + 1):
                        MAP[path[i][0] + j, path[i][1]] = ROCK
    MAP[SOURCE_COORDINATES] = SOURCE
    part_one(MAP)
    part_two(MAP)
