from collections import deque

DEMO_PATH = "../Inputs/demo_input5.txt"
INPUT_PATH = "../Inputs/input5.txt"


def part_one(data):
    columns = [deque() for _ in range(10)]
    instructions = []
    for line in data:
        if len(line) == 0:
            continue
        if line[0] == " " or line[0] == "[":
            spaces = 0
            letters = 0
            for i in range(len(line)):
                if line[i] == " ":
                    if letters > 0 and line[i - 1] == "]":
                        continue
                    spaces += 1
                elif "A" <= line[i] <= "Z":
                    columns[(spaces // 4) + letters + 1].append(line[i])
                    letters += 1
        elif not "0" <= line[0] <= "9":
            line = line.split(" ")
            instructions.append((int(line[1]), int(line[3]), int(line[5])))

    for instruction in instructions:
        for _ in range(instruction[0]):
            element = columns[instruction[1]].popleft()
            columns[instruction[2]].appendleft(element)

    result = "".join([column[0] if len(column) != 0 else "" for column in columns])
    print(result)


def part_two(data):
    columns = [deque() for _ in range(10)]
    instructions = []
    for line in data:
        if len(line) == 0:
            continue
        if line[0] == " " or line[0] == "[":
            spaces = 0
            letters = 0
            for i in range(len(line)):
                if line[i] == " ":
                    if letters > 0 and line[i - 1] == "]":
                        continue
                    spaces += 1
                elif "A" <= line[i] <= "Z":
                    columns[(spaces // 4) + letters + 1].append(line[i])
                    letters += 1
        elif not "0" <= line[0] <= "9":
            line = line.split(" ")
            instructions.append((int(line[1]), int(line[3]), int(line[5])))

    for instruction in instructions:
        crates = deque()
        for _ in range(instruction[0]):
            crates.appendleft(columns[instruction[1]].popleft())
        columns[instruction[2]].extendleft(crates)

    result = "".join([column[0] if len(column) != 0 else "" for column in columns])
    print(result)


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
    part_one(data)
    part_two(data)
