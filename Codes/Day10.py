from Library import PATH_TO_INPUTS
from collections import deque

with open(PATH_TO_INPUTS + "/input10.txt", "r") as f:
    data = f.readlines()
data = [element.replace('\n', '') for element in data]

openings = ['{', '(', '[', '<']
closures_to_openings = {'}': '{', ')': '(', ']': '[', '>': '<'}
openings_to_closures = {'{': '}', '(': ')', '[': ']', '<': '>'}
scores_part_one = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_part_two = {')': 1, ']': 2, '}': 3, '>': 4}


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one():
    failures = []
    scores = []
    for line in data:
        q = deque()
        for char in line:
            if char in openings:
                q.append(char)
            else:
                opening = closures_to_openings[char]
                if q[-1] == opening:
                    q.pop()
                else:
                    scores.append(scores_part_one[char])
                    failures.append(char)
                    break
    print(sum(scores))


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def calculate_score(arr):
    total_score = 0
    for element in arr:
        total_score *= 5
        total_score += scores_part_two[element]
    return total_score


def part_two():
    incomplete_lines = []
    for line in data:
        q = deque()
        corrupted = False
        for char in line:
            if char in openings:
                q.append(char)
            else:
                opening = closures_to_openings[char]
                if q[-1] == opening:
                    q.pop()
                else:
                    corrupted = True
                    break
        if not corrupted:
            incomplete_lines.append((line, q))

    results = []
    for line in incomplete_lines:
        line[1].reverse()
        openings_left = list(map(lambda x: openings_to_closures[x], line[1]))
        results.append(calculate_score(openings_left))
    results.sort()
    print(results[len(results) // 2])
