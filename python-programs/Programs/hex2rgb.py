"""Created on Fri Apr 30 02:50:17 2021

@author: Mohammad
"""


# Horner's method
def sixteen2ten(int16: str) -> int:
    hex_str = int16.strip().upper()
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    result = 0
    for ch in hex_str:
        if '0' <= ch <= '9':
            digit = ord(ch) - ord('0')
        elif 'A' <= ch <= 'F':
            digit = ord(ch) - ord('A') + 10
        else:
            raise ValueError(f'invalid digit: {ch}')
        result = result * 16 + digit
    return result


def hex2rgb(code: str) -> tuple[int, int, int]:
    code = code.strip().upper().lstrip('#')

    if len(code) != 6:
        raise ValueError('hex code must be 6 chars')

    r = sixteen2ten(code[0:2])
    g = sixteen2ten(code[2:4])
    b = sixteen2ten(code[4:6])
    return r, g, b


def main():
    while True:
        print('=======================================')
        print('Hex to RGB')
        print('=======================================')
        code = input('Enter Hex Code: #')

        try:
            rgb = hex2rgb(code)
            print(f'result: RGB{rgb}')
        except ValueError as e:
            print(f'error: {e}')

        answer = input('Are you want to contine (y/n)?').strip().lower()
        if answer in ('n', 'no'):
            print('bye!')
            break


if __name__ == '__main__':
    main()

# Edited on Sat May 29 21:18:00 2021
# Edited on Fri Dec 31 22:43:00 2021
# Edited on Fri Feb 11 01:52:00 2022
# Edited on Tue Nov 03 15:55:00 2026
