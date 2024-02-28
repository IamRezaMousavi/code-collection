# @Author: @IamRezaMousavi
# @Date:   2021-12-09 00:20:24
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:16:05

import csv
import os

import serial


def s_in16(za):
    if za & 0x8000:
        za = -(0xFFFF - za)
    return za


with open('portname.txt') as portnamefile:
    port = portnamefile.readline()

os.system('attrib -h portname.txt')
os.system('del portname.txt')

ser = serial.Serial(
    port=port,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0,
)

print('connected to: ' + ser.portstr)

header = ('Count', 'ax', 'ay', 'az', 'Gx', 'Gy', 'Gz', 'Mx', 'My', 'Mz')
data = []

i = 0
count = 0
try:
    print('Press Ctrl-C to terminate while statement')
    while True:
        if ser.in_waiting > 0:  # Wait until there is data waiting in the serial buffer
            ss = (
                ser.readline()
            )  # Read data out of the buffer until a carraige return / new line is found

            if ss[0] == 170 and ss[1] == 187 and len(ss) == 25:
                print(ss, len(ss))
                count = (ss[5] << 24) | (ss[4] << 16) | (ss[3] << 8) | (ss[2])
                print(count)
                ax = (s_in16((ss[7] << 8) | (ss[6]))) * 16 * 9.81 / 32768
                ay = (s_in16((ss[9] << 8) | (ss[8]))) * 16 * 9.81 / 32768
                az = (s_in16((ss[11] << 8) | (ss[10]))) * 16 * 9.81 / 32768

                gx = 2000 * (s_in16((ss[13] << 8) | (ss[12]))) / 32768
                gy = 2000 * (s_in16((ss[15] << 8) | (ss[14]))) / 32768
                gz = 2000 * (s_in16((ss[17] << 8) | (ss[16]))) / 32768

                mx = s_in16((ss[19] << 8) | (ss[18]))
                my = s_in16((ss[21] << 8) | (ss[20]))
                mz = s_in16((ss[23] << 8) | (ss[22]))
                data_sensor = (count, ax, ay, az, gx, gy, gz, mx, my, mz)
                data.append(data_sensor)

except KeyboardInterrupt:
    pass

filename = 'data.csv'
if os.path.exists(filename):
    os.system('attrib -h ' + filename)
with open(filename, 'w', newline='') as filecsv:
    out = csv.writer(filecsv)
    out.writerow(header)
    out.writerows(data)
os.system('attrib +h ' + filename)

ser.close()
