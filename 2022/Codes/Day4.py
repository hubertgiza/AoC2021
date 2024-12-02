DEMO_PATH = "../Inputs/demo_input4.txt"
INPUT_PATH = "../Inputs/input4.txt"


def contains(left, right):
    if left[0] <= right[0] and left[1] >= right[1]:
        return True
    if right[0] <= left[0] and right[1] >= left[1]:
        return True
    return False


def overlaps(left, right, depth=0):
    if right[0] <= left[0] <= right[1]:
        return True
    if right[0] <= left[1] <= right[1]:
        return True
    if depth == 0:
        return overlaps(right, left, 1)
    return False


def part_one(data):
    results = [1 if contains(*pairs) else 0 for pairs in data]
    print(sum(results))


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [line.split(",") for line in data]
        data = [list(map(lambda x: x.split("-"), line)) for line in data]
        data = [(tuple(map(lambda x: int(x), pair[0])), tuple(map(lambda x: int(x), pair[1]))) for pair in data]
    results = [1 if overlaps(*pairs) else 0 for pairs in data]
    print(sum(results))
