# @Author: @IamRezaMousavi
# @Date:   2021-12-09 00:46:54
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:15:55


import glob
import sys

import serial


def serial_ports():
    """List serial port names"""
    if sys.platform.startswith('win'):
        ports = [f'COM{i + 1}' for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise OSError('Unsupported Platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append()
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())
