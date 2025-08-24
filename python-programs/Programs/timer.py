# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2021-12-31 23:06:33

from time import sleep


def timer(seconds):
    for i in range(seconds, -1, -1):
        print(i)
        sleep(1)


seconds = int(input('Please type how many second(s) you want: '))
timer(seconds)

# Edited on Sat May 29 20:22:00 2021
