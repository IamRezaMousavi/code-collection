# -*- coding: utf-8 -*-
# @Author: S.Reza Mousavi
# @Date:   2022-01-24 18:39:16
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-01-24 18:43:49


import psutil
from psutil._common import bytes2human

def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != "percent":
            value = bytes2human(value)
        print("%-10s : %7s" % (name.capitalize(), value))

def main():
    print("MEMORY\n------")
    pprint_ntuple(psutil.virtual_memory())
    print("\nSWAP\n--------")
    pprint_ntuple(psutil.swap_memory())


if __name__ == "__main__":
    main()
