# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-02-11 02:56:39
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 02:57:05


import numpy 
a = numpy.arange(10) 
expr = sin(x)
f = lambdify(x, expr, "numpy") #lambda in sp
print("\t", f(a))
#or
f = lambdify(x, expr, "math")
print("\t", f(0.1))
#or
def mysin(x):
    return x
f = lambdify(x, expr, {"sin":mysin})
print("\t", f(0.1))


pprint(Integral(sqrt(1/x), x), use_unicode=False) #to output
print(pretty(Integral(sqrt(1/x), x), use_unicode=False)) #to string
