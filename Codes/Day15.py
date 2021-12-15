import numpy as np

from Library import PATH_TO_INPUTS
from collections import deque
import sys

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=200)

with open(PATH_TO_INPUTS + "/input15.txt", "r") as f:
    data = f.readlines()
data = np.array([list(map(int, element.replace('\n', ''))) for element in data])
data = np.vstack([np.full(shape=data.shape[1], dtype='int16', fill_value=-1), data,
                  np.full(shape=data.shape[1], dtype='int16', fill_value=-1)])
data = np.hstack((np.full(shape=(data.shape[0], 1), dtype='int16', fill_value=-1), data,
                  np.full(shape=(data.shape[0], 1), dtype='int16', fill_value=-1)))
shortest_paths = np.full(shape=data.shape, dtype='int32', fill_value=100000)
shortest_paths[:, 0] = -1
shortest_paths[0, :] = -1
shortest_paths[:, -1] = -1
shortest_paths[-1, :] = -1


def BFS(arr, arr_visited, i, j):
    def get_neighbours(x, y):
        return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)

    query = deque()
    query.append((i, j))
    arr_visited[(i, j)] = 0
    while len(query) > 0:
        curr_point = query.popleft()
        for neighbour in get_neighbours(*curr_point):
            if arr_visited[neighbour] > arr_visited[curr_point] + arr[neighbour]:
                arr_visited[neighbour] = arr_visited[curr_point] + arr[neighbour]
                query.append(neighbour)
    print(arr_visited[-2, -2])


def part_one():
    BFS(data, shortest_paths, 1, 1)


def create_full_maps(arr):
    def compute_risk(array, a, b):
        res = array + a + b
        return res if res < 10 else res - 9

    big_shape = (arr.shape[0] - 2) * 5 + 2, (arr.shape[1] - 2) * 5 + 2

    big_paths_map = np.full(shape=big_shape, dtype='int32', fill_value=10000000)
    big_paths_map[:, 0] = -1
    big_paths_map[0, :] = -1
    big_paths_map[:, -1] = -1
    big_paths_map[-1, :] = -1

    big_map = np.zeros(shape=big_shape, dtype='int16')
    big_map[1:1 + (arr.shape[0] - 2), 1:1 + (arr.shape[1] - 2)] = arr[1:-1, 1:-1]
    big_map[:, 0] = -1
    big_map[0, :] = -1
    big_map[:, -1] = -1
    big_map[-1, :] = -1

    vectorized_risk = np.vectorize(compute_risk)
    for i in range(5):
        for j in range(5):
            big_map[1 + i * (arr.shape[0] - 2):1 + (i + 1) * (arr.shape[0] - 2),
            1 + j * (arr.shape[1] - 2):1 + (j + 1) * (arr.shape[1] - 2)] = vectorized_risk(arr[1:-1, 1:-1], i, j)
    return big_map, big_paths_map


big_data, big_paths = create_full_maps(data)
BFS(big_data, big_paths, 1, 1)
