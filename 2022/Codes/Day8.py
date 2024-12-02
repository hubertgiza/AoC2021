DEMO_PATH = "../Inputs/demo_input8.txt"
INPUT_PATH = "../Inputs/input8.txt"


class Tree:
    def __init__(self, height):
        self.height = height

        # part one
        self.visible_left = False
        self.visible_right = False
        self.visible_top = False
        self.visible_down = False

        # part two
        self.score_left = 0
        self.score_right = 0
        self.score_top = 0
        self.score_down = 0

    def __repr__(self):
        return f"{'T' if self.is_visible() else 'F'}"

    def is_visible(self):
        return self.visible_left | self.visible_top | self.visible_right | self.visible_down

    def get_score(self):
        return self.score_left * self.score_top * self.score_right * self.score_down


def part_one(data):
    for i in range(len(data)):
        max_height = -1
        for j in range(len(data[i])):
            if data[i][j].height > max_height:
                data[i][j].visible_left = True
                max_height = data[i][j].height

    for i in range(len(data)):
        max_height = -1
        for j in range(len(data[i]) - 1, -1, -1):
            if data[i][j].height > max_height:
                data[i][j].visible_right = True
                max_height = data[i][j].height

    for i in range(len(data)):
        max_height = -1
        for j in range(len(data)):
            if data[j][i].height > max_height:
                data[j][i].visible_top = True
                max_height = data[j][i].height

    for i in range(len(data)):
        max_height = -1
        for j in range(len(data) - 1, -1, -1):
            if data[j][i].height > max_height:
                data[j][i].visible_down = True
                max_height = data[j][i].height
    print(sum(1 if tree.is_visible() else 0 for row in data for tree in row))


def part_two(data):
    for row in range(len(data)):
        for column in range(len(data[row])):
            data[row][column].score_left = score(reversed(data[row][:column]), data[row][column].height)
            if column != len(data[row]):
                data[row][column].score_right = score(data[row][column + 1:], data[row][column].height)
            if row == 0:
                data[row][column].score_top = score(reversed(data[:row]), data[row][column].height)
            else:
                data[row][column].score_top = score(reversed(get_column(data[:row], column)), data[row][column].height)
            if row != len(data):
                data[row][column].score_down = score(get_column(data[row + 1:], column), data[row][column].height)
    print(max(tree.get_score() for row in data for tree in row))


def score(array, height):
    score_value = 0
    for element in array:
        score_value += 1
        if element.height < height:
            continue
        else:
            break
    return score_value


def get_column(matrix, i):
    return [row[i] for row in matrix]


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [list((map(int, list(line)))) for line in data]
        data = [list(map(Tree, row)) for row in data]

    part_one(data)
    part_two(data)
