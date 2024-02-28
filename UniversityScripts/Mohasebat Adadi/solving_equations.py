# @Author: @IamRezaMousavi
# @Date:   2021-09-22 05:41:44
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2021-11-26 12:29:37


class SolvingEquation:
    def __init__(self, func):
        self.func = func

    def bisection(self, a, b, e):
        a, b = min(a, b), max(a, b)
        func = self.func

        def sign(x):
            if x > 0:
                return 1
            elif x == 0:
                return 0
            return -1

        fa = func(a)
        fb = func(b)
        if sign(fa) * sign(fb) >= 0:
            return 'f(a)*f(b) < 0 not satisfied'
        while (b - a) / 2 > e:
            c = (a + b) / 2
            fc = func(c)
            if fc == 0:
                break
            if sign(fc) * sign(fa) < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        return (a + b) / 2

    def displayBisection(self, a, b, e):
        a, b = min(a, b), max(a, b)
        func = self.func

        def sign(x):
            if x > 0:
                return 1
            elif x == 0:
                return 0
            return -1

        fa = func(a)
        fb = func(b)
        if sign(fa) * sign(fb) >= 0:
            print('f(a)*f(b) < 0 not satisfied')
            return None
        print(
            '\n_____________________________________________________________________________________',
        )
        print(
            '|  n  |      a      |      b      |     Cn      |    f(a)    |   f(Cn)   |  |b-a|/2  |',
        )
        print(
            '_____________________________________________________________________________________',
        )
        n = 0
        en = (b - a) / 2
        while en > e:
            n += 1
            c = (a + b) / 2
            fc = func(c)
            if fc == 0:
                break
            if fc > 0:
                print(
                    '| %3d |   %.5f   |   %.5f   |   %.5f   |  %.5f  |  %.5f  |  %.5f  |'
                    % (n, a, b, c, fa, fc, en),
                )
            else:
                print(
                    '| %3d |   %.5f   |   %.5f   |   %.5f   |  %.5f  | %.5f  |  %.5f  |'
                    % (n, a, b, c, fa, fc, en),
                )
            if sign(fc) * sign(fa) < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            en = (b - a) / 2
        n += 1
        c = (a + b) / 2
        fc = func(c)
        if fc >= 0:
            print(
                '| %3d |   %.5f   |   %.5f   |   %.5f   |  %.5f  |  %.5f  |  %.5f  |'
                % (n, a, b, c, fa, fc, en),
            )
        else:
            print(
                '| %3d |   %.5f   |   %.5f   |   %.5f   |  %.5f  | %.5f  |  %.5f  |'
                % (n, a, b, c, fa, fc, en),
            )
        print(
            '_____________________________________________________________________________________',
        )
        print(f'Answer is {c}\n')
        return c

    def fixedPoint(self, x0, k):
        func = self.func
        x = [x0]
        for i in range(1, k + 1):
            x.append(func(x[i - 1]))
        return x[-1]

    def secant(self, a, b, e):
        from math import log10

        log_error = abs(int(log10(e)))
        f = self.func
        formole = lambda xi, xii: xi - (f(xi) * (xi - xii)) / (f(xi) - f(xii))
        x = [a, b]
        x_next = formole(a, b)
        x.append(x_next)
        while abs(f(x_next)) >= e:
            x_next = formole(x[-1], x[-2])
            x.append(round(x_next, log_error))
        print(' ------------------------ ')
        print('|  i  |        xi        |')
        print('|------------------------|')
        for i, xi in enumerate(x):
            print('|%5d| %.14f |' % (i + 1, xi))
        print(' ------------------------ ')
        print(f'Answer is {x[-1]}')
        return x[-1]

    def falsePosition(self, a, b, e):
        f = self.func
        formole = lambda a, b: (b * f(a) - a * f(b)) / (f(a) - f(b))
        n = 0
        print('-----------------------------------------------------------')
        print('|  n  |    a     |    b    |    c    |   f(a)   |   f(c)  |')
        while True:
            n += 1
            c = formole(a, b)
            if f(c) == 0 or abs(b - a) < e:
                return c
            print('|%5d| %.5f | %.5f | %.5f | %.5f | %.5f |' % (n, a, b, c, f(a), f(b)))
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        print('-----------------------------------------------------------')


f = lambda x: x**3 + x - 1
s = SolvingEquation(f)
print(s.secant(0, 1, 10**-14))

"""
f = lambda x: x**5 + x - 1
a = SolvingEquation(f)
a.displayBisection(0, 1, 10**-3)
"""
"""
from math import sin
f = lambda x: x**2 - 4*sin(x)
a = SolvingEquation(f)
a.displayBisection(1, 2, 10**-4)
"""
"""
f = lambda x: x**2 - 2
a = SolvingEquation(f)
a.displayBisection(1.4, 1.5, 10**-2)
"""
"""
from math import cos
f = lambda x: cos(x) - x
a = SolvingEquation(f)
a.displayBisection(0, 1, 10**-6)
"""
"""
from math import cos
g = lambda x: cos(x)
a = SolvingEquation(g)
print(a.fixedPoint(0, 10))
"""
"""
from math import log
h = lambda x: (log(x)+4) / 2
a = SolvingEquation(h)
print(a.fixedPoint(2.5, 10))
"""
