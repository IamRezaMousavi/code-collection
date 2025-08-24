"""Created on Wed Apr 14 01:21:59 2021

@author: Mohammad
"""

import tkinter as tk

window = tk.Tk()
lbl = tk.Label(master=window)


def ok():
    word = scan.get()
    if word == 'reza':
        lbl.config(text='OK')
        lbl.grid(columnspan=3)
    else:
        lbl.config(text='No')
        lbl.grid(columnspan=3)


window.title('Mohammad')
window.configure(bg='white')
# window.geometry("235x250+300+150")
l = tk.Label(window, text='This is a label')
scan = tk.Entry()
b = tk.Button(
    window,
    text='Button',
    bg='red',
    fg='white',
    command=ok,
    activebackground='blue',
    activeforeground='yellow',
)
b1 = tk.Button(
    window,
    text='Button1',
    bg='red',
    fg='white',
    command=ok,
    activebackground='blue',
    activeforeground='yellow',
)

b2 = tk.Button(
    window,
    text='Button2',
    bg='red',
    fg='white',
    command=ok,
    activebackground='blue',
    activeforeground='yellow',
)

b3 = tk.Button(
    window,
    text='Button3',
    bg='red',
    fg='white',
    command=ok,
    activebackground='blue',
    activeforeground='yellow',
)


l.grid(columnspan=3)
scan.grid(columnspan=3)
b.grid(row=2, column=1)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
window.mainloop()
