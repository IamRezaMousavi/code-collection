"""Created on Tue Aug 10 15:45:46 2021

@author: Mohammad
"""


class NumericalDifferentation:
    def __init__(self, func):
        # get function for different
        self.func = func

    def pishrof1x2(self, x, h):
        f = self.func
        return (f(x + h) - f(x)) / h

    def pishrof2x3(self, x, h):
        f = self.func
        return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h**2)

    def pishrof1x3(self, x, h):
        f = self.func
        return (-f(x + 2 * h) + 4 * f(x + h) - 3 * f(x)) / (2 * h)

    def pasrof1x2(self, x, h):
        f = self.func
        return (f(x) - f(x - h)) / h

    def pasrof2x3(self, x, h):
        f = self.func
        return (f(x - 2 * h) - 2 * f(x - h) + f(x)) / (h**2)

    def pasrof1x3(self, x, h):
        f = self.func
        return (f(x - 2 * h) - 4 * f(x - h) + 3 * f(x)) / (2 * h)

    def markazif1x2(self, x, h):
        f = self.func
        return (f(x + h) - f(x - h)) / (2 * h)

    def richardson(self, x, h):
        f = self.markazif1x2
        fh = f(x, h)
        fh2 = f(x, h / 2)
        return (((2**2) * fh2) - fh) / ((2**2) - 1)


# =====================================================
if __name__ == '__main__':

    def v(t):
        import math

        ln = (14 * (10**4)) / ((14 * (10**4)) - (2100 * t))
        return (2000 * math.log(ln)) - (9.8 * t)

    def f(x):
        if x == 1:
            return 0
        elif x == 2:
            return 1.3863
        elif x == 3:
            return 3.2958

    def x(t):
        if t == 0:
            return 0
        elif t == 0.5:
            return 3.65
        elif t == 1:
            return 6.8
        elif t == 1.5:
            return 9.9
        elif t == 2:
            return 12.15

    def xln(x):
        x = round(x, 2)
        if x == 1.2:
            return 0.2188
        elif x == 1.4:
            return 0.4711
        elif x == 1.6:
            return 0.7520
        elif x == 1.8:
            return 1.0580
        elif x == 2:
            return 1.3863

    nd1 = NumericalDifferentation(xln)
    print(nd1.richardson(1.6, 0.4))
