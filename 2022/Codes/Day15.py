DEMO_PATH = "../Inputs/demo_input15.txt"
INPUT_PATH = "../Inputs/input15.txt"
EMPTY = 0
SENSOR = 1
BEACON = 2
POSSIBLE_BEACON = 3


def distance_between_coordinates(coordinates_1, coordinates_2):
    distance = 0
    distance += abs(coordinates_1[0] - coordinates_2[0])
    distance += abs(coordinates_1[1] - coordinates_2[1])
    return distance


def point_on_line_n_in_distance(position, distance, n):
    steps = abs(position[1] - n)
    length_over_n = distance - steps + 1
    position_on_n_1 = [(position[0] + i, n) for i in range(length_over_n)]
    position_on_n_2 = [(position[0] - i, n) for i in range(1, length_over_n)]
    return position_on_n_1 + position_on_n_2


def part_one(sensors_list, beacons_list, n):
    all_positions = []
    for i in range(len(sensors_list)):
        distance = distance_between_coordinates(sensors_list[i], beacons_list[i])
        print(distance, sensors_list[i], beacons_list[i])
        all_positions += point_on_line_n_in_distance(sensors_list[i], distance, n)
    all_positions = set(all_positions)
    for i in range(len(sensors_list)):
        if sensors_list[i] in all_positions:
            all_positions.remove(sensors_list[i])
        if beacons_list[i] in all_positions:
            all_positions.remove(beacons_list[i])
    print(len(all_positions))


def merge_intervals(intervals_list, max_x):
    intervals_list.sort(key=lambda x: x[0])
    result = (intervals_list[0][0], intervals_list[0][1])
    for interval in intervals_list:
        if interval[0] > result[1] + 1:
            if interval[0] - result[1] > 2:
                print("kupsko")
                return
            else:
                return result[1] + 1
        else:
            result = (0, max(result[1], interval[1]))
    if result == (0, max_x):
        return -1
    else:
        if max_x - result[1] > 1:
            print("kupsko2")
            return
        elif result[0] != 0 and result[1] != max_x:
            print("kupsko3")
            return
        elif result[0] > 1:
            print("kupsko4")
        else:
            return result[1] + 1


def in_range_on_n(sensors_list, distances, n, boundary):
    ranges = []
    for i in range(len(sensors_list)):
        steps_over_n = distances[i] - abs(sensors_list[i][1] - n)
        if steps_over_n > 0:
            ranges.append((max(sensors_list[i][0] - steps_over_n, boundary[0]),
                           min(boundary[1], sensors_list[i][0] + steps_over_n)))
    merge_result = merge_intervals(ranges, boundary[1])
    return merge_result


def part_two(sensors, beacons, boundary):
    distances = [distance_between_coordinates(sensors[i], beacons[i]) for i in range(len(sensors))]
    for i in range(boundary[1]):
        in_range = in_range_on_n(sensors, distances, i, boundary)
        if in_range is not None:
            if in_range > 0:
                print(in_range * 4000000 + i)


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [element.split(" ") for element in data]
        data = [[element[2].split("=")[1], element[3].split("=")[1], element[8].split("=")[1], element[9].split("=")[1]]
                for element in data]
        data = [
            list(map(lambda coordinate: int("".join(filter(lambda x: "0" <= x <= "9" or x == "-", coordinate))), line))
            for line in data]
        sensors = [(row[0], row[1]) for row in data]
        beacons = [(row[2], row[3]) for row in data]
        boundary = (0, 4000000)
