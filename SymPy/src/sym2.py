# @Author: @IamRezaMousavi
# @Date:   2022-02-11 02:54:08
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 03:28:37


import sympy as sp

x, y = sp.symbols('x y')
print(x, y)

sp.sqrt(8)  # 2*sqrt(2)

# sp.init_printing(use_unicode=True) پرینت زیبا
sp.diff(sp.sin(x) * sp.exp(x), x)  # مشتق

sp.integrate(sp.sin(x**2), (x, -sp.oo, sp.oo))  # انتگرال

sp.limit(sp.sin(x) / x, x, 0)  # حد

sp.solve(x**2 - 2, x)  # حل معادله

t = sp.symbols('t')
y = sp.Function('y')

sp.dsolve(sp.Eq(y(t).diff(t, t) - y(t), sp.exp(t)), y(t))  # معادلات دیفرانسیل

sp.Matrix([[1, 2], [2, 2]]).eigenvals()  # مقدارهای ویژه ماتریس

# print("\t", latex(Integral(cos(x)**2, (x, 0, pi)))) #تبدیل به لاتکس LaTeX

print('Done')
