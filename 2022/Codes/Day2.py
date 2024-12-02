DEMO_PATH = "../Inputs/demo_input2.txt"
INPUT_PATH = "../Inputs/input2.txt"

LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

X_SCORE = 1
Y_SCORE = 2
Z_SCORE = 3


def score(left, right):
    shape_score = X_SCORE if right == "A" else Y_SCORE if right == "B" else Z_SCORE
    if left == right:
        return shape_score + DRAW_SCORE
    if left == "A":
        if right == "C":
            return shape_score + LOSE_SCORE
        if right == "B":
            return shape_score + WIN_SCORE
    if left == "B":
        if right == "A":
            return shape_score + LOSE_SCORE
        if right == "C":
            return shape_score + WIN_SCORE
    if left == "C":
        if right == "B":
            return shape_score + LOSE_SCORE
        if right == "A":
            return shape_score + WIN_SCORE


def get_losing_shape(left):
    if left == "A":
        return "C"
    elif left == "B":
        return "A"
    else:
        return "B"


def get_drawing_shape(left):
    return left


def get_wining_shape(left):
    if left == "A":
        return "B"
    elif left == "B":
        return "C"
    else:
        return "A"


def part_one(data):
    data = [(element[0], "A" if element[1] == "X" else "B" if element[1] == "Y" else "C") for element in data]
    print("Part one: " + str(sum(score(*match) for match in data)))


def part_two(data):
    func_dict = {"X": get_losing_shape, "Y": get_drawing_shape, "Z": get_wining_shape}
    data = [(left, func_dict[right](left)) for left, right in data]
    print("Part two: " + str(sum(score(*match) for match in data)))


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = list(map(lambda x: x.split(" "), f.read().split("\n")))
    part_one(data)
    part_two(data)
