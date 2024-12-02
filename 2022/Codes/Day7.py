DEMO_PATH = "../Inputs/demo_input7.txt"
INPUT_PATH = "../Inputs/input7.txt"

AVAILABLE_DISK_SPACE = 70000000
MINIMUM_SPACE = 30000000


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"({self.size} {self.name})"


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.files = []
        self.children = []
        self.size = -1

    def get_size_of_contents(self):
        if self.size == -1:
            self.size = 0
            for element in self.files:
                self.size += element.size
            for subdirectory in self.children:
                self.size += subdirectory.get_size_of_contents()
        return self.size

    def __repr__(self):
        return f'{self.name}'


def get_directory(name, dictionary):
    directory = dictionary.get(name)
    if directory is None:
        directory = Directory(name)
        dictionary[name] = directory
    return directory


def get_small_directories_sum(dir: Directory):
    result = 0
    size = dir.get_size_of_contents()
    if size <= 100000:
        result += size
    for subdirectory in dir.children:
        result += get_small_directories_sum(subdirectory)
    return result


def get_minimum_size_to_delete(dir, curr_space):
    best_difference = curr_space + dir.size - MINIMUM_SPACE
    if best_difference < 0:
        best_difference = AVAILABLE_DISK_SPACE
    for subdir in dir.children:
        best_difference = min(best_difference, get_minimum_size_to_delete(subdir, curr_space))
    return best_difference


def part_one(root_dir):
    print(get_small_directories_sum(root))


def part_two(root_dir):
    CURR_AVAILABLE_SPACE = AVAILABLE_DISK_SPACE - root.get_size_of_contents()
    best_difference = get_minimum_size_to_delete(root, CURR_AVAILABLE_SPACE)
    print(best_difference + MINIMUM_SPACE - CURR_AVAILABLE_SPACE)


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
        data = [line.split(" ") for line in data]
        curr_directory = Directory("/")
        root = curr_directory
        for line in data[1:]:
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        curr_directory = curr_directory.parent
                    else:
                        for directory in curr_directory.children:
                            if directory.name == line[2]:
                                curr_directory = directory
            elif line[0] == "dir":
                new_dir = Directory(line[1])
                curr_directory.children.append(new_dir)
                new_dir.parent = curr_directory
            else:
                curr_directory.files.append(File(line[1], int(line[0])))
    part_one(root)
    part_two(root)
