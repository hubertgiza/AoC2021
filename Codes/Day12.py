from Library import PATH_TO_INPUTS_2


class Vertex:
    def __init__(self, name, is_big=False):
        self.name = name
        if self.name == 'end':
            self.paths = 0
        self.is_big = is_big
        self.neighbours = []

    def add_neighbour(self, vertex):
        self.neighbours.append(vertex)


with open(PATH_TO_INPUTS_2 + "/input12.txt", "r") as f:
    data = f.readlines()
data = [element.replace('\n', '').split('-') for element in data]

vertices = {}
for element in data:
    if vertices.get(element[0]) is None:
        vertices[element[0]] = Vertex(element[0], True) if element[0].isupper() else Vertex(element[0])
    if vertices.get(element[1]) is None:
        vertices[element[1]] = Vertex(element[1], True) if element[1].isupper() else Vertex(element[1])
    vertices[element[0]].add_neighbour(vertices[element[1]])
    vertices[element[1]].add_neighbour(vertices[element[0]])


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one():
    def travel_part_one(vertex, small_caves_travelled):
        for cave in vertex.neighbours:
            if not cave.is_big and cave.name not in small_caves_travelled:
                if cave.name == 'end':
                    cave.paths += 1
                else:
                    travel_part_one(cave, small_caves_travelled + [cave.name])
            elif cave.is_big:
                travel_part_one(cave, small_caves_travelled)
        return

    travel_part_one(vertices['start'], ['start'])
    print(vertices['end'].paths)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two():
    def travel_part_two(vertex, small_caves_travelled, double_small_cave):
        for cave in vertex.neighbours:
            if not cave.is_big and cave.name not in small_caves_travelled:
                if cave.name == 'end':
                    cave.paths += 1
                else:
                    travel_part_two(cave, small_caves_travelled + [cave.name], double_small_cave)
            elif cave.is_big:
                travel_part_two(cave, small_caves_travelled, double_small_cave)
            elif not cave.is_big and small_caves_travelled.count(cave.name) == 1 and not double_small_cave:
                if cave.name != 'start' and cave.name != 'end':
                    travel_part_two(cave, small_caves_travelled + [cave.name], True)
        return

    travel_part_two(vertices['start'], ['start'], False)
    print(vertices['end'].paths)
