import numpy as np

from Library import PATH_TO_INPUTS

np.set_printoptions(linewidth=100)
with open(PATH_TO_INPUTS + "/input13.txt", "r") as f:
    data = f.readlines()
data = [element.replace('\n', '').split(',') for element in data]
points = list(map(lambda x: (int(x[0]), int(x[1])), filter(lambda x: len(x) > 1, data)))
folds = [element[0].split(' ')[-1].split('=') for element in list(filter(lambda x: len(x) == 1, data))]


def vertical_fold(arr, y, arr_x=-1, arr_y=-1):
    if arr_x == -1 and arr_y == -1:
        arr_x, arr_y = arr.shape
    for i in range(y + 1, arr_x):
        for j in range(arr_y):
            if arr[i, j] == 1:
                arr[i, j] = 0
                new_row = y - (i - y)
                if new_row >= 0:
                    arr[new_row, j] = 1


def horizontal_fold(arr, x, arr_x=-1, arr_y=-1):
    if arr_x == -1 and arr_y == -1:
        arr_x, arr_y = arr.shape
    for i in range(arr_x):
        for j in range(x + 1, arr_y):
            if arr[i, j] == 1:
                arr[i, j] = 0
                new_column = x - (j - x)
                if new_column >= 0:
                    arr[i, new_column] = 1


max_x = max(points, key=lambda x: x[0])[0] + 1
max_y = max(points, key=lambda x: x[1])[1] + 1

thermal_map = np.zeros(shape=(max_y, max_x), dtype='int8')
for point in points:
    thermal_map[point[1], point[0]] = 1


def part_one():
    first_fold = folds[0]
    if first_fold[0] == 'y':
        vertical_fold(thermal_map, int(first_fold[1]))
        print(np.sum(thermal_map))
    else:
        horizontal_fold(thermal_map, int(first_fold[1]))
        print(np.sum(thermal_map))


def part_two():
    arr_shape = thermal_map.shape
    for fold in folds:
        if fold[0] == 'y':
            vertical_fold(thermal_map, int(fold[1]), *arr_shape)
            arr_shape = int(fold[1]), arr_shape[1]
        else:
            horizontal_fold(thermal_map, int(fold[1]), *arr_shape)
            arr_shape = arr_shape[0], int(fold[1])

    result_map = thermal_map[:arr_shape[0], :arr_shape[1]]
    print(result_map)
    print(np.sum(result_map))
