# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2021-12-31 22:29:21
import sys
import time


def counter(number):
    for i in range(number):
        sys.stdout.write('\r' + str(i) + ' Reza ' + str(i))
        time.sleep(0.5)
        sys.stdout.flush()
    print()


sys.stdout.write('Hello')
counter(5)
print('Done')
