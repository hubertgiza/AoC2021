from collections import defaultdict

DEMO_PATH = "../Inputs/demo_input5.txt"
INPUT_PATH = "../Inputs/input5.txt"


def validate_update(rules, update):
    for i in range(1, len(update)):
        for j in range(i):
            if update[j] in rules[update[i]]:
                return 0
    return int(update[len(update) // 2])


def fix_update(rules, update: list):
    if validate_update(rules, update) != 0:
        return 0

    for i in range(1, len(update)):
        for j in range(i):
            if update[j] in rules[update[i]]:
                element = update.pop(i)
                update.insert(j, element)
    return int(update[len(update) // 2])


def part_1():
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("\n")
        rules = defaultdict(list)
        updates = []
        now_rules = True
        for element in data:
            if len(element) == 0:
                now_rules = False
                continue
            if now_rules:
                left, right = element.split("|")
                rules[left].append(right)
            else:
                updates.append(element.split(","))
        results = [validate_update(rules, update) for update in updates]
        print(sum(results))


if __name__ == '__main__':
    with open(INPUT_PATH, "r") as f:
        data = f.read().split("\n")
        rules = defaultdict(list)
        updates = []
        now_rules = True
        for element in data:
            if len(element) == 0:
                now_rules = False
                continue
            if now_rules:
                left, right = element.split("|")
                rules[left].append(right)
            else:
                updates.append(element.split(","))
        results = [fix_update(rules, update) for update in updates]
        print(results)
        print(sum(results))
