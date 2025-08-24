"""Created on Mon May 31 22:52:50 2021

@author: Mohammad
"""


def ten2sixteen(number):
    number = int(number)
    sixteen = ''
    while True:
        kharj = number // 16
        baghi = number % 16
        if baghi == 10:
            sixteen = 'A' + sixteen
        elif baghi == 11:
            sixteen = 'B' + sixteen
        elif baghi == 12:
            sixteen = 'C' + sixteen
        elif baghi == 13:
            sixteen = 'D' + sixteen
        elif baghi == 14:
            sixteen = 'E' + sixteen
        elif baghi == 15:
            sixteen = 'F' + sixteen
        else:
            sixteen = str(baghi) + sixteen
        number = kharj
        if not number:
            break
    return sixteen


def rgb2hex(rgb: str):
    rgb = rgb.split()

    red = ten2sixteen(rgb[0])
    red = red if len(red) == 2 else '0' + red

    green = ten2sixteen(rgb[1])
    green = green if len(green) == 2 else '0' + green

    blue = ten2sixteen(rgb[2])
    blue = blue if len(blue) == 2 else '0' + blue

    return '#' + red + green + blue


print(rgb2hex('11 22 33'))

# Edited on Fri Dec 31 23:03:00 2021
