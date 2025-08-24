"""Created on Wed May 26 16:38:56 2021

@author: Mohammad
"""


def integrate(f, start, stop, ndigits=5):
    n = 10 ** (ndigits)

    h = (stop - start) / n

    x = [start + i * h for i in range(n + 1)]

    integ = sum([f(x[i]) for i in range(1, len(x) - 1)])

    integ = (h / 2) * (f(start) + (2 * integ) + f(stop))

    return round(integ, ndigits)


if __name__ == '__main__':
    from math import cos

    x = lambda x: cos(x)
    print(integrate(x, 1, 5, 5))

# Edited on Sun May 30 17:24:58 2021
# Edited on Sun May 30 18:56:34 2021
# Edited on Tue Jun  1 00:06:59 2021
# Edited on Fri Feb 11 01:41:00 2022
