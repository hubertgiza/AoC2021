DEMO_PATH = "../Inputs/demo_input3.txt"
INPUT_PATH = "../Inputs/input3.txt"


def score(letter: str):
    if "a" <= letter <= "z":
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def part_one(data):
    lengths = [len(line) for line in data]
    data = [set(line[:lengths[i] // 2]) & set(line[lengths[i] // 2:]) for i, line in enumerate(data)]
    print(sum(score(*element) for element in data))


def part_two(data):
    data = [set(data[i]) & set(data[i + 1]) & set(data[i + 2]) for i in range(0, len(data), 3)]
    print(sum(score(*element) for element in data))


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
    part_one(data)
    part_two(data)
