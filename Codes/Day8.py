import numpy as np

from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input8.txt", "r") as f:
    data = f.readlines()
data = [element.replace('\n', '').split('|') for element in data]


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def day_one(puzzle):
    outputs = []
    for i in range(len(puzzle)):
        puzzle[i][1] = puzzle[i][1].split(' ')
        puzzle[i][1] = list(filter(lambda x: len(x) > 0, puzzle[i][1]))
        outputs.append(puzzle[i][1])

    count = 0
    for output in outputs:
        for element in output:
            if len(element) in (2, 3, 4, 7):
                count += 1
    print(count)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# The idea is to find number of common components between all segments and fill the matrix 10x10 with it. Each row is
# unique and it will be still unique after sort. So looking for the answer means taking each input and create the same
# common components matrix, sort the rows and then find matching rows in the templates matrix. Index of the row in
# templates matrix means that it is i-th segment. So finding out that given row from input common component matrix
# matches with i-th templates common components matrix means this given row is i-th segment.
class Segment:
    def __init__(self, *args):
        if len(args) == 7:
            self.up, self.left_1, self.right_1, self.middle, \
            self.left_2, self.right_2, self.bottom = list(args) + (7 - len(args)) * [None]
            self.components = set(filter(lambda x: x is not None, args))
        else:
            self.components = set(args[0])

    def __repr__(self):
        def none_to_dot(x):
            return x if x is not None else '.'

        return ' ' + f'{none_to_dot(self.up)}' * 4 + ' \n' + \
               (f'{self.left_1}' + 4 * ' ' + f'{self.right_1}\n') * 2 + \
               ' ' + f'{none_to_dot(self.middle)}' * 4 + ' \n' + \
               (f'{self.left_2}' + 4 * ' ' + f'{self.right_2}\n') * 2 + ' ' + \
               f'{none_to_dot(self.bottom)}' * 4 + ' '

    def __add__(self, other):
        return self.components & other.components


def create_common_element_matrix(data):
    segments = [Segment(element) for element in data]
    common_elements = [sorted([len(segments[i] + segments[j]) if i != j else 0 for j in range(len(segments))])
                       for i in range(len(segments))]
    return np.array(common_elements)


zero = Segment('a', 'b', 'c', None, 'e', 'f', 'g')
one = Segment(None, None, 'c', None, None, 'f', None)
two = Segment('a', None, 'c', 'd', 'e', None, 'g')
three = Segment('a', None, 'c', 'd', None, 'f', 'g')
four = Segment(None, 'b', 'c', 'd', None, 'f', None)
five = Segment('a', 'b', None, 'd', None, 'f', 'g')
six = Segment('a', 'b', None, 'd', 'e', 'f', 'g')
seven = Segment('a', None, 'c', None, None, 'f', None)
eight = Segment('a', 'b', 'c', 'd', 'e', 'f', 'g')
nine = Segment('a', 'b', 'c', 'd', None, 'f', 'g')

templates = [zero, one, two, three, four, five, six, seven, eight, nine]
common_elements_matrix_templates = [[len(templates[i] + templates[j]) if i != j else 0 for j in range(len(templates))]
                                    for i in
                                    range(len(templates))]

common_elements_matrix_templates = [sorted(element) for element in common_elements_matrix_templates]

inputs, outputs = zip(*data)
inputs = [list(filter(lambda x: len(x) > 0, element.split(' '))) for element in inputs]
outputs = [list(filter(lambda x: len(x) > 0, element.split(' '))) for element in outputs]

results = []
for i, entry in enumerate(inputs):
    inputs_segments_numbers = []
    common_elements_matrix_entry = create_common_element_matrix(entry)
    for segment in common_elements_matrix_entry:
        inputs_segments_numbers.append(
            np.argwhere(np.sum(common_elements_matrix_templates == segment, axis=1) == 10)[0][0])
    if len(set(inputs_segments_numbers)) != 10:
        print('shit')
        print(common_elements_matrix_templates)
        print(common_elements_matrix_entry)
        break
    inputs_components = [set(segment) for segment in entry]

    outputs_segments_numbers = []
    outputs_components = [set(element) for element in outputs[i]]
    for i in range(len(outputs_components)):
        for j in range(len(inputs_components)):
            if len(outputs_components[i].difference(inputs_components[j])) == \
                    len(inputs_components[j].difference(outputs_components[i])) == 0:
                outputs_segments_numbers.append(inputs_segments_numbers[j])
    results.append(sum([outputs_segments_numbers[k] * (10 ** (len(outputs_segments_numbers) - k - 1)) for k in
                        range(len(outputs_segments_numbers))]))
print(sum(results))
