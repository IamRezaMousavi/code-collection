# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:37:10 2021

@author: Mohammad
"""

from pprint import pprint as pp
import json

with open("Data.txt") as r:
    newdata = r.readlines()
    print("Read is Seccessful.")

newdata2 = json.loads(newdata[-1])
pp(newdata2)
