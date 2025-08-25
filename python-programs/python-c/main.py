# @Author: @IamRezaMousavi
# @Date:   2022-12-20 14:09:51
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-12-20 15:30:41

import ctypes
import sys
import os
from ctypes import POINTER, c_double, c_size_t


class MyLib:
    def __init__(self):
        if sys.platform.startswith('win'):
            libname = 'mylib.dll'
        else:
            libname = 'libmylib.so'

        libpath = os.path.join(os.path.dirname(__file__), libname)
        self.lib = ctypes.CDLL(libpath)

        self.lib.dot.argtypes = [POINTER(c_double), POINTER(c_double), c_size_t]
        self.lib.dot.restype = c_double

        self.lib.circle_area.argtypes = [c_double]
        self.lib.circle_area.restype = c_double

        self.lib.pi.argtypes = []
        self.lib.pi.restype = c_double

    def dot(self, array1: list[float], array2: list[float]) -> float:
        if len(array1) != len(array2):
            raise ValueError('lists must have the same length')
        arr1 = (c_double * len(array1))(*array1)
        arr2 = (c_double * len(array2))(*array2)
        return self.lib.dot(arr1, arr2, len(arr1))

    def circle_area(self, r: float) -> float:
        return self.lib.circle_area(r)

    def pi(self) -> float:
        return self.lib.pi()


if __name__ == '__main__':
    lib = MyLib()
    print('dot([1.0, 2.0], [3.0, 4.0]) =', lib.dot([1.0, 2.0], [3.0, 4.0]))
    print('circle_area(2.0) =', lib.circle_area(2.0))
    print('PI =', lib.pi())
