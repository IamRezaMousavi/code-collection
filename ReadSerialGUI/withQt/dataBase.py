# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-01-06 06:52:51
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:11:45

import time
import csv


class DataBase():
    def __init__(self):
        self.state = False

    def guardar(self, data, fileName):
        if self.state == True:
            data.append(time.asctime())
            fileName = "data" if fileName == "" else fileName
            with open(fileName + ".csv", "a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(data)

    def start(self):
        self.state = True

    def stop(self):
        self.state = False
