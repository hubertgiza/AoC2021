import numpy as np

DEMO_PATH = "../Inputs/demo_input7.txt"
INPUT_PATH = "../Inputs/input7.txt"


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


operations_dict = {
    "+": add,
    "*": mul,
    "||": concat
}


def calculate_part_one(curr_signs, curr_i, all_numbers, target):
    if curr_i == len(all_numbers):
        res = 0
        for i in range(len(curr_signs) - 1):
            if i == 0:
                res = operations_dict[curr_signs[i]](all_numbers[i], all_numbers[i + 1])
            else:
                res = operations_dict[curr_signs[i]](res, all_numbers[i + 1])
        if res == target:
            return True
        return False
    res_1 = calculate_part_one(curr_signs + ["+"], curr_i + 1, all_numbers, target)
    res_2 = calculate_part_one(curr_signs + ["*"], curr_i + 1, all_numbers, target)
    res_3 = calculate_part_one(curr_signs + ["||"], curr_i + 1, all_numbers, target)
    return res_1 or res_2 or res_3


def calculate_part_two(curr_signs, curr_i, all_numbers, target):
    if curr_i == len(all_numbers):
        res = 0
        for i in range(len(curr_signs) - 1):
            if i == 0:
                if curr_signs[i] == "+":
                    res = all_numbers[i] + all_numbers[i + 1]
                else:
                    res = all_numbers[i] * all_numbers[i + 1]
            else:
                if curr_signs[i] == "+":
                    res = res + all_numbers[i + 1]
                else:
                    res = res * all_numbers[i + 1]
        if res == target:
            return True
        return False
    return calculate_part_one(curr_signs + ["+"], curr_i + 1, all_numbers, target) or calculate_part_one(curr_signs + ["*"], curr_i + 1, all_numbers, target)


def part_one():
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("\n")
        targets = []
        numbers = []
        for element in data:
            result, operations_numbers = element.split(":")

            numbers.append(list(map(int, operations_numbers[1:].split(" "))))
            targets.append(int(result))
        results = [calculate_part_one([], 0, numbers[i], targets[i]) for i in range(len(targets))]
        print(np.sum(np.array(targets) * np.array(results)))


if __name__ == '__main__':
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("\n")
        targets = []
        numbers = []
        for element in data:
            result, operations_numbers = element.split(":")
            numbers.append(list(map(int, operations_numbers[1:].split(" "))))
            targets.append(int(result))
        results = []
        for i in range(len(targets)):
            print(f"{i}/{len(targets)}")
            results.append(calculate_part_one([], 0, numbers[i], targets[i]))
        print(np.sum(np.array(targets) * np.array(results)))
