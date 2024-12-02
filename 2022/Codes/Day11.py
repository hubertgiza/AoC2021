DEMO_PATH = "../Inputs/demo_input11.txt"
INPUT_PATH = "../Inputs/input11.txt"

DEMO_MODULO_VALUE = 23 * 19 * 13 * 17
INPUT_MODULO_VALUE = 19 * 13 * 5 * 7 * 17 * 2 * 3 * 11


class Monkey:
    def __init__(self, idx: int, starting_items: list, worry_function, test: int):
        self.idx = idx
        self.items = starting_items
        self.worry_function = worry_function
        self.test = test
        self.monkey_true = None
        self.monkey_false = None
        self.inspections = 0

    def throw(self):
        if len(self.items) == 0:
            return
        item = self.items.pop(0)
        item = self.worry_function(item)

        # dividing only in part one
        # item //= 3

        if item % self.test == 0:
            self.monkey_true.items.append(item % INPUT_MODULO_VALUE)
        else:
            self.monkey_false.items.append(item % INPUT_MODULO_VALUE)
        self.inspections += 1
        self.throw()

    def __lt__(self, other):
        return self.inspections < other.inspections

    def __repr__(self):
        return f"{self.idx}: {self.inspections} "


def demo_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0, [79, 98], lambda x: x * 19, 23))
    monkey_list.append(Monkey(1, [54, 65, 75, 74], lambda x: x + 6, 19))
    monkey_list.append(Monkey(2, [79, 60, 97], lambda x: x ** 2, 13))
    monkey_list.append(Monkey(3, [74], lambda x: x + 3, 17))
    monkey_list[0].monkey_true = monkey_list[2]
    monkey_list[0].monkey_false = monkey_list[3]
    monkey_list[1].monkey_true = monkey_list[2]
    monkey_list[1].monkey_false = monkey_list[0]
    monkey_list[2].monkey_true = monkey_list[1]
    monkey_list[2].monkey_false = monkey_list[3]
    monkey_list[3].monkey_true = monkey_list[0]
    monkey_list[3].monkey_false = monkey_list[1]
    return monkey_list


def input_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0, [93, 98], lambda x: x * 17, 19))
    monkey_list.append(Monkey(1, [95, 72, 98, 82, 86], lambda x: x + 5, 13))
    monkey_list.append(Monkey(2, [85, 62, 82, 86, 70, 65, 83, 76], lambda x: x + 8, 5))
    monkey_list.append(Monkey(3, [86, 70, 71, 56], lambda x: x + 1, 7))
    monkey_list.append(Monkey(4, [77, 71, 86, 52, 81, 67], lambda x: x + 4, 17))
    monkey_list.append(Monkey(5, [89, 87, 60, 78, 54, 77, 98], lambda x: x * 7, 2))
    monkey_list.append(Monkey(6, [69, 65, 63], lambda x: x + 6, 3))
    monkey_list.append(Monkey(7, [89], lambda x: x ** 2, 11))

    monkey_list[0].monkey_true = monkey_list[5]
    monkey_list[0].monkey_false = monkey_list[3]

    monkey_list[1].monkey_true = monkey_list[7]
    monkey_list[1].monkey_false = monkey_list[6]

    monkey_list[2].monkey_true = monkey_list[3]
    monkey_list[2].monkey_false = monkey_list[0]

    monkey_list[3].monkey_true = monkey_list[4]
    monkey_list[3].monkey_false = monkey_list[5]

    monkey_list[4].monkey_true = monkey_list[1]
    monkey_list[4].monkey_false = monkey_list[6]

    monkey_list[5].monkey_true = monkey_list[1]
    monkey_list[5].monkey_false = monkey_list[4]

    monkey_list[6].monkey_true = monkey_list[7]
    monkey_list[6].monkey_false = monkey_list[2]

    monkey_list[7].monkey_true = monkey_list[0]
    monkey_list[7].monkey_false = monkey_list[2]
    return monkey_list


if __name__ == '__main__':
    monkeys = input_monkeys()
    for i in range(10000):
        # print(i)
        for monkey in monkeys:
            monkey.throw()
    monkeys.sort(reverse=True)
    print(monkeys)
    print(monkeys[0].inspections * monkeys[1].inspections)
