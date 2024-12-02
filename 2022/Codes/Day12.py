from typing import List
from collections import deque
from copy import deepcopy

DEMO_PATH = "../Inputs/demo_input12.txt"
INPUT_PATH = "../Inputs/input12.txt"

INFINITY = 1000000


class Node:
    def __init__(self, height, i, j):
        self.steps = INFINITY
        self.height = height
        self.visited = False
        self.i = i
        self.j = j

    def __repr__(self):
        return f"{self.height}"


def BFS(array: List[List[Node]], starting_node, ending_node):
    queue = deque()
    array[starting_node[0]][starting_node[1]].steps = 0
    visit(array, starting_node[0], starting_node[1], queue)
    while len(queue) > 0:
        curr_node = queue.popleft()
        if array[curr_node.i][curr_node.j].steps > curr_node.steps:
            array[curr_node.i][curr_node.j].steps = curr_node.steps
            visit(array, curr_node.i, curr_node.j, queue)
    return array[ending_node[0]][ending_node[1]].steps


def visit(array: List[List[Node]], i: int, j: int, queue: deque):
    curr_node = array[i][j]
    curr_node.visited = True
    possible_coordinates = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
    for coordinates in possible_coordinates:
        x, y = coordinates
        if can_move_to(array, x, y, curr_node):
            node_to_queue = Node(array[x][y].height, x, y)
            node_to_queue.steps = curr_node.steps + 1
            queue.append(node_to_queue)


def can_move_to(array: List[List[Node]], i: int, j: int, curr_node: Node):
    if i < 0 or j < 0:
        return False
    if i >= len(array) or j >= len(array[0]):
        return False
    next_node = array[i][j]
    if next_node.height > curr_node.height + 1:
        return False
    else:
        if not next_node.visited:
            return True
        else:
            if next_node.steps > curr_node.steps + 1:
                return True
    return False


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        grid = []
        starting_node = None
        ending_node = None
        for i in range(len(data)):
            new_row = []
            for j in range(len(data[i])):
                point = data[i][j]
                if point == "S":
                    starting_node = i, j
                    new_row.append(Node(0, i, j))
                elif point == "E":
                    ending_node = i, j
                    new_row.append(Node(25, i, j))
                else:
                    new_row.append(Node(ord(point) - ord("a"), i, j))
            grid.append(new_row)
    # part one
    # print(BFS(grid, starting_node, ending_node))

    # part two
    results = []
    number_of_iterations = sum([row.count("a") for row in data])
    iteration = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].height == 0:
                new_grid = deepcopy(grid)
                results.append(BFS(new_grid, (i, j), ending_node))
                print(f"Iteration {iteration}/{number_of_iterations}")
                iteration += 1
    print(min(results))
