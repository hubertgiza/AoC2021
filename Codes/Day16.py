import numpy as np
from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input16.txt", "r") as f:
    data = f.readlines()
with open(PATH_TO_INPUTS + "/hex2bin.txt", "r") as f:
    hex2bin = f.readlines()

data = [element.replace('\n', '') for element in data]
hex2bin = [element.replace('\n', '').replace(' ', '').split('=') for element in hex2bin]
hex2bin = {element[0]: element[1] for element in hex2bin}

functions_dict = {0: np.sum,
                  1: np.product,
                  2: np.min,
                  3: np.max,
                  5: lambda x: 1 if x[0] > x[1] else 0,
                  6: lambda x: 1 if x[0] < x[1] else 0,
                  7: lambda x: 1 if x[0] == x[1] else 0
                  }


def day_one():
    def parse_bin_message(string):
        if len(string) < 11:
            return 0
        version = int(string[:3], 2)
        message_type = int(string[3:6], 2)

        if message_type == 4:
            string = string[6:]
            i = 0
            while string[5 * i] != '0':
                i += 1
            return version + parse_bin_message(string[5 * (i + 1):])

        length_type = string[6]
        if length_type == '0':
            return version + parse_bin_message(string[22:])
        else:
            return version + parse_bin_message(string[18:])

    for example in data:
        bin_data = "".join([hex2bin[char] for char in example])
        print(parse_bin_message(bin_data))


def parse(full_string):
    string = full_string

    def parse_bin_message():
        nonlocal string
        if len(string) < 11:
            return []
        message_type = int(string[3:6], 2)
        if message_type == 4:
            string = string[6:]
            value = ""
            while string[0] != '0':
                value += string[1:5]
                string = string[5:]
            value += string[1:5]
            value = int(value, 2)
            string = string[5:]
            return [value]
        length_type = string[6]
        if length_type == '0':
            sub_packets_length = int(string[7:22], 2)
            string = string[22:]

            curr_len = len(string)
            res = []
            if message_type in [5, 6, 7]:
                for _ in range(2):
                    res += parse_bin_message()
                return [functions_dict[message_type](res)]
            while curr_len - len(string) < sub_packets_length:
                res += parse_bin_message()
            return [functions_dict[message_type](res)]
        else:
            val = int(string[7:18], 2)
            string = string[18:]
            res = []
            for _ in range(val):
                res += parse_bin_message()
            return [functions_dict[message_type](res)]

    return parse_bin_message()


for example in data:
    bin_data = "".join([hex2bin[char] for char in example])
    print(parse(bin_data))
