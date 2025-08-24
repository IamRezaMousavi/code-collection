# @Author: S.Reza Mousavi
# @Date:   2022-01-24 18:03:30
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-01-24 18:44:35


import psutil

print('CPU Count:', psutil.cpu_count(logical=False))

for _ in range(10):
    print('CPU:', psutil.cpu_percent(interval=0.1, percpu=True), '\tRAM:', psutil.virtual_memory())

print('CPU Frequence:', psutil.cpu_freq(percpu=True))
print('Load Average:', psutil.getloadavg())
