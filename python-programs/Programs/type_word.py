"""Created on Sun Apr 18 21:33:30 2021

@author: Mohammad
"""

import os
import time


def clearPage():
    os.system(['clear', 'cls'][os.name == 'nt'])


def typeWord(word):
    temp = ''
    for ch in word:
        temp += ch
        yield temp


clearPage()
word = 'Reza'
for i in typeWord(word):
    print(i)
    time.sleep(1)
    clearPage()
print()

# Edited on Sat May 29 20:14:00 2021
