import pandas as pd
from Library import *

pd.set_option("display.max_columns", 101)
with open(PATH_TO_INPUTS + "/input3.txt", "r") as f:
    data = f.readlines()
data = [list(element.replace('\n', '')) for element in data]


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART ONE ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_one(puzzle):
    # get index (so it is the exactly this number) of the value which occurs the most in each column
    result_list = pd.DataFrame(puzzle).apply(lambda x: x.value_counts().idxmax()).values
    # just make conversion from binary to decimal
    gamma = int("".join(result_list), 2)
    # change all 1 to 0 and all 0 to 1
    epsilon = int("".join(list(map(lambda x: "0" if x == "1" else "1", result_list))), 2)
    print(gamma * epsilon)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- PART TWO ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def part_two(puzzle):
    df = pd.DataFrame(puzzle)
    N = df.columns.shape[0]

    def oxygen_bit(dataframe, n):
        """
        Get dominating bit, while draws are returning 1
        :param dataframe: dataframe with data to work on
        :param n: in which column do we want to find dominating bit
        :return: dominating bit
        """
        column = dataframe[n]
        return int(column.value_counts().idxmax()) if column.value_counts().max() > column.value_counts().min() else 1

    def co2_bit(dataframe, n):
        """
        Get non-dominating bit, while draws are returning 0
        :param dataframe: dataframe with data to work on
        :param n: in which column do we want to find non-dominating bit
        :return: non-dominating bit
        """
        column = dataframe[n]
        return int(column.value_counts().idxmin()) if column.value_counts().max() > column.value_counts().min() else 0

    # make copies, because we will be deleting rows that do not meet the requirements
    df_oxygen = df.copy()
    df_co2 = df.copy()

    # step 0
    # add tmp columns which will store information about previous iteration
    curr_oxygen_bit = oxygen_bit(df_oxygen, 0)
    curr_co2_bit = co2_bit(df_co2, 0)

    # lambda: return 1 if given bit is equal to dominant bit for oxygen or non-dominant bit for co2. Otherwise return 0
    df_oxygen['tmp_oxygen'] = df_oxygen[0].apply(lambda x: 1 if int(x) == curr_oxygen_bit else 0)
    df_co2['tmp_co2'] = df_co2[0].apply(lambda x: 1 if int(x) == curr_co2_bit else 0)

    # delete rows that do not meet the requirements
    df_oxygen = df_oxygen[df_oxygen['tmp_oxygen'] == 1]
    df_co2 = df_co2[df_co2['tmp_co2'] == 1]

    # do the same step as above, but repeat it N-1 times
    for i in range(1, N):
        curr_oxygen_bit = oxygen_bit(df_oxygen, i)
        curr_co2_bit = co2_bit(df_co2, i)
        if df_oxygen['tmp_oxygen'].sum() != 1:
            df_oxygen['tmp_oxygen'] = df_oxygen[i].apply(lambda x: 1 if int(x) == curr_oxygen_bit else 0)
            df_oxygen = df_oxygen[df_oxygen['tmp_oxygen'] == 1]
        if df_co2['tmp_co2'].sum() != 1:
            df_co2['tmp_co2'] = (df_co2[i].apply(lambda x: 1 if int(x) == curr_co2_bit else 0))
            df_co2 = df_co2[df_co2['tmp_co2'] == 1]
    # we do not need these columns anymore. The answer lays in the other columns
    df_oxygen.drop(columns='tmp_oxygen', inplace=True)
    df_co2.drop(columns='tmp_co2', inplace=True)

    # translate from binary to decimal to get the answer
    result_list_oxygen = df_oxygen.values[0]
    result_list_co2 = df_co2.values[0]
    gamma = int("".join(result_list_oxygen), 2)
    epsilon = int("".join(result_list_co2), 2)
    print(gamma * epsilon)
