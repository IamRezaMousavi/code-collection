# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2021-12-31 23:04:36

n = int(input('Please type a number:'))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 != 0:
        print('Solo')
    elif i % 3 != 0 and i % 5 == 0:
        print('Learn')
    elif i % 3 == 0 and i % 5 == 0:
        print('SoloLearn')
    else:
        print(i)
input()
