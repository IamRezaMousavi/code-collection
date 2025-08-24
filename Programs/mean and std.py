# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-02-11 01:53:48

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players) / len(players)
print(f'Mean: {mean}')

std = (sum([(player - mean) ** 2 for player in players]) / len(players)) ** 0.5
print(f'STD: {std}')

for player in players:
    if mean - std < player < mean + std:
        print(player)
