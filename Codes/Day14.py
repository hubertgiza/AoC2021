from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input14.txt", "r") as f:
    data = f.readlines()
data = [element.replace('\n', '').split(' -> ') for element in data]
polymer = data[0][0]


def calculate_score(string):
    values = set(string)
    occurrences = []
    for x in values:
        occurrences.append(string.count(x))
    return max(occurrences) - min(occurrences)


def part_one():
    global polymer
    productions_local = dict((x, y) for x, y in data[2:])

    for k in range(40):
        print(k)
        next_polymer = polymer[0]
        for i in range(1, len(polymer)):
            curr_key = polymer[i - 1] + polymer[i]
            if curr_key in productions_local.keys():
                next_polymer += productions_local[curr_key]
            next_polymer += polymer[i]
        polymer = next_polymer

    print(calculate_score(polymer))


def split_by_productions(string, dictionary):
    res = []
    for i in range(1, len(string)):
        if string[i - 1] + string[i] in dictionary.keys():
            res.append(string[i - 1] + string[i])
    return res


def part_two():
    productions_letter = dict((x, y) for x, y in data[2:])
    productions_whole = dict((x, x[0] + y + x[1]) for x, y in data[2:])
    productions_in_polymer = {}
    for production in split_by_productions(polymer, productions_whole):
        productions_in_polymer[production] = productions_in_polymer.get(production, 0) + 1
    for key in productions_whole.keys():
        productions_whole[key] = split_by_productions(productions_whole[key], productions_whole)

    letters_count = [0] * 26
    for letter in polymer:
        letters_count[ord(letter) - 65] += 1
    for _ in range(40):
        tmp_dict = productions_in_polymer.copy()
        for production in tmp_dict.keys():
            if tmp_dict[production] > 0:
                productions_to_add = productions_whole[production]
                for element in productions_to_add:
                    productions_in_polymer[element] = productions_in_polymer.get(element, 0) + tmp_dict[production]
            letters_count[ord(productions_letter[production]) - 65] += tmp_dict[production]
            productions_in_polymer[production] -= tmp_dict[production]

    print(max(letters_count) - min(filter(lambda x: x > 0, letters_count)))
