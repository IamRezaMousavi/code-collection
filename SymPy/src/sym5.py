# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-02-11 02:57:27
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 02:58:32


expr = 1/x + (3*x/2 - 2)/(x - 4)
print(pretty(expr))
print()
print(pretty(cancel(expr)))
print()


expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
print(pretty(expr))
print(pretty(apart(expr)))

# ساده‌سازی عبارات دارای توابع مثلثاتی
print(pretty(trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)))
print(pretty(trigsimp(sin(x)*tan(x)/sec(x))))

print("\t", expand_trig(sin(x + y)))
print("\t", expand_trig(tan(2*x)))

x, y = symbols('x y', positive=True)
a, b = symbols('a b', real=True)
z, t, c = symbols('z t c')

print("\t", powsimp(x**a*x**b))
print("\t", powsimp(x**a*y**a))
print("\t", powsimp(t**c*z**c))

print("\t", (z*t)**2)
print("\t", sqrt(x*y))

print("\t", powsimp(t**c*z**c, force=True)) #بدون فرضیات


print(pretty(tan(x).rewrite(sin)))
print()
print("\t", pretty(factorial(x).rewrite(gamma)))


expr = Integral(log(x)**2, x)
print(pretty(expr))
print("\t", expr.doit())


f, g = symbols('f g', cls=Function)
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
print(pretty(diffeq))
print()
print(pretty(dsolve(diffeq, f(x))))
