PATH = "/home/hubert/PycharmProjects/AdventOfCode2021"
PATH_TO_CODES = PATH + "/Codes"
PATH_TO_INPUTS = PATH + "/Inputs"

PATH_2 = "/Users/hubertgiza/PycharmProjects/Aoc2021"
PATH_TO_CODES_2 = PATH_2 + "/Codes"
PATH_TO_INPUTS_2 = PATH_2 + "/Inputs"


class Day4Parser:
    def __init__(self, file):
        with open(PATH_TO_INPUTS + '/' + file, 'r') as f:
            self.data = f.read()
        self.data = self.data.replace('\n\n', ';')
        self.numbers = None
        self.boards = None
        self.board_size = 5

    def parse_numbers(self):
        i = 0
        while self.data[i] != ';':
            i += 1
        self.numbers = self.data[:i].split(',')
        self.numbers = list(map(int, self.numbers))
        self.data = self.data[i + 1:]

    def parse_boards(self):
        N = self.data.count(';') + 1
        self.boards = [[[0 for _ in range(self.board_size)] for _ in range(self.board_size)] for _ in range(N)]
        self.data = self.data.split(';')
        self.data = [board.replace('\n', ' ').replace('   ', ' ').replace('  ', ' ') for board in self.data]
        self.data = [board.split(' ') for board in self.data]
        for i in range(N):
            if self.data[i][0] == '':
                self.data[i].pop(0)
        self.data = [list(map(int, board)) for board in self.data]
        for n in range(N):
            for i in range(self.board_size):
                for j in range(self.board_size):
                    self.boards[n][i][j] = self.data[n][i * 5 + j]
