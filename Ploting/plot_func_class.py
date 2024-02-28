"""Created on Wed Jul  7 16:02:35 2021

@author: Mohammad
"""

import math

import matplotlib.pyplot as plt
import numpy as np


class Chart:
    def __init__(self, func):
        self.function = func.split('.')[1]
        self.func = lambda x: eval(func)

    def __str__(self):
        return self.function

    def drawChart(self, start, stop, n=100):
        x = np.linspace(start, stop, n)
        y = [self.func(i) for i in x]
        plt.plot(x, y)
        plt.show()


sin = Chart('math.sin(x)')
sin.drawChart(-math.pi, 2 * math.pi)
print(sin)

exp = Chart('math.exp(x)')
exp.drawChart(0, 10)
print(exp)
