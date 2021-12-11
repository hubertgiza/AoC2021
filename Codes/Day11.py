import numpy as np

from Library import PATH_TO_INPUTS_2
from itertools import product

with open(PATH_TO_INPUTS_2 + "/input11.txt", "r") as f:
    data = f.readlines()
data = np.array([list(map(int, element.replace('\n', ''))) for element in data])
data = np.vstack([np.full(shape=data.shape[1], dtype='int16', fill_value=-1), data,
                  np.full(shape=data.shape[1], dtype='int16', fill_value=-1)])
data = np.hstack((np.full(shape=(data.shape[0], 1), dtype='int16', fill_value=-1), data,
                  np.full(shape=(data.shape[0], 1), dtype='int16', fill_value=-1)))


def flash(arr, arr_visited, i, j):
    coordinates = list(product([i - 1, i, i + 1], [j - 1, j, j + 1]))
    coordinates.remove((i, j))
    arr_visited[(i, j)] = 1
    for point in coordinates:
        if arr[point] != -1:
            arr[point] += 1
        if not arr_visited[point] and arr[point] > 9:
            flash(arr, arr_visited, point[0], point[1])


def step_one(arr):
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            arr[i, j] += 1


def step_two(arr, arr_visited):
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            if not arr_visited[i, j] and arr[i, j] > 9:
                flash(arr, arr_visited, i, j)


def step_three(arr):
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            if arr[i, j] > 9:
                arr[i, j] = 0


def count_flashes(arr):
    return np.sum(arr == 0)


def simulate_iteration(arr):
    flashing_octopuses = np.zeros(shape=arr.shape, dtype='int8')
    step_one(arr)
    step_two(arr, flashing_octopuses)
    step_three(arr)
    return count_flashes(arr)


def part_one():
    s = 0
    for i in range(195):
        s += simulate_iteration(data)
    print(s)


def part_two():
    iteration = 1
    while simulate_iteration(data) != 100:
        iteration += 1
        continue
    print(iteration)
