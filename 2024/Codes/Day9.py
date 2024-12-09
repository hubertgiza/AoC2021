DEMO_PATH = "../Inputs/demo_input9.txt"
INPUT_PATH = "../Inputs/input9.txt"


class Block:
    def __init__(self, val, length):
        self.val = val
        self.length = length
        self.is_pause = val == -1
        self.calculated = False

    def calculate(self, curr_idx):
        assert self.val != -1
        self.calculated = True
        return sum([self.val * (curr_idx + i) for i in range(self.length)])

    def __str__(self):
        return f"({self.val, self.length})"

    def __repr__(self):
        return f"{self.val, self.length}"


def part_one():
    with open(DEMO_PATH, "r") as f:
        data = f.read()

        curr_id = 0
        now_file = True
        res = []
        for i in range(len(data)):
            if now_file:
                res += [curr_id] * int(data[i])
                curr_id += 1
                now_file = False
            else:
                res += ["."] * int(data[i])
                now_file = True
        checksum = 0
        idx = 0
        i = 0
        j = len(res) - 1
        print(res)
        while i <= j:
            if res[i] != ".":
                checksum += idx * int(res[i])
                idx += 1
                i += 1
            else:
                if res[j] != ".":
                    checksum += idx * int(res[j])
                    idx += 1
                    i += 1
                    j -= 1
                else:
                    j -= 1
        print(checksum)


if __name__ == '__main__':
    with open(INPUT_PATH, "r") as f:
        data = f.read()

    file_system = []
    free_space = False
    id = 0

    for i in data:
        if free_space:
            length = int(i)
            file_system.append((-1, int(length)))
            free_space = False
        else:
            length = int(i)
            file_system.append((id, int(length)))
            id += 1
            free_space = True

    index = len(file_system) - 1
    while index > 0:
        if file_system[index][0] == -1:
            index -= 1
            continue

        block_length = file_system[index][1]
        for j in range(index):
            if file_system[j][0] == -1:
                free_length = file_system[j][1]
                free_block_found = False
                if free_length == block_length:
                    free_block_found = True
                    file_system[j] = file_system[index]
                if free_length > block_length:
                    free_block_found = True
                    file_system.insert(j, file_system[index])
                    index += 1
                    file_system[j + 1] = (-1, free_length - block_length)

                if free_block_found:
                    file_system[index] = (-1, block_length)
                    break
        i = 0
        while i < len(file_system) - 1:
            if file_system[i][0] == -1:
                if file_system[i + 1][0] == -1:
                    file_system[i] = (-1, file_system[i + 1][1] + file_system[i][1])
                    del file_system[i + 1]
            i += 1
        index -= 1
    checksum = 0
    i = 0
    for f in file_system:
        if f[0] == -1:
            i += f[1]
            continue
        for _ in range(f[1]):
            checksum += i * f[0]
            i += 1

    print(checksum)
