import numpy as np

from Library import *


class BingoPartOne:
    def __init__(self, boards, board_size):
        self.boards = np.array(boards)
        self.number_of_boards = len(boards)
        self.board_size = board_size
        self.chosen_numbers = np.zeros(shape=(len(self.boards), self.board_size, self.board_size))
        self.rows_scores = np.zeros(shape=(len(self.boards), self.board_size))
        self.columns_scores = np.zeros(shape=(len(self.boards), self.board_size))

    def __repr__(self):
        return "BOARDS:\n" + str(self.boards) + '\n\n' + "CHOSEN NUMBERS:\n" + \
               str(self.chosen_numbers) + '\n\n' + "ROW SCORES:\n" + \
               str(self.rows_scores) + '\n\n' + "COLUMNS SCORES:\n" + \
               str(self.columns_scores)

    def check_winner(self, i):
        """
        Check if i-th board is the winner.
        :param i: boards number
        :return: True if it is the winner. False otherwise
        """
        results_rows = np.where(self.rows_scores[i] == self.board_size)
        results_columns = np.where(self.columns_scores[i] == self.board_size)
        if len(results_rows[0]) != 0:
            return True
        if len(results_columns[0]) != 0:
            return True
        return False

    def calculate_board_score(self, i, x):
        """

        :param i: number of the board
        :param x: called number
        :return: score of the board according to the rules of the puzzle
        """
        sum_of_uncalled_numbers = np.sum(np.where(self.chosen_numbers[i] == 0, self.boards[i], 0))
        return sum_of_uncalled_numbers * x

    def add_number_to_board(self, x, board_number):
        """
        Add number x to the given board and mark it in the chosen_numbers array
        :param x: number to add
        :param board_number: number of board
        :return:
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.boards[board_number][i][j] == x:
                    if self.chosen_numbers[(board_number, i, j)] == 0:
                        self.chosen_numbers[(board_number, i, j)] = 1
                        self.rows_scores[(board_number, i)] += 1
                        self.columns_scores[(board_number, j)] += 1

    def add_number_to_all_boards(self, x):
        """
        Add number x to all of the boards. If the i-th board is the winner, then immediately calculate it score and
        break the loop
        :param x: the number to add
        :return: True if the winner is found. False otherwise
        """
        for i in range(len(self.boards)):
            self.add_number_to_board(x, i)
            if self.check_winner(i):
                print(self.calculate_board_score(i, x))
                return True
        return False


class BingoPartTwo:
    def __init__(self, boards, board_size):
        self.boards = np.array(boards)
        self.number_of_boards = len(boards)
        self.board_size = board_size
        self.chosen_numbers = np.zeros(shape=(len(self.boards), self.board_size, self.board_size))
        self.rows_scores = np.zeros(shape=(len(self.boards), self.board_size))
        self.columns_scores = np.zeros(shape=(len(self.boards), self.board_size))
        self.winners = np.array([0] * len(self.boards))

    def __repr__(self):
        return "BOARDS:\n" + str(self.boards) + '\n\n' + "CHOSEN NUMBERS:\n" + \
               str(self.chosen_numbers) + '\n\n' + "ROW SCORES:\n" + \
               str(self.rows_scores) + '\n\n' + "COLUMNS SCORES:\n" + \
               str(self.columns_scores) + '\n\n' + "WINNERS:\n" + \
               str(self.winners)

    def check_winner(self, i):
        """
        Check if i-th board is the winner.
        :param i: boards number
        :return: True if it is the winner. False otherwise
        """
        results_rows = np.where(self.rows_scores[i] == self.board_size)
        results_columns = np.where(self.columns_scores[i] == self.board_size)
        if len(results_rows[0]) != 0:
            return True
        if len(results_columns[0]) != 0:
            return True
        return False

    def calculate_board_score(self, i, x):
        """
        Calculate score of board x
        :param i: number of the board
        :param x: called number
        :return: score of the board according to the rules of the puzzle
        """
        sum_of_uncalled_numbers = np.sum(np.where(self.chosen_numbers[i] == 0, self.boards[i], 0))
        return sum_of_uncalled_numbers * x

    def add_number_to_board(self, x, board_number):
        """
        Add number x to the given board and mark it in the chosen_numbers array
        :param x: number to add
        :param board_number: number of board
        :return:
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.boards[board_number][i][j] == x:
                    if self.chosen_numbers[(board_number, i, j)] == 0:
                        self.chosen_numbers[(board_number, i, j)] = 1
                        self.rows_scores[(board_number, i)] += 1
                        self.columns_scores[(board_number, j)] += 1

    def add_number_to_all_boards(self, x):
        """
        Add number x to all of the boards. Return True if last winner is found and calculate its score
        :param x: number to add
        :return: True if the last winner is found. False otherwise
        """
        for i in range(len(self.boards)):
            self.add_number_to_board(x, i)
            if self.check_winner(i):
                self.winners[i] = 1
                if np.sum(self.winners) == len(self.boards):
                    print(self.calculate_board_score(i, x))
                    return True
        return False


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one():
    parser = Day4Parser('input4.txt')
    parser.parse_numbers()
    parser.parse_boards()
    game_board = BingoPartOne(parser.boards, parser.board_size)
    for i in range(len(parser.numbers)):
        if game_board.add_number_to_all_boards(parser.numbers[i]):
            break


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two():
    parser = Day4Parser('input4.txt')
    parser.parse_numbers()
    parser.parse_boards()
    game_board = BingoPartTwo(parser.boards, parser.board_size)
    for i in range(len(parser.numbers)):
        if game_board.add_number_to_all_boards(parser.numbers[i]):
            break


part_two()
