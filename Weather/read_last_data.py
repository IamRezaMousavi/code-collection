"""Created on Sat May 15 21:37:10 2021

@author: Mohammad
"""

import json
from pprint import pprint as pp

with open('Data.txt') as r:
    newdata = r.readlines()
    print('Read is Seccessful.')

newdata2 = json.loads(newdata[-1])
pp(newdata2)
