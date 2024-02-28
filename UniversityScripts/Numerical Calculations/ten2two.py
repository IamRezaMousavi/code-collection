"""Created on Thu Jul 22 17:31:32 2021

@author: Mohammad
"""


def ten2two(number):
    number = [int(i) for i in str(number).split('.')]
    ans1 = ''
    while number[0] >= 2:
        ans1 = str(number[0] % 2) + ans1
        number[0] //= 2
    ans1 = str(number[0]) + ans1
    ans2 = ''
    if len(number) == 2:
        number[1] = float('0.' + str(number[1]))
        while number[1] != 0:
            i = int(number[1] * 2)
            ans2 += str(i)
            number[1] = (number[1] * 2) - i
    ans = float(ans1 + '.' + ans2)
    if ans == int(ans):
        return int(ans)
    return ans


def two2ten(number):
    pass
