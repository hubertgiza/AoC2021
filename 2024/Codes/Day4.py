DEMO_PATH = "../Inputs/demo_input4.txt"
INPUT_PATH = "../Inputs/input4.txt"


def horizontal_search(row, i):
    res = 0
    if i >= 3:
        if row[i - 3:i] == "SAM":
            res += 1
    if i < len(row) - 3:
        if row[i + 1:i + 4] == "MAS":
            res += 1
    return res


def vertical_search(arr, i, j):
    res = 0
    if i >= 3:
        if arr[i - 1][j] + arr[i - 2][j] + arr[i - 3][j] == "MAS":
            res += 1
    if i < len(arr) - 3:
        if arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j] == "MAS":
            res += 1
    return res


def diagonal_search(arr, i, j):
    res = 0
    if i >= 3 and j >= 3:
        if arr[i - 1][j - 1] + arr[i - 2][j - 2] + arr[i - 3][j - 3] == "MAS":
            res += 1
    if i >= 3 and j < len(arr[i]) - 3:
        if arr[i - 1][j + 1] + arr[i - 2][j + 2] + arr[i - 3][j + 3] == "MAS":
            res += 1
    if i < len(arr) - 3 and j >= 3:
        if arr[i + 1][j - 1] + arr[i + 2][j - 2] + arr[i + 3][j - 3] == "MAS":
            res += 1
    if i < len(arr) - 3 and j < len(arr[i]) - 3:
        if arr[i + 1][j + 1] + arr[i + 2][j + 2] + arr[i + 3][j + 3] == "MAS":
            res += 1
    return res


def part_1():
    with open(INPUT_PATH, "r") as f:
        res = 0
        data = f.read().split("\n")
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "X":
                    horizontal = horizontal_search(data[i], j)
                    vertical = vertical_search(data, i, j)
                    diagonal = diagonal_search(data, i, j)
                    res += horizontal + vertical + diagonal
        print(res)


if __name__ == '__main__':
    x_mas_patterns = ["MSAMS", "SSAMM", "MMASS", "SMASM"]
    with open(INPUT_PATH, "r") as f:
        res = 0
        data = f.read().split("\n")
        for i in range(len(data) - 2):
            for j in range(len(data[i]) - 2):
                X = data[i][j] + data[i][j + 2] + data[i + 1][j + 1] + data[i + 2][j] + data[i + 2][j + 2]
                if X in x_mas_patterns:
                    res += 1
        print(res)
