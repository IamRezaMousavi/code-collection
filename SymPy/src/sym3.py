# @Author: @IamRezaMousavi
# @Date:   2022-02-11 02:55:27
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 03:35:38

import sympy as sp

x = sp.symbols('x')
expr = x + 1
expr.subs(x, 2)

y = sp.Eq(x + 1, 4)  # x+1 = 4

print(sp.solve(y))

a = (x + 1) ** 2
b = x**2 + 2 * x + 1

sp.simplify(a - b)  # ساده‌سازی

c = x**2 - 2 * x + 1
sp.simplify(a - c)

a = sp.cos(x) ** 2 - sp.sin(x) ** 2
b = sp.cos(2 * x)

a.equals(b)
# چک کردن مساوی با چک کردن اعداد تصادفی

x, y, z = sp.symbols('x y z')
expr = x**3 + 4 * x * y - z
expr.subs([(x, 2), (y, 4), (z, 0)])


str_expr = 'x**2 + 3*x - 1/2'
expr = sp.sympify(str_expr)
print(expr)
print(expr.subs(x, 2))


expr = sp.sqrt(8)
expr.evalf()  # defult 15 digit
sp.pi.evalf(50)

expr = sp.cos(2 * x)
expr.evalf(subs={x: 2.4})

one = sp.cos(1) ** 2 + sp.sin(1) ** 2

(one - 1).evalf()
# -0.e-124
(one - 1).evalf(chop=True)
# 0

print('Done')
