"""Created on Tue Apr  6 18:21:13 2021

@author: Mohammad
"""

from datetime import datetime

start = datetime.now()

for i in range(1000000):
    print(i)

print('Zaman Ejra: ', datetime.now() - start)
input()
