# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:55:14 2021

@author: Mohammad
"""

import cmath
import math

z = (1-1j)
r, teta = cmath.polar(z)
print(f"z = {r} < {math.degrees(teta)}")

print("=======================")

r, teta = 100, 45
z = cmath.rect(r, math.radians(teta))
print(f"z = {z.real} + {z.imag}j")

print("=======================")

zconj = z.conjugate()
print(f"z*: {zconj.real} + {zconj.imag}j")
