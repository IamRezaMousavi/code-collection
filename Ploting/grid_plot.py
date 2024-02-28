# @Author: @IamRezaMousavi
# @Date:   2021-09-25 23:01:38
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-11 02:03:51


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_yticks(np.arange(0.2, 0.8, 0.2), minor=False)
ax.set_yticks(np.linspace(0.2, 0.8, 60), minor=True)

ax.yaxis.grid(True, which='major', linewidth=0.8)
ax.yaxis.grid(True, which='minor', linewidth=0.4)

plt.show()
