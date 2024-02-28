# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:26:47 2021

@author: Mohammad
"""

import requests, json
from pprint import pprint as pp

url_base = "http://api.openweathermap.org/data/2.5/weather?q="
cityname = "London"
APIKey = "58339b029b4279319dfd339d5f21d532"
url = url_base + cityname + "&appid=" + APIKey #+ "&lang=fa"

data = requests.get(url)
data = data.json()
data = json.dumps(data)

with open(cityname+".txt", "a+") as f:
    f.write(data)
    f.write("\n")
    print("Write is done.")

with open(cityname+".txt") as r:
    olddata = r.readlines()
    print("Read is Seccessful.")

newdata = json.loads(olddata[-1])
pp(newdata)
