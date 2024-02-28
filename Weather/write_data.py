# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:26:47 2021

@author: Mohammad
"""

import requests, json

url_base = "http://api.openweathermap.org/data/2.5/weather?q="
#cityname = input("Please type a city name: ")
#cityname = cityname.lower()
cityname = "abadan"
APIKey = "58339b029b4279319dfd339d5f21d532"
url = url_base + cityname + "&appid=" + APIKey #+ "&lang=fa"
#print(url)
data = requests.get(url)
data1 = data.json()
data2 = json.dumps(data1)
with open("Data.txt", "a+") as f:
    f.write(data2)
    f.write("\n")
    print("Write is done.")
