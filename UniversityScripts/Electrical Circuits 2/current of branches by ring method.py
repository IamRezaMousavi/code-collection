# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:59:53 2021

@author: Mohammad
"""

import numpy as np
import sympy as sp
import math
import cmath

def rect(r, teta):
    znumber = cmath.rect(r, math.radians(teta))
    return complex(round(znumber.real, 4), round(znumber.imag, 4))

b = np.matrix([[1, 0, 1],
               [0, 1, -1]
               ])
z = np.matrix([[15j, 0, 0],
               [0, -5j, 0],
               [0, 0, 10]
               ])

zi = b * z * b.T

print("zi = b * z * b.T:", zi, "===================", sep="\n")

r, teta = 20, 0
v1 = rect(r, teta)

r, teta = 30, -90
v2 = rect(r, teta)

i2 = sp.Symbol("i2") # برای منابع وابسته

vs = np.matrix([[-v1],
               [v2],
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

