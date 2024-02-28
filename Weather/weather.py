# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 07:29:59 2021

@author: Mohammad
"""

import requests

url_base = "http://api.openweathermap.org/data/2.5/weather?q="
#cityname = input("Please type a city name: ")
#cityname = cityname.lower()
cityname = "tehran"
APIKey = "58339b029b4279319dfd339d5f21d532"
url = url_base + cityname + "&appid=" + APIKey #+ "&lang=fa"
#print(url)
data = requests.get(url)
data = data.json()
#print(data)
if data["cod"] == "404":
    print("City not found")
else:
    print("OK")
    temp = data["main"]["temp"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    description = data["weather"][0]["description"]
    print("Temp: " + str(round(temp-273.15, 2)) + " c")
    print("Temp Max: " + str(round(temp_max-273.15, 2)) + " c")
    print("Temp Min: " + str(round(temp_min-273.15, 2)) + " c")
    print("Pressure: " + str(pressure) + " hPa")
    print("Humidity: " + str(humidity) + "%")
    print("Wind Speed: " + str(round(wind_speed * 1.609, 2)) + " km/h")
    print("Wind Degree: " + str(wind_deg) + "")
    print("Description: " + description)
