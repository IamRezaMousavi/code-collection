# @Author: @IamRezaMousavi
# @Date:   2021-12-07 13:53:17
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:16:26


import os
import tkinter as tk

from serial_ports import serial_ports


def runSerialMain():
    os.system('start cmd /k "whileTrue.py"')  # /c 'start cmd /k "serial_main.py"'
    #'start /B start cmd.exe @cmd /k python p.py'


window = tk.Tk()
window.title('Test')
window.geometry('800x400+100+100')

ports = ['COM1', 'COM2'] + serial_ports()

open_port_frame = tk.LabelFrame(window, text='Open Port', width=80, height=70)
open_port_frame.grid_propagate(False)
open_port_frame.grid(column=0, row=0, ipadx=5, ipady=5, padx=10, pady=10, sticky=tk.NW)

optionmenu_value = tk.StringVar()
optionmenu_value.set('COM?')
port_menu = tk.OptionMenu(open_port_frame, optionmenu_value, *ports)
port_menu.grid(row=0, column=0, sticky=tk.E)


def print_answers():
    port = optionmenu_value.get()
    answerLabel.config(text=port)
    filePortName = 'portname.txt'
    if os.path.exists(filePortName):
        os.system('attrib -h ' + filePortName)
        os.remove(filePortName)
    with open(filePortName, 'w') as portnamefile:
        portnamefile.write(port)
    os.system('attrib +h ' + filePortName)
    runSerialMain()


open_button = tk.Button(open_port_frame, text='Open', command=print_answers, width=8)
open_button.grid(row=1, column=0, sticky=tk.S)

status_frame = tk.LabelFrame(window, text='Status')
status_frame.grid(column=1, row=0, ipadx=5, ipady=5, padx=5, pady=5, sticky=tk.N)

answerLabel = tk.Label(status_frame)
answerLabel.grid(row=0, column=0)

save_frame = tk.LabelFrame(window, text='Save', width=80, height=70)
save_frame.grid_propagate(False)
save_frame.grid(column=0, row=4, ipadx=5, ipady=5)

fileName = tk.Entry(save_frame, width=10)
fileName.grid(row=0, column=0, sticky=tk.N)


def saveToFile():
    filename = 'data.csv'
    os.system('attrib -h ' + filename)
    file_name = fileName.get()
    os.rename('data.csv', file_name + '.csv')


saveButton = tk.Button(save_frame, text='Save to file', command=saveToFile)
saveButton.grid(column=0, row=2, sticky=tk.S, padx=5, pady=5)

window.mainloop()
