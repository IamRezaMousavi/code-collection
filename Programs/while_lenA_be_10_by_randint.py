"""Created on Tue Apr 13 01:31:47 2021

@author: Mohammad
"""

from random import randint

a = set()
level = 1

while len(a) != 10:
    # while len(a) == 10 by randint
    rand = randint(1, 10)
    a.add(rand)
    print(f'a in {level} level: ', a)
    level += 1

# Edited on Sat May 29 20:38:00 2021
# Edited on Mon May 31 17:10:00 2021
