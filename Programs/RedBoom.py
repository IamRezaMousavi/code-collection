"""Created on Thu Apr 22 01:24:11 2021

@author: Mohammad
"""

import time
import tkinter as tk
from datetime import datetime

font_calender = 'Freestyle Script'
font_clock = 'Comic Sans MS'
font_name = 'Segoe Print'

window = tk.Tk()
window.title('Red Boom')

date1 = ''
calendar = tk.Label(window, font=(font_calender, 30), anchor='center')
calendar.config(bg='#140000', fg='white')
calendar.pack(fill=tk.BOTH, expand=2)

time1 = ''
clock = tk.Label(window, font=(font_clock, 80, 'bold'))
clock.config(bg='#140000', fg='white')
clock.pack(fill=tk.BOTH, expand=2)

name = tk.Label(window, font=(font_name, 10), anchor='se', bg='#140000', fg='white', text='Mousavi')
name.pack(fill=tk.BOTH, expand=2)


def tick():
    global time1
    time2 = time.strftime('%H : %M : %S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        if int(time.strftime('%S')) >= 00:
            clock.config(fg='#ffffff')
        if int(time.strftime('%S')) >= 5:
            clock.config(fg='#ffebeb')
        if int(time.strftime('%S')) >= 10:
            clock.config(fg='#ffc4c4')
        if int(time.strftime('%S')) >= 15:
            clock.config(fg='#ffb1b1')
        if int(time.strftime('%S')) >= 20:
            clock.config(fg='#ff9d9d')
        if int(time.strftime('%S')) >= 25:
            clock.config(fg='#ff8989')
        if int(time.strftime('%S')) >= 30:
            clock.config(fg='#ff7676')
        if int(time.strftime('%S')) >= 35:
            clock.config(fg='#ff6262')
        if int(time.strftime('%S')) >= 40:
            clock.config(fg='#ff4e4e')
        if int(time.strftime('%S')) >= 45:
            clock.config(fg='#ff3b3b')
        if int(time.strftime('%S')) >= 50:
            clock.config(fg='#ff2727')
        if int(time.strftime('%S')) >= 55:
            clock.config(fg='#ff1414')
    clock.after(200, tick)


def isdate():
    global date1
    date2 = datetime.today().strftime('%A %B %d, %Y')
    if date2 != date1:
        date1 = date2
        calendar.config(text=date2)
    calendar.after(200, isdate)


isdate()
tick()
window.mainloop()
