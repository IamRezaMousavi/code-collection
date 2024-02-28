# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:30:37 2021

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
        x = [start + x*h for x in range(n+1)]
        y = [self.func(x) for x in x]
        T = (h/2) * (y[0] + 2*(sum([y[i] for i in range(1,n)])) + y[-1])
        return T
    def displayTrapezoid(self, start, stop, Tn):
        # ghaede zozanaghe ei
        n = Tn
        h = (stop - start) / n
        x = [Fraction(str(start + x*h)) for x in range(n+1)]
        print(f"X{n} = {x}")
        y = [Fraction(str(self.func(x))) for x in x]
        print(f"Y{n} = {y}")
        T = (h/2) * (y[0] + 2*(sum([y[i] for i in range(1,n)])) + y[-1])
        print(f"T{n} = {repr(Fraction(h))} * [{repr(Fraction(1, 2))}*{repr(y[0])}", end="")
        for item in y[1:-1]:
                print(f" + {repr(item)}", end="")
        print(f" + {repr(Fraction(1, 2))}*{repr(y[-1])})] = \n= {T}")
        return T

if __name__ == "__main__":
    func1 = lambda x: 1/x
    ni1 = NumericalIntegration(func1)
    print(ni1.displayTrapezoid(1, 2, 16) == ni1.trapezoid(1, 2, 16))
