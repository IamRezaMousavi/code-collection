"""Created on Mon May 31 22:52:50 2021

@author: Mohammad
"""


def ten2sixteen(number: int) -> str:
    result = ''
    while True:
        digit = number % 16
        if digit == 10:
            result = 'A' + result
        elif digit == 11:
            result = 'B' + result
        elif digit == 12:
            result = 'C' + result
        elif digit == 13:
            result = 'D' + result
        elif digit == 14:
            result = 'E' + result
        elif digit == 15:
            result = 'F' + result
        else:
            result = str(digit) + result
        number //= 16
        if number == 0:
            break
    return result.zfill(2)


def rgb2hex(rgb: list[int]) -> str:
    if len(rgb) != 3:
        raise ValueError('rgb lenght must be exact 3')

    r, g, b = rgb
    return '#' + ten2sixteen(r) + ten2sixteen(g) + ten2sixteen(b)


print(rgb2hex([255, 128, 255]))

# Edited on Fri Dec 31 23:03:00 2021
# Edited on Tue Nov 03 16:07:00 2026
