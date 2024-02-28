# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2021-09-29 03:22:32
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2021-09-29 04:43:59


class MyClass:
    def __init__(self, func):
        self.func = func
    def falsePosition(self, a, b, e):
        f = self.func
        formole = lambda a, b: (b*f(a)-a*f(b)) / (f(a)-f(b))
        n = 0
        print("-----------------------------------------------------------")
        print("|  n  |    a     |    b    |    c    |   f(a)   |   f(c)  |")
        while True:
            n += 1
            c = formole(a, b)
            if f(c) == 0 or abs(b-a) < e:
                return c
            print("|%5d| %.5f | %.5f | %.5f | %.5f | %.5f |"%(n, a, b, c, f(a), f(b)))
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
        print("-----------------------------------------------------------")

f = lambda x: x**2 - 2*x**2 + (3/2)*x
s = MyClass(f)
print(s.falsePosition(-1, 1, 0.01))
