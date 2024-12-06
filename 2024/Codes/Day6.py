DEMO_PATH = "../Inputs/demo_input6.txt"
INPUT_PATH = "../Inputs/input6.txt"
import numpy as np


class Guard:
    directions = ["up", "right", "down", "left"]
    moves = {
        "up": (0, -1),
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0)
    }

    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.direction = 0

    def move_part_1(self, puzzle_map):
        puzzle_map[self.y][self.x] = "X"
        move_x, move_y = self.moves[self.directions[self.direction]]
        next_x, next_y = self.x + move_x, self.y + move_y
        if next_x > max_x or next_x < 0 or next_y > max_y or next_y < 0:
            return "END"
        if puzzle_map[next_y][next_x] == "#":
            self.direction = (self.direction + 1) % len(self.directions)
            return self.move_part_1(puzzle_map)
        self.x, self.y = next_x, next_y
        return

    def move_part_2(self, puzzle_map, visits):
        visits[self.y][self.x][self.direction] += 1
        if visits[self.y][self.x][self.direction] > 1:
            return "CYCLE"
        puzzle_map[self.y][self.x] = "X"
        move_x, move_y = self.moves[self.directions[self.direction]]
        next_x, next_y = self.x + move_x, self.y + move_y
        if next_x > max_x or next_x < 0 or next_y > max_y or next_y < 0:
            return "END"
        if puzzle_map[next_y][next_x] == "#":
            self.direction = (self.direction + 1) % len(self.directions)
            return self.move_part_1(puzzle_map)
        self.x, self.y = next_x, next_y
        return

    def simulate(self, puzzle_map, visits):
        move_result = self.move_part_2(puzzle_map, visits)
        while move_result is None:
            move_result = self.move_part_2(puzzle_map, visits)
        return move_result


def part_one():
    with open(DEMO_PATH, "r") as f:
        data = list(map(list, f.read().split("\n")))
        max_x = len(data[0]) - 1
        max_y = len(data) - 1
        start_x, start_y = -1, -1
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "^":
                    start_x, start_y = x, y
                    break
            if start_x != -1:
                break
        guard = Guard(start_x, start_y, max_x, max_y)
        while guard.move_part_1(data) != "END":
            continue
        res = [element.count("X") for element in data]
        print(sum(res))


def part_two():
    with open(INPUT_PATH, "r") as f:
        data = list(map(list, f.read().split("\n")))
        max_x = len(data[0]) - 1
        max_y = len(data) - 1
        start_x, start_y = -1, -1
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "^":
                    start_x, start_y = x, y
                    break
            if start_x != -1:
                break
        res = []
        counter = 0
        all_possibilities = (max_x + 1) * (max_y + 1)
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                print(f"{counter}/{all_possibilities}")
                if data[y][x] != "#":
                    guard = Guard(start_x, start_y, max_x, max_y)
                    curr_map = np.array(data)
                    curr_map[y][x] = "#"
                    visits = np.array([[[0] * 4 for i in range(max_y + 1)] for j in range(max_x + 1)])
                    move_result = guard.simulate(curr_map, visits)
                    if move_result == "CYCLE":
                        res.append((x, y))
                counter += 1

        print(len(res))


if __name__ == '__main__':
    part_one()
    part_two()
