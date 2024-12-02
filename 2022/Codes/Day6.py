DEMO_PATH = "../Inputs/demo_input6.txt"
INPUT_PATH = "../Inputs/input6.txt"


def check_if_4_different(line, index):
    if len(set(line[(index - 3):index + 1])) == 4:
        return True
    return False


def check_if_14_different(line, index):
    if len(set(line[(index - 13):index + 1])) == 14:
        return True
    return False


def part_one(data):
    for line in data:
        for i in range(3, len(line)):
            if check_if_4_different(line, i):
                print(i + 1)
                break


def part_two(data):
    for line in data:
        for i in range(3, len(line)):
            if check_if_14_different(line, i):
                print(i + 1)
                break


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
    part_one(data)
    part_two(data)
