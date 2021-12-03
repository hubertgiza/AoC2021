from Library import *

with open(PATH_TO_INPUTS + "/input2.txt", "r") as f:
    data = f.readlines()
data = [line.replace("\n", '').split(' ') for line in data]


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class Submarine:
    def __init__(self):
        self.X = 0
        self.depth = 0

    def forward(self, x):
        self.X += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x

    def __repr__(self):
        return str(self.X * self.depth)


def part_one(puzzle):
    save_the_christmas = Submarine()
    for move in puzzle:
        if move[0] == "forward":
            save_the_christmas.forward(int(move[1]))
        elif move[0] == "up":
            save_the_christmas.up(int(move[1]))
        else:
            save_the_christmas.down(int(move[1]))
    print(save_the_christmas)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class Submarine2:
    def __init__(self):
        self.X = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.X += x
        self.depth += self.aim * x

    def up(self, x):
        self.aim -= x

    def down(self, x):
        self.aim += x

    def __repr__(self):
        return str(self.depth * self.X)


def part_two(puzzle):
    save_the_christmas = Submarine2()
    for move in puzzle:
        if move[0] == "forward":
            save_the_christmas.forward(int(move[1]))
        elif move[0] == "up":
            save_the_christmas.up(int(move[1]))
        else:
            save_the_christmas.down(int(move[1]))
    print(save_the_christmas)
