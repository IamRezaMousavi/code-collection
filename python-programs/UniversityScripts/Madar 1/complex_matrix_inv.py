"""Created on Sat Jun 19 20:33:50 2021

@author: Mohammad
"""

import cmath

import numpy as np
import sympy as sp

i1 = sp.Symbol('i1')
i2 = sp.Symbol('i2')

a1 = -150 + (1 + 2j) * i1 + (12 - 16j) * (i1 - i2)
a1 = sp.simplify(a1)

a2 = (12 - 16j) * (i2 - i1) + (1 + 3j) * i2 + 39 * (i1 - i2)
a2 = sp.simplify(a2)

print('===================')
print('A1: ', a1)
print('A2: ', a2)
print('===================')

a = np.matrix([[(13 - 14j), (-12 + 16j)], [(27 + 16j), -(26 + 13j)]])
b = np.matrix([[150], [0]])

x = np.linalg.inv(a) * b
print(x)
print('===================')

r, teta = cmath.polar(x[0])
print(f'x1 = {r} < {np.degrees(teta)}')

r, teta = cmath.polar(x[1])
print(f'x2 = {r} < {np.degrees(teta)}')
print('===================')
