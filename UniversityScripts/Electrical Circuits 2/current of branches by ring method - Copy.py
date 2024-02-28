# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:59:53 2021

@author: Mohammad
"""

import numpy as np
import math
import cmath
import sympy as sp

def rect(r, teta):
    znumber = cmath.rect(r, math.radians(teta))
    return complex(round(znumber.real, 4), round(znumber.imag, 4))

b = np.matrix([[1, 0, 1],
               [0, 1, -1]
               ])
z = np.matrix([[2,   0,    0],
               [0,  10,    0],
               [0,   0,   20]
               ])

zi = b * z * b.T

print("zi = b * z * b.T:", zi, "===================", sep="\n")

r, teta = 10*math.sqrt(2), 45
v1 = rect(r, teta)
i2 = sp.Symbol("i2")

vs = np.matrix([[-20],
               [4*i2],
               [0]
               ])
print("vs = ", vs, "===================", sep="\n")

js = np.matrix([[0],
               [0],
               [0]
               ])
print("js = ", js, "===================", sep="\n")

es = -b*vs + b*z*js
print("es = -b*vs + b*z*js :", es, "===================", sep="\n")

i = np.linalg.inv(zi) * es
print("i = inv(zi) * es :", i, "===================", sep="\n")

print(f"i1 = {i[0]}\ni2 = {i[1]}\ni3 = i1 - i2 = {i[0] - i[1]}")

