from collections import deque

DEMO_PATH = "../Inputs/demo_input16.txt"
INPUT_PATH = "../Inputs/input16.txt"
MINUTES = 30


class Valve:
    def __init__(self, name, idx, flow):
        self.name = name
        self.idx = idx
        self.flow = flow
        self.neighbours = []

    def __repr__(self):
        return f"{self.name}:{self.flow}"

    def calculate_value(self, n):
        return self.flow * n


def BFS(start_node, adjacency_list):
    visited = [-1] * len(adjacency_list)
    que = deque()
    visited[start_node] = 0
    que.append(start_node)
    while len(que) > 0:
        curr_node = que.pop()
        for neighbour in adjacency_list[curr_node]:
            if visited[neighbour] == -1:
                visited[neighbour] = visited[curr_node] + 1
                que.append(neighbour)
            elif visited[neighbour] > visited[curr_node] + 1:
                visited[neighbour] = visited[curr_node] + 1
                que.append(neighbour)
    return visited


def calculate_values(valves_list, distance_list, n):
    return [valves_list[i].flow * (n - distance_list[i]) for i in range(len(valves_list))]


if __name__ == '__main__':
    with open(DEMO_PATH) as f:
        data = f.read().splitlines()
        data = [line.split(" ") for line in data]
        data = [[line[1]] + [int(line[4].split("=")[1][:-1])] + line[9:] for line in data]
    name_to_index = {data[i][0]: i for i in range(len(data))}
    valves = []
    for i in range(len(data)):
        valves.append(Valve(data[i][0], name_to_index[data[i][0]], data[i][1]))
    for i in range(len(valves)):
        neighbours = tuple(map(lambda x: name_to_index[x[:-1]] if x[-1] == "," else name_to_index[x], data[i][2:]))
        for neighbour in neighbours:
            valves[i].neighbours.append(valves[neighbour])
    adjacency_list = [[neighbour.idx for neighbour in valve.neighbours] for valve in valves]
    distance_list = BFS(0, adjacency_list)
    for i in range(len(valves)):
        print(BFS(i, adjacency_list))

    print("--------------------------------------------------")
    for i in range(len(valves)):
        print(calculate_values(valves, BFS(i, adjacency_list), MINUTES))
    # print(name_to_index)
    # print(distance_list)
    # print(BFS(3, adjacency_list))
    # print(calculate_values(valves, distance_list, MINUTES))

# def visit(valve, time, taken_list, valves_list, value):
#     curr_valve = valves_list[valve]
#     if time == MINUTES:
#         value += calculate_value(valves_list, taken_list)
#         return value
