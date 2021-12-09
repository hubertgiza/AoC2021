import numpy as np

from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input9.txt", "r") as f:
    data = f.readlines()

data = np.array([list(map(int, element.replace('\n', ''))) for element in data])


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def is_lowest_point(arr, i, j):
    x = arr[i, j]
    if i == 0:
        if j == 0:
            if x < arr[i + 1, j] and x < arr[i, j + 1]:
                return True
        elif j == arr.shape[1] - 1:
            if x < arr[i + 1, j] and x < arr[i, j - 1]:
                return True
        else:
            if x < arr[i, j - 1] and x < arr[i, j + 1] and x < arr[i + 1, j]:
                return True
    elif i == arr.shape[0] - 1:
        if j == 0:
            if x < arr[i - 1, j] and x < arr[i, j + 1]:
                return True
        elif j == arr.shape[1] - 1:
            if x < arr[i - 1, j] and x < arr[i, j - 1]:
                return True
        else:
            if x < arr[i, j - 1] and x < arr[i, j + 1] and x < arr[i - 1, j]:
                return True
    else:
        if j == 0:
            if x < arr[i + 1, j] and x < arr[i - 1, j] and x < arr[i, j + 1]:
                return True
        elif j == arr.shape[1] - 1:
            if x < arr[i + 1, j] and x < arr[i - 1, j] and x < arr[i, j - 1]:
                return True
        else:
            if x < arr[i, j - 1] and x < arr[i, j + 1] and x < arr[i + 1, j] and x < arr[i - 1, j]:
                return True
    return False


lowest_points_map = np.zeros(shape=data.shape, dtype='int32')
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if is_lowest_point(data, i, j):
            lowest_points_map[i, j] = data[i, j] + 1
# print(np.sum(lowest_points_map))

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

visited = np.zeros(shape=data.shape, dtype='int8')
coordinates_lowest_points = np.argwhere(lowest_points_map > 0)


def DFS(arr_map, arr_visited, lowest_points):
    def DFS_visit(arr_map, arr_visited, i, j):
        arr_visited[i, j] = 1
        nonlocal time
        time += 1

        if i == 0:
            if j == 0:
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
            elif j == arr_map.shape[1] - 1:
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
            else:
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
        elif i == arr_map.shape[0] - 1:
            if j == 0:
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
            elif j == arr_map.shape[1] - 1:
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
            else:
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
        else:
            if j == 0:
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
            elif j == arr_map.shape[1] - 1:
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
            else:
                if not arr_visited[i, j - 1] and arr_map[i, j - 1] != 9 and arr_map[i, j - 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j - 1)
                if not arr_visited[i - 1, j] and arr_map[i - 1, j] != 9 and arr_map[i - 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i - 1, j)
                if not arr_visited[i + 1, j] and arr_map[i + 1, j] != 9 and arr_map[i + 1, j] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i + 1, j)
                if not arr_visited[i, j + 1] and arr_map[i, j + 1] != 9 and arr_map[i, j + 1] > arr_map[i, j]:
                    DFS_visit(arr_map, arr_visited, i, j + 1)

    time = 0
    arr_times = []
    for point in lowest_points:
        i, j = point
        if not arr_visited[i, j]:
            DFS_visit(arr_map, arr_visited, i, j)
            arr_times.append(time)
            time = 0

    arr_times.sort(reverse=True)
    arr_times = arr_times[:3]
    print(arr_times[0]*arr_times[1]*arr_times[2])


DFS(data, visited, coordinates_lowest_points)
