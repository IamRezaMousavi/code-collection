"""Created on Thu Jul  1 20:09:31 2021

@author: Mohammad
"""

import cmath
import math

i_max, teta_i = 2, -20  # cmath.polar()
v_max, teta_v = 100, 10  # v_max = v_rms * math.sqrt(2)

i = cmath.rect(i_max, math.radians(teta_i))
v = cmath.rect(v_max, math.radians(teta_v))

print('=====================================')

p = 0.5 * v_max * i_max * math.cos(math.radians(teta_v - teta_i))
print(f'P (Active): {p} [W]')

pf = math.cos(math.radians(teta_v - teta_i))
print(f'(PF: cos({teta_v - teta_i}) = {pf})')

q = 0.5 * v_max * i_max * math.sin(math.radians(teta_v - teta_i))
print(f'Q (Reactive): {q} [VAr]')

print('=====================================')

s = 0.5 * v * i.conjugate()
print(f'S (Mokhtalet): {s.real}, {s.imag} [VA]')

sz = 0.5 * v_max * i_max
print(f'|S| (Zaheri): {sz} [VA]')

print('=====================================')
