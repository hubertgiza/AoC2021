import json
from collections import deque

DEMO_PATH = "../Inputs/demo_input13.txt"
INPUT_PATH = "../Inputs/input13.txt"
CORRECT_ORDER = 1
CONTINUE = 0
INCORRECT_ORDER = -1


class Array:
    def __init__(self, string):
        self.array = json.loads(string)

    def __lt__(self, other):
        res = compare_elements(self.array, other.array)
        if res == CORRECT_ORDER:
            return True
        return False

    def __repr__(self):
        return f"{self.array}"


def part_one(data):
    data = [element.split("\n") for element in data]
    data = [(string_to_list(row[0]), string_to_list(row[1])) for row in data]
    correct_indexes = []
    for i in range(len(data)):
        list_left = data[i][0]
        list_right = data[i][1]
        result = compare_elements(list_left, list_right)
        if result == CORRECT_ORDER:
            correct_indexes.append(i + 1)
    print(sum(correct_indexes))


def part_two(data):
    data = list(filter(lambda x: x != "", data))
    data = [Array(element) for element in data]
    divider_1 = Array("[[2]]")
    divider_2 = Array("[[6]]")
    data.append(divider_1)
    data.append(divider_2)
    data.sort()
    print((data.index(divider_1) + 1) * (data.index(divider_2) + 1))


def string_to_list(string: str):
    return json.loads(string)


def compare_elements(array_left, array_right):
    for element_left, element_right in zip(array_left, array_right):
        if isinstance(element_left, int) and isinstance(element_right, int):
            if element_left < element_right:
                return CORRECT_ORDER
            elif element_left > element_right:
                return INCORRECT_ORDER
        elif isinstance(element_left, list) and isinstance(element_right, list):
            result = compare_elements(element_left, element_right)
            if result == CORRECT_ORDER or result == INCORRECT_ORDER:
                return result
        elif isinstance(element_left, int) and isinstance(element_right, list):
            result = compare_elements([element_left], element_right)
            if result == CORRECT_ORDER or result == INCORRECT_ORDER:
                return result
        elif isinstance(element_left, list) and isinstance(element_right, int):
            result = compare_elements(element_left, [element_right])
            if result == CORRECT_ORDER or result == INCORRECT_ORDER:
                return result
    if len(array_left) < len(array_right):
        return CORRECT_ORDER
    if len(array_left) > len(array_right):
        return INCORRECT_ORDER
    return CONTINUE


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        # data = f.read().split("\n\n")
        # part_one(data)
        data = f.read().split("\n")
        part_two(data)