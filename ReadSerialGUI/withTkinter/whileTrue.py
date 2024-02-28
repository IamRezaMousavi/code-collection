# @Author: @IamRezaMousavi
# @Date:   2021-12-13 16:30:46
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:15:42


import csv
import os
from time import sleep

os.system('attrib -h portname.txt')
os.system('del portname.txt')

index = 0
data = []
try:
    print('Press Ctrl-C to terminate while statement')
    while True:
        data.append(index)
        print(index)
        index += 1
        sleep(1)

except KeyboardInterrupt:
    pass

filename = 'data.csv'
if os.path.exists(filename):
    os.system('attrib -h ' + filename)

with open(filename, 'w', newline='') as filecsv:
    out = csv.writer(filecsv)
    for index in data:
        out.writerow(str(index))
os.system('attrib +h ' + filename)
