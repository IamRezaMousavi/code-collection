"""Created on Fri Apr 30 02:50:17 2021

@author: Mohammad
"""


def sixteen2ten(int16):
    int16 = list(int16.upper())
    for index in range(len(int16)):
        if int16[index] == 'A':
            int16[index] = 10
        elif int16[index] == 'B':
            int16[index] = 11
        elif int16[index] == 'C':
            int16[index] = 12
        elif int16[index] == 'D':
            int16[index] = 13
        elif int16[index] == 'E':
            int16[index] = 14
        elif int16[index] == 'F':
            int16[index] = 15
        else:
            int16[index] = int(int16[index])
    for j in range(-1, -(len(int16) + 1), -1):
        int16[j] *= 16 ** (-j - 1)
    int10 = sum(int16)
    return int10


def hex2rgb(code):
    code = list(code.upper())  # upper for a -> A and other
    red1 = code[0] + '0'
    red2 = code[1]

    green1 = code[2] + '0'
    green2 = code[3]

    blue1 = code[4] + '0'
    blue2 = code[5]

    red1 = sixteen2ten(red1)
    red2 = sixteen2ten(red2)

    green1 = sixteen2ten(green1)
    green2 = sixteen2ten(green2)

    blue1 = sixteen2ten(blue1)
    blue2 = sixteen2ten(blue2)

    red = red1 + red2
    green = green1 + green2
    blue = blue1 + blue2

    return (red, green, blue)


while True:
    print('=======================================')
    print('Hex to RGB')
    print('=======================================')
    code = input('Enter Hex Code: #')

    if len(code) == 6:
        if code:
            print('Hex2RGB:', hex2rgb(code))
    else:
        print('\nERROR')
        print('Just Enter 6 Character.')

    answer = input('Are you want to contine (y/n)?')
    if answer == 'n':
        break

# Edited on Sat May 29 21:18:00 2021
# Edited on Fri Dec 31 22:43:00 2021
# Edited on Fri Feb 11 01:52:00 2022
