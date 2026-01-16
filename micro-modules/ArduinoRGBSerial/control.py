# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-03-30 22:20:55
# @Last Modified by:   Reza Mousavi
# @Last Modified time: 2026-01-16 06:32:36

from serial import Serial

def main():
    with Serial("com3", 9600) as arduino:
        while arduino.isOpen():
            try:
                numbers = input("Enter RGB?")
                arduino.write(str.encode(numbers))
                print(arduino.readline().decode())
            except KeyboardInterrupt:
                print("Break")
                break

if __name__ == "__main__":
    main()
