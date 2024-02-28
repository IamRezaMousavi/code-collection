# @Author: @IamRezaMousavi
# @Date:   2022-01-06 06:52:51
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:12:50

import random
from datetime import datetime

import serial


class Communication:
    def __init__(self, portName='0'):
        self.baudrate = 9600
        self.portName = portName
        self.ser = serial.Serial()
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
        except serial.serialutil.SerialException:
            self.dummyMode = True

    def close(self):
        if self.ser.isOpen():
            self.ser.close()

    def getData(self):
        if self.isOpen():
            value = self.ser.readline()
            decoded_bytes = str(value[0 : len(value) - 2].decode('utf-8'))
            value_chain = decoded_bytes.split(',')
        elif self.dummyMode:
            now = datetime.now().second + (datetime.now().microsecond / 10**6)
            value_chain = (
                [now]
                + random.sample(range(300), 1)
                + [random.getrandbits(1)]
                + random.sample(range(20), 8)
            )
        return value_chain

    def isOpen(self):
        return self.ser.isOpen()
