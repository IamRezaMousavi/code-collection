"""Created on Tue Aug 10 15:30:37 2021

@author: Mohammad
"""

from fractions import Fraction


class NumericalIntegration:
    def __init__(self, func):
        # take function for integration
        self.func = func

    def trapezoid(self, start, stop, n):
        # ghaede zozanaghe ei
        h = (stop - start) / n
        x = [start + x * h for x in range(n + 1)]
        y = [self.func(x) for x in x]
        T = (h / 2) * (y[0] + 2 * (sum([y[i] for i in range(1, n)])) + y[-1])
        return T

    def displayTrapezoid(self, start, stop, n):
        # ghaede zozanaghe ei
        h = (stop - start) / n
        x = [Fraction(str(start + x * h)) for x in range(n + 1)]
        print(f'X{n} = {x}')
        y = [Fraction(str(self.func(x))) for x in x]
        print(f'Y{n} = {y}')
        T = (h / 2) * (y[0] + 2 * (sum([y[i] for i in range(1, n)])) + y[-1])
        print(f'T{n} = {Fraction(h)!r} * [{Fraction(1, 2)!r}*{y[0]!r}', end='')
        for item in y[1:-1]:
            print(f' + {item!r}', end='')
        print(f' + {Fraction(1, 2)!r}*{y[-1]!r})] = \n= {T}')
        return T

    def midpoint(self, start, stop, n):
        # ravesh noghte miani
        h = (stop - start) / n
        m_n = [start + (i - 0.5) * h for i in range(1, n + 1)]
        M_n = h * sum([self.func(i) for i in m_n])
        return M_n

    def simpson(self, start, stop, n):
        h = (stop - start) / n
        x = [start + i * h for i in range(n + 1)]
        y = [self.func(i) for i in x]
        s = 0.0
        for i in range(len(y)):
            if i == 0 or i == len(y) - 1:
                s += y[i]
            elif i % 2 == 1:
                s += 4 * y[i]
            elif i % 2 == 0:
                s += 2 * y[i]
        S_n = (h / 3) * s
        return S_n

    def romberg(self, start, stop, n):
        import numpy as np

        n2 = int(np.log2(n))
        T = np.zeros((n2 + 1, n2 + 1))
        for i in range(n2 + 1):
            h = (stop - start) / (2**i)
            t = [self.func(j) for j in np.arange(start, stop + h / 2, h)]
            T[i][0] = (h / 2) * (sum(t) + sum(t[1 : len(t) - 1]))
        for i in range(1, n2 + 1):
            for j in range(1, n2 + 1):
                if j < i:
                    continue
                T[j][i] = ((4**i) * T[j][i - 1] - T[j - 1][i - 1]) / (-1 + 4**i)
        return T


if __name__ == '__main__':
    func1 = lambda x: 1 / x
    ni1 = NumericalIntegration(func1)
    print(ni1.displayTrapezoid(1, 2, 16), '\n', ni1.trapezoid(1, 2, 16))
