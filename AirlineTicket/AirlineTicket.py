"""Created on Wed Jun  2 17:45:04 2021

@author: Mohammad
"""

import json
from datetime import datetime

managers = dict()
parvaz = dict()


def loadData(data):
    with open(data.title() + '.json') as jsonfile:
        newdata = json.load(jsonfile)
    return newdata


def addManager(name, family):
    global managers
    today = datetime.today()
    y, mo, d = today.year, today.month, today.day
    key_manager = str(10) + str(y) + str(mo) + str(d) + str(len(managers))
    managers[key_manager] = {'name': name.title(), 'family': family.title()}
    return key_manager


def saveData(data):
    with open(data.title() + '.json', 'w') as jsonfile:
        json.dump(eval(data), jsonfile)
    print(f'Save {data} data is seccessful.')


def addParvaz(start, end, price, chair):
    global parvaz
    today = datetime.today()
    y, mo, d = today.year, today.month, today.day
    key_parvaz = str(20) + str(y) + str(mo) + str(d) + str(len(parvaz))
    parvaz[key_parvaz] = {
        'start': start.title(),
        'end': end.title(),
        'price': price,
        'chair': [0] * chair,
    }
    print(f'Parvaz {key_parvaz} from {start} to {end} by {price} $ with {chair} chairs.')
