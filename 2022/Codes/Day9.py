DEMO_PATH = "../Inputs/demo_input9_1.txt"
DEMO_PATH2 = "../Inputs/demo_input9_2.txt"
INPUT_PATH = "../Inputs/input9.txt"


class Knot:
    def __init__(self, following=None):
        self.x = 0
        self.y = 0
        self.visited = []
        self.following = following

    def move_right(self):
        self.x = self.x + 1

    def more_left(self):
        self.x = self.x - 1

    def move_down(self):
        self.y = self.y - 1

    def move_up(self):
        self.y = self.y + 1

    def add_position(self):
        self.visited.append((self.x, self.y))

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def __repr__(self):
        return f"x:{self.x} y:{self.y}"


def part_one(data):
    head = Knot()
    tail = Knot()
    tail.add_position()
    for instruction in data:
        for _ in range(instruction[1]):
            if instruction[0] == "R":
                head.move_right()
            elif instruction[0] == "U":
                head.move_up()
            elif instruction[0] == "L":
                head.more_left()
            else:
                head.move_down()
            diff_x, diff_y = (head.x - tail.x, head.y - tail.y)
            if abs(diff_x) == 2 and abs(diff_y) == 1:
                diff_x //= 2
                tail.move(diff_x, diff_y)
            elif abs(diff_x) == 1 and abs(diff_y) == 2:
                diff_y //= 2
                tail.move(diff_x, diff_y)
            else:
                tail.move(int(diff_x / 2), int(diff_y / 2))
            tail.add_position()
    print(len(set(tail.visited)))


def part_two(data, number_of_tails):
    knots = [Knot()]
    for i in range(number_of_tails):
        new_tail = Knot(knots[i])
        knots.append(new_tail)
    for instruction in data:
        for _ in range(instruction[1]):
            if instruction[0] == "R":
                knots[0].move_right()
            elif instruction[0] == "U":
                knots[0].move_up()
            elif instruction[0] == "L":
                knots[0].more_left()
            else:
                knots[0].move_down()
            for i in range(1, len(knots)):
                diff_x, diff_y = (knots[i].following.x - knots[i].x, knots[i].following.y - knots[i].y)
                if abs(diff_x) == 2 and abs(diff_y) == 1:
                    diff_x = int(diff_x / 2)
                    knots[i].move(diff_x, diff_y)
                elif abs(diff_x) == 1 and abs(diff_y) == 2:
                    diff_y = int(diff_y / 2)
                    knots[i].move(diff_x, diff_y)
                elif abs(diff_x) == 2 and abs(diff_y) == 2:
                    diff_x = int(diff_x / 2)
                    diff_y = int(diff_y / 2)
                    knots[i].move(diff_x, diff_y)
                else:
                    knots[i].move(int(diff_x / 2), int(diff_y / 2))
                knots[-1].add_position()
    print(len(set(knots[-1].visited)))


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        f = lambda x: (x[0], int(x[1]))
        data = [f(element.split(" ")) for element in data]
    NUMBER_OF_TAILS = 9
    part_one(data)
    part_two(data, NUMBER_OF_TAILS)
