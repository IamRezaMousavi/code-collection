# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:46:54 2021

@author: Mohammad
"""

import requests, json
from pprint import pprint as pp
import pprint
from xlwt import Workbook
 
#url_base = "http://api.openweathermap.org/data/2.5/weather?q="

url_base = "http://api.openweathermap.org/data/2.5/forecast?q="

#cityname = input("Enter city name:").title()
cityname = "Abadan"
APIKey = "58339b029b4279319dfd339d5f21d532"
url = url_base + cityname + "&appid=" + APIKey #+ "&lang=fa"

try:
    print("Try to send a request")
    data = requests.get(url)
    data = data.json()
    data = json.dumps(data)
    print("Request is work seccessful")

    with open(cityname+"2.txt", "a+") as f:
        f.write(data)
        f.write("\n")
        print("Write is done.")
    
    data = json.loads(data)

except:
    print("Request is not working")
    try:
        print("Try to load from database")
        with open(cityname+"2.txt") as r:
            olddata = r.readlines()
            print("Read is Seccessful.")
    
        data = json.loads(olddata[-1])
        pp(data)
    except:
        print("Database is not found")
else:
    pp(data)

data["city"]["name"] = cityname

print()
prettydata = pprint.pformat(data)
with open(cityname + "PrettyData.txt", "w") as pd:
    pd.write(prettydata)
print(cityname + " Pretty Data was written")

print()
now = data["list"][0]["dt_txt"]
far = data["list"][0]["main"]["temp"]
print("Temp of ", now," is ", far, " f")
c = data["list"][0]["main"]["temp"] - 273.15
print("Temp of ", now," is ", c, " c")

temp = []
temptime = []
for i in range(len(data["list"])):
    temp += [data["list"][i]["main"]["temp"]]
    temptime += [int((data["list"][i]["dt"]-data["list"][0]["dt"])/3600)]

wb = Workbook()
tempsheet = wb.add_sheet("TempData")
for i in range(len(data["list"])):
    tempsheet.write(0,i,temp[i])
    tempsheet.write(1,i,temptime[i])
wb.save(cityname + "TempData.xls")
