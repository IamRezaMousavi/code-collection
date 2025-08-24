"""Created on Sun May 16 15:39:55 2021

@author: Mohammad
"""

from xlwt import Workbook

wb = Workbook()
temp = wb.add_sheet('Temp')

k = 0
for i in range(15):
    temp.write(0, i, k)
    k += 1
wb.save('TempDataTestByExcel.xls')
