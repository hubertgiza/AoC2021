DEMO_PATH = "../Inputs/demo_input1.txt"
INPUT_PATH = "../Inputs/input1.txt"

if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().split("\n\n")
        data = [list(map(lambda x: int(x), line.split("\n"))) for line in data]
        data = [sum(elf_items) for elf_items in data]
        print(sum(sorted(data, reverse=True)[0:3]))
