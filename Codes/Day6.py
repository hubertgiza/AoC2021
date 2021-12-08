import numpy as np

from Library import PATH_TO_INPUTS

with open(PATH_TO_INPUTS + "/input6.txt", "r") as f:
    data = f.readlines()

data = list(map(int, data[0].split(',')))
fish = [0] * 9
for i in range(len(data)):
    fish[data[i]] += 1

days = 256
for i in range(days):
    fish_to_add = fish[0]
    fish[0] = 0
    for i in range(1, len(fish)):
        fish[i - 1] = fish[i]
        fish[i] = 0
    fish[8] = fish_to_add
    fish[6] += fish_to_add

print(sum(fish))
