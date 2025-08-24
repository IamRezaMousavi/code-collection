# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:20:50
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 03:18:55

import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')
a = (x + y) ** 2

sp.expand(a)  # گسترش

a.evalf(subs={x: 1, y: 2})  # جایگذاری

sp.simplify((x + x + y) / x)  # ساده‌سازی

sp.limit(sp.sin(x) / x, x, 0)  # حد

sp.limit(1 / x, x, sp.oo)  # حد بینهایت

sp.diff(sp.sin(x), x)  # مشتق

sp.integrate(sp.sin(x), x)  # انتگرال نامعین

sp.integrate(sp.sin(x), (x, -sp.pi / 2, sp.pi / 2))  # انتگرال معین

sp.series(sp.sin(x), x)  # بسط توابع

sp.solve(x**2 + 1, x)  # حل معادله

sp.solve([x**2 + y**2, x - y], [x, y])

f = x**4 + 3 * x**2
sp.factor(f)  # فاکتورگیری

"""
f = sp.Symbol("f", cls=sp.Function)
sp.dsolve(
        f(x).diff(x, x) + f(x),
        f(x)
    ) #معادله دیفرانسیل
"""

print('Done')
