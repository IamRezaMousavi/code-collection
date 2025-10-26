# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-02-11 01:36:31

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6.3, 100)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('sin_plot.png', format='png', dpi=1000, transparent=False)
plt.show()
