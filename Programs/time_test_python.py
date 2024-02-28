"""Created on Wed Apr  7 20:52:45 2021

@author: Mohammad
"""

from datetime import datetime

start = datetime.now()
for i in range(1000000):
    print(i)

print(datetime.now() - start)
input()
