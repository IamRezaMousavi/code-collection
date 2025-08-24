"""Created on Wed Jun 16 19:59:32 2021

@author: Mohammad
"""


def romberg(func, start, stop, n):
    import math

    import numpy as np

    n2 = int(math.log2(n))
    T = np.zeros((n2 + 1, n2 + 1))
    for i in range(n2 + 1):
        t = 0.0
        h = (stop - start) / 2**i
        t = [func(j) for j in np.arange(start, stop + h / 2, h)]
        T[i][0] = (h / 2) * (sum(t) + sum(t[1 : len(t) - 1]))
    for i in range(1, n2 + 1):
        for j in range(1, n2 + 1):
            if j < i:
                continue
            T[j][i] = ((4**i) * T[j][i - 1] - T[j - 1][i - 1]) / (-1 + 4**i)
    return T


def f(x):
    if x == 0:
        return 1
    elif x == 0.25:
        return 0.9689
    elif x == 0.5:
        return 0.8776
    elif x == 0.75:
        return 0.7317
    elif x == 1:
        return 0.5403


func = lambda x: 1 / (1 + x**3)
import math

ff = lambda x: math.sin(x)
t = romberg(ff, 0, math.pi, 2**7)
