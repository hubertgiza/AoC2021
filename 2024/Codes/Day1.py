DEMO_PATH = "../Inputs/demo_input1.txt"
INPUT_PATH = "../Inputs/input1.txt"


def part_1():
    with open(INPUT_PATH) as f:
        data = f.read().split("\n")
        data = [element.split(" ") for element in data]
        left = sorted([int(element[0]) for element in data])
        right = sorted([int(element[-1]) for element in data])
        diff = 0
        for i in range(len(left)):
            diff += abs(left[i] - right[i])
        print(diff)


def part_2():
    with open(INPUT_PATH) as f:
        data = f.read().split("\n")
        data = [element.split(" ") for element in data]
        left = sorted([int(element[0]) for element in data])
        right = sorted([int(element[-1]) for element in data])
        diff = 0
        for i in range(len(left)):
            count_in_right = right.count(left[i])
            diff += left[i] * count_in_right
        print(diff)


if __name__ == '__main__':
    part_1()
    part_2()
