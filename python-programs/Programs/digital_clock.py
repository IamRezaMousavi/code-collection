"""Created on Wed Apr 21 07:47:29 2021

@author: Mohammad
"""

import time
from tkinter import *

window = Tk()
time1 = ''
clock = Label(window, font=('times', 80, 'bold'), bg='yellow')
clock.pack(fill=BOTH, expand=2)


def tick():
    global time1
    time2 = time.strftime('%H : %M : %S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


tick()
window.mainloop()
