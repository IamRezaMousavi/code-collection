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

q = np.matrix([[1, 1, 0],
               [-1, 0, 1]
               ])
y = np.matrix([[0.8, 0, 0],
               [0, 0.2, 0],
               [0, 0, 0.3]
               ])
print("y: ", y, "===================", sep="\n")

yq = q * y * q.T

print("yq = q * y * q.T:", yq, "===================", sep="\n")

vs = np.matrix([[0],
               [0],
               [0]
               ])
print("vs = ", vs, "===================", sep="\n")

r, teta = 20, 0
v1 = rect(r, teta)

r, teta = 30, -90
v2 = rect(r, teta)

e2 = sp.Symbol("e2") # برای منابع وابسته

js = np.matrix([[0],
               [-5],
               [4*0.2*e2]
               ])
print("js = ", js, "===================", sep="\n")

i_s = -q*js + q*y*vs
print("i_s = -q*js + q*y*vs :", i_s, "===================", sep="\n")

e = np.linalg.inv(yq) * i_s
print("e = inv(yq) * i_s :", e, "===================", sep="\n")
