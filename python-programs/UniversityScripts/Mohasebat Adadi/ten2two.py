"""Created on Thu Jul 22 17:31:32 2021

@author: Mohammad
"""


def dec2bin(number: float, precision: int = 16) -> str:  # precision: fraction digit limit
    integer = int(number)
    fraction = number - integer

    result = ''
    if integer == 0:
        result = '0'
    while integer:
        result = str(integer % 2) + result
        integer //= 2

    if fraction == 0:
        return result

    result += '.'
    for _ in range(precision):
        fraction *= 2
        bit = int(fraction)

        result += str(bit)
        fraction -= bit

        if fraction == 0:
            break

    return result


def bin2dec(number: str) -> float:
    integer, *fraction = number.split('.')

    result = 0
    for digit in integer:
        result = result * 2 + int(digit)

    divisor = 2
    for digit in fraction[0] if fraction else '':
        result += int(digit) / divisor  # int(digit) * (2 ** -(i + 1))
        divisor *= 2

    return result


print(bin2dec('1010.101'))  # 10.625
print(bin2dec('1101.01'))  # 13.25
print(bin2dec('101'))  # 5.0
print(bin2dec('0.101'))  # 0.625

print(dec2bin(10.625))  # 1010.101
print(dec2bin(13.25))  # 1101.01
print(dec2bin(0.625))  # 0.101
print(dec2bin(5))  # 101
