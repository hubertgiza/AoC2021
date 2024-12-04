DEMO_PATH_1 = "../Inputs/demo_input3_1.txt"
DEMO_PATH_2 = "../Inputs/demo_input3_2.txt"
INPUT_PATH = "../Inputs/input3.txt"


def validate(string: str) -> int:
    if len(string) < 5:
        return 0
    if string[0] != "(":
        return 0
    if ")" not in string or "," not in string:
        return 0
    comma_idx = string.find(",")
    end_idx = string.find(")")
    number_1 = string[1:comma_idx]
    number_2 = string[comma_idx + 1:end_idx]
    if number_1.isdecimal() and number_2.isdecimal():
        return int(number_1) * int(number_2)
    return 0


def part_1():
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("mul")
        values = [validate(element) for element in data]
        print(sum(values))


def part_2():
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("do()")
        for i, element in enumerate(data):
            dont = element.find("don't()")
            if dont != -1:
                data[i] = element[:dont]
            data[i] = data[i].split("mul")
        values = []
        for element in data:
            for string in element:
                values.append(validate(string))
        print(sum(values))


if __name__ == '__main__':
    part_1()
    part_2()
