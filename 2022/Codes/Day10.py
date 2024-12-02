DEMO_PATH = "../Inputs/demo_input10.txt"
INPUT_PATH = "../Inputs/input10.txt"


class Sprite:
    def __init__(self):
        self.position = 0

    def check_if_contains(self, position):
        return self.position == position or self.position + 1 == position or self.position + 2 == position

    def set_position(self, position):
        self.position = position


class Processor:
    def __init__(self):
        self.cycle = 1
        self.value = 1
        # part one
        self.milestones = []
        # part two
        self.crt = []
        self.sprite = Sprite()

    def noop_part_one(self):
        self.check_if_milestone()
        self.cycle += 1

    def noop_part_two(self):
        self.draw()
        self.cycle += 1

    def add_part_one(self, value):
        self.check_if_milestone()
        self.cycle += 1
        self.check_if_milestone()
        self.cycle += 1
        self.value += value

    def add_part_two(self, value):
        self.draw()
        self.cycle += 1
        self.draw()
        self.cycle += 1
        self.value += value
        self.sprite.set_position(self.value)

    def draw(self):
        if self.sprite.check_if_contains(self.cycle % 40):
            self.crt.append("#")
        else:
            self.crt.append(".")

    def add_milestone_value(self):
        self.milestones.append((self.cycle, self.value))

    def check_if_milestone(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.add_milestone_value()

    def calculate_result(self):
        return sum(milestone[0] * milestone[1] for milestone in self.milestones)

    def __repr__(self):
        return f"{self.cycle}: {self.value}"


def part_one(data):
    processor = Processor()
    for instruction in data:
        if len(instruction) == 1:
            processor.noop_part_one()
        else:
            processor.add_part_one(instruction[1])
    print(processor.calculate_result())


def print_crt(processor: Processor):
    print("".join(processor.crt[0:40]))
    print("".join(processor.crt[40:80]))
    print("".join(processor.crt[80:120]))
    print("".join(processor.crt[120:160]))
    print("".join(processor.crt[160:200]))
    print("".join(processor.crt[200:240]))


def part_two(data):
    processor = Processor()
    for instruction in data:
        if len(instruction) == 1:
            processor.noop_part_two()
        else:
            processor.add_part_two(instruction[1])
    print_crt(processor)
    # BJFRHRFU


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [element.split(" ") for element in data]
        data = list(map(lambda x: x if len(x) == 1 else [x[0], int(x[1])], data))
