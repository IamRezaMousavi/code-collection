# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:32:56
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2021-12-31 22:48:32

import random
import time
from datetime import datetime

odds = list(range(1, 60, 2))

for i in range(4):
    right_this_minute = datetime.today().minute
    print('Minute ', right_this_minute, ' is')
    if right_this_minute in odds:
        print('An Odd Minute')
    else:
        print('Not An Odd Minute')
    wait_time = random.randint(1, 5)
    print('Wait Time For')
    print(wait_time, ' secund')
    print('************')
    time.sleep(wait_time)
