# @Author: @IamRezaMousavi
# @Date:   2022-03-20 22:45:20
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-20 22:51:34

import threading


def bigThread(threadName):
    for i in range(5):
        print(f'\tThread {threadName} -> {i} is running...')


threads = []
for i in range(4):
    t = threading.Thread(target=bigThread, args=(str(i)))
    t.start()
    threads.append(t)

for thread in threads:
    t.join()
