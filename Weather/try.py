"""Created on Sat May 15 21:26:47 2021

@author: Mohammad
"""

import json
from pprint import pprint as pp

import requests

url_base = 'http://api.openweathermap.org/data/2.5/weather?q='
cityname = 'Abadan'.title()
APIKey = '58339b029b4279319dfd339d5f21d532'
url = url_base + cityname + '&appid=' + APIKey  # + "&lang=fa"

try:
    print('Try to send a request')
    data = requests.get(url)
    data = data.json()
    data = json.dumps(data)
    print('Request is work seccessful')

    with open(cityname + '.txt', 'a+') as f:
        f.write(data)
        f.write('\n')
        print('Write is done.')

    data = json.loads(data)

except:
    print('Request is not working')
    try:
        print('Try to load from database')
        with open(cityname + '.txt') as r:
            olddata = r.readlines()
            print('Read is Seccessful.')

        data = json.loads(olddata[-1])
        pp(data)
    except:
        print('Database is not found')
else:
    pp(data)
