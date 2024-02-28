# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-12-20 14:09:51
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-12-20 15:30:41

import ctypes
import sys

if sys.platform.startswith('win'):
    libname = "./funcs.dll"

cfunc = ctypes.CDLL(libname)

cfunc.PI.restype = ctypes.c_float

print(cfunc.PI())

cfunc.getF.restype = ctypes.c_float
print(cfunc.getF(ctypes.c_float(22.5)))
