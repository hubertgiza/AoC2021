from itertools import combinations

DEMO_PATH = "../Inputs/demo_input2.txt"
INPUT_PATH = "../Inputs/input2.txt"


def check_if_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] >= 0 or abs(arr[i] - arr[i + 1]) > 3:
            return False
    return True


def check_if_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] <= 0 or abs(arr[i] - arr[i + 1]) > 3:
            return False
    return True


def part_one():
    with open(INPUT_PATH) as f:
        data = f.read().split("\n")
        data = [list(map(int, element.split(" "))) for element in data]
        res = []
        for report in data:
            is_increasing = check_if_increasing(report)
            is_decreasing = check_if_decreasing(report)
            res.append(is_increasing or is_decreasing)
        print(sum(res))


def part_two():
    with open(INPUT_PATH) as f:
        data = f.read().split("\n")
        data = [list(map(int, element.split(" "))) for element in data]
        res = []
        for report in data:
            all_combinations = combinations(report, len(report) - 1)
            combinations_result = [check_if_increasing(combination) or check_if_decreasing(combination) for combination in all_combinations]
            res.append(any(combinations_result))
        print(sum(res))


if __name__ == '__main__':
    part_one()
    part_two()
