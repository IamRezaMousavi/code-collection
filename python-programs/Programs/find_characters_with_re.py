"""Created on Thu May 27 23:55:20 2021

@author: Mohammad
"""

import re

words = 'The rain in Spain 123456 Kilo'

# Find All Lower Characters Between "a" to "m"
x = re.findall('[a-m]', words)
print(x)

x = re.findall('in', words)
print(x)

# Find Numbers
x = re.findall(r'\d', words)
print(x)
